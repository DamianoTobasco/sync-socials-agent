"""Validate and reproducibly package the credential-free hosted Claude plugin."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile


PACKAGE = Path(__file__).resolve().parents[1] / "plugins" / "claude-sync-socials"
FILES = {
    ".claude-plugin/plugin.json",
    ".claude-plugin/icon.png",
    ".mcp.json",
    "README.md",
    "LICENSE",
    "skills/social-publishing/SKILL.md",
}
ENDPOINT = "https://app.sync-socials.com/api/mcp"
TOOLS = {
    "syncsocials_get_workspace", "syncsocials_list_connections",
    "syncsocials_list_media", "syncsocials_upload_media_from_url",
    "syncsocials_create_content_draft", "syncsocials_get_brand_profile",
    "syncsocials_generate_viral_concepts", "syncsocials_produce_viral_video",
    "syncsocials_create_post", "syncsocials_get_post", "syncsocials_list_posts",
    "syncsocials_update_post", "syncsocials_publish_post", "syncsocials_delete_post",
}


def validate(mcp_source):
    entries = list(PACKAGE.rglob("*"))
    if any(entry.is_symlink() for entry in entries):
        raise ValueError("Plugin files and directories must not be symlinks")
    actual = {entry.relative_to(PACKAGE).as_posix() for entry in entries if entry.is_file()}
    if actual != FILES:
        raise ValueError(f"Unexpected package files: {sorted(actual ^ FILES)}")
    manifest = json.loads((PACKAGE / ".claude-plugin/plugin.json").read_text())
    if manifest["name"] != "sync-socials" or not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
        raise ValueError("Keep the released plugin identity and use a semantic version")
    expected_mcp = {"mcpServers": {"sync-socials": {"type": "http", "url": ENDPOINT}}}
    if json.loads((PACKAGE / ".mcp.json").read_text()) != expected_mcp:
        raise ValueError("The plugin must use the canonical HTTPS endpoint without credentials")
    skill = (PACKAGE / "skills/social-publishing/SKILL.md").read_text()
    if not skill.startswith("---\nname: social-publishing\ndescription:"):
        raise ValueError("Invalid publishing skill frontmatter")
    referenced_tools = set(re.findall(r"\bsyncsocials_[a-z_]+\b", skill))
    if referenced_tools != TOOLS:
        raise ValueError(f"Skill tool contract differs: {sorted(referenced_tools ^ TOOLS)}")
    if mcp_source:
        registered = set(re.findall(r'registerTool\(\s*"(syncsocials_[a-z_]+)"', mcp_source.read_text()))
        hosted = registered - {"syncsocials_upload_media_from_local_file"}
        if hosted != TOOLS:
            raise ValueError(f"MCP source tool contract differs: {sorted(hosted ^ TOOLS)}")
    if len((PACKAGE / "README.md").read_text().split()) < 40:
        raise ValueError("Directory README must contain at least 40 words")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Output ZIP path")
    parser.add_argument("--mcp-source", type=Path, help="Optional deployed app mcp-server.ts contract check")
    args = parser.parse_args()
    manifest = validate(args.mcp_source)
    output = args.output.resolve()
    if output.is_relative_to(PACKAGE):
        raise ValueError("The archive must be outside the plugin folder")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(FILES):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(entry, (PACKAGE / name).read_bytes())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("Archive integrity check failed")
        for name in FILES:
            if archive.read(name) != (PACKAGE / name).read_bytes():
                raise ValueError(f"Archive/source mismatch: {name}")
    print(json.dumps({
        "version": manifest["version"], "archive": str(output),
        "bytes": output.stat().st_size,
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "files": sorted(FILES), "claude_tool_count": len(TOOLS),
    }, indent=2))


if __name__ == "__main__":
    main()
