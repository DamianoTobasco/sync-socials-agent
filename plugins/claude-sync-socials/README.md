# Sync Socials for Claude

Manage social drafts, existing media, scheduled posts, and publishing status from
Claude through your Sync Socials workspace. This plugin bundles the hosted Sync
Socials MCP connector and one social-publishing skill.

**Release status: candidate source, not published in the Claude directory.** Public authentication and
end-to-end testing of this combined package are pending. This package is not yet
ready for public installation. Its manifest version is 0.2.0; this is a candidate
version, not evidence of a public release.

## What you can do

- Inspect your workspace, connected social accounts, media library, and queue.
- Save caption ideas as drafts without choosing an account.
- Create or edit posts using existing images and videos.
- Schedule or publish selected posts when you explicitly request it.
- Check results or cancel a selected scheduled post before publication.

The skill defaults to drafts. It preserves post fields you did not ask to change
and verifies write results before reporting success. Available destinations and
allowances depend on your workspace and connected accounts.

Text concepts require a configured workspace AI provider and use its allowance.
Existing-video editing assembles footage, text overlays, and an existing
soundtrack. This connector does not generate images, footage, speech, or music
through AI models.

## Connection requirements

You need a Sync Socials workspace with API access and workspace-owner approval.
Connect social accounts in Sync Socials before targeting a post.

The plugin declares the remote HTTPS endpoint
`https://app.sync-socials.com/api/mcp`. It does not contain credentials or
authenticate an account merely by being installed. In Chat and Cowork, connect
Sync Socials from the plugin's **Connectors** tab and complete the secure sign-in
and workspace-consent flow. On Team and Enterprise plans, an Owner may first need
to add the connector for the organization. Claude Code uses its own `/mcp`
connection interface; direct authentication for this candidate remains untested.

The private preview used a dedicated confidential OAuth client. Public hosted
authentication depends on Anthropic holding the required client secret, which
remains pending. The developer portal permits a connector submission with that
publication gate, but the connector cannot publish until it is resolved. Never
paste an application client secret, access token, or social password into chat,
this package, or an ordinary email.

See the [Sync Socials setup guide](https://sync-socials.com/claude.html) for current
availability. If tools are missing or sign-in fails, the skill reports the
connection requirement instead of switching to another authentication method.

## Data and behavior

The bundle contains Markdown, JSON, a PNG brand icon, and its license. It starts no local
process, installs no dependencies, and changes no Claude permissions. The
declared MCP connection sends tool requests to Sync Socials over HTTPS after
the user connects their account.

Depending on your request, tool inputs can include captions, business briefs,
website or media URLs, media and post IDs, selected account IDs, schedules, and
privacy choices. Sync Socials stores drafts and schedules, imports requested
media, and sends approved posts to selected social services. Concept requests
can fetch a supplied website and use the workspace's configured AI provider.
The [Sync Socials privacy policy](https://app.sync-socials.com/privacy) applies.

## Validation and availability

The previous skills-only 0.1.0 private preview passed a workspace-read smoke test
in Chat and Cowork using an already authenticated connector. Those tests do not
verify this combined 0.2.0 candidate, a new user's authentication, write
workflows, or Claude Code.

Before publication, this candidate needs successful new-user sign-in, workspace
consent, revocation and reconnect tests, workflow checks on each advertised
Claude surface and the developer portal's
validation and review. Local syntax validation does not establish any of those
results. Neither directory submission nor approval is claimed by this package.

## Source

This plugin lives at [`plugins/claude-sync-socials`](https://github.com/DamianoTobasco/sync-socials-agent/tree/main/plugins/claude-sync-socials)
in the public [Sync Socials Agent repository](https://github.com/DamianoTobasco/sync-socials-agent).
The repository's root agent-neutral skill and API-key setup are separate from
this Claude OAuth bundle. Publishing source does not make this plugin available
in the Claude directory or complete its authentication setup.

## License and support

MIT, copyright 2026 Damiano Tobasco. See [LICENSE](LICENSE).

Product: [Sync Socials](https://sync-socials.com). Documentation:
[Claude setup guide](https://sync-socials.com/claude.html). Support:
[contactsyncsocials@gmail.com](mailto:contactsyncsocials@gmail.com).
