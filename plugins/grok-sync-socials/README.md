# Sync Socials for Grok Build

Create social drafts, import existing media, schedule approved posts, and check
publishing results from Grok Build. This package contains one publishing skill
and a hosted MCP connection. It starts no local server, installs no dependencies,
and includes no hooks or executable scripts.

This is a source-distributed plugin. An official Grok Build marketplace listing
and successful Grok runtime tests are not claimed. Installing the package does
not connect a workspace or a social account automatically.

## Connect your workspace

1. Sign in to [Sync Socials](https://app.sync-socials.com) and select your workspace.
   An eligible Growth workspace with API access is required. In workspace
   settings, create or use your own API key. Growth supports one active key;
   replacing or revoking a key also affects other clients using that key.
2. Make that key available to the Grok process as `SYNC_SOCIALS_API_KEY`, using
   your own environment or secret-management setup. Do not add it to this
   package, a project `.env` file, source control, chat, or screenshots. The
   package contains only the variable reference, never a shared credential.
3. Install and trust the package from its public source:

   ```bash
   grok plugin install 'DamianoTobasco/sync-socials-agent#plugins/grok-sync-socials' --trust
   ```

4. Start Grok with the environment variable available. Open `/plugins` to check
   that Sync Socials is enabled, then `/mcps` to check its connection. Restart
   Grok after changing the environment. `grok mcp doctor` can diagnose connection
   failures; redact credentials before sharing diagnostics.

For a temporary terminal session on macOS or Linux, this Bash command prompts
without echoing the key or putting its value in shell history. Exit Grok to end
that session:

```bash
bash -c 'read -r -s -p "Sync Socials API key: " SYNC_SOCIALS_API_KEY; printf "\n"; test -n "$SYNC_SOCIALS_API_KEY" || exit 1; export SYNC_SOCIALS_API_KEY; exec grok'
```

The connection uses Streamable HTTP at
`https://app.sync-socials.com/api/mcp`, with
`Authorization: Bearer ${SYNC_SOCIALS_API_KEY}`. Grok expands the variable at load
time. This package uses API-key authentication, without an OAuth client secret
or a registered Grok OAuth flow. If authentication fails, check that the variable
is available to the Grok process, the key is current, and the workspace has API
access. Do not reuse another customer’s or a directory reviewer’s credentials.

Grok can also discover existing Claude MCP configuration. Use one active Sync
Socials connection for the intended workspace; resolve a conflicting older
definition in `/mcps` before trying writes. The separately published Claude Chat
and Cowork plugin has a different connection flow.

## Create your first draft

After connecting, ask:

> Read my Sync Socials workspace, then create an untargeted draft titled
> "Getting started" with the caption "Our first post is coming soon."
> Return the draft ID and confirm it is still a draft.

This needs no social account, media asset, or AI-generation provider. Open the
draft in Sync Socials to review it. Connect destinations in
[Connections](https://app.sync-socials.com/app/connections) when you are ready to
schedule or publish.

Supported destinations depend on the accounts and capabilities returned by the
service. Facebook targets Pages; Instagram requires a professional account
linked to a Facebook Page. X/Twitter publishing is unsupported by this connector.

The skill defaults to drafts. Scheduling, publishing, and deletion follow your
explicit requests and selected content/accounts. Queued or processing results
are reported as pending until a subsequent status read confirms completion.

## Media, generation, and access

- Reuse workspace media or import a user-provided HTTPS media URL. A path on the
  Grok user's computer is not a path on the hosted Sync Socials server. Upload
  local attachments through the Sync Socials media library first. Any advertised
  server-local import tool is limited to the server's allowed roots and is not a
  client-device upload mechanism.
- Hosted text concepts require a configured workspace AI provider and use its
  allowance. Grok access does not supply those provider credits.
  `syncsocials_produce_viral_video` supports `library` and `remix` assembly using
  existing footage, text overlays, and an existing soundtrack. That tool does
  not generate images, footage, speech, or music through AI models and uses the
  workspace's production allowance.
- The key is revocable and bound to one workspace. It grants the API's read/write
  operations within that workspace, including publishing and deletion when their
  prerequisites are met; it is not read-only or restricted to individual tools.
  Never connect a workspace you do not intend the agent to operate.
- Normal plan, request, mutation, upload, and rate limits apply. Read current
  allowances with `syncsocials_get_workspace`; stop on quota or access errors.

## Data and network access

The plugin's MCP connection sends authenticated tool requests only to
`https://app.sync-socials.com/api/mcp`. It does not collect telemetry or scan local
files. Inputs may include captions, business briefs, supplied website/media URLs,
post and media IDs, account selections, schedules, and privacy choices.

The hosted service stores requested drafts and schedules, imports requested
media, and sends approved posts to selected social platforms. Text-concept
requests can use a supplied website and the workspace's configured AI provider.
Video assembly uses existing assets. These are service-side actions initiated by the selected tools, not
additional local plugin processes. See [Privacy](https://app.sync-socials.com/privacy)
and [Terms](https://app.sync-socials.com/terms).

## Validation and distribution

From the repository root, with Grok Build installed:

```bash
grok plugin validate ./plugins/grok-sync-socials
```

Structural validation does not establish authenticated Grok compatibility.
Before claiming that result, verify discovery, the expected workspace, an
untargeted draft, and its subsequent status through Grok using an authorized
workspace. Use only disposable data for any deletion test. No publishing or
generation is needed for the first-draft check.

An official marketplace submission references this directory in the public
repository at a full commit SHA. Source publication and a marketplace PR are
separate from xAI review, acceptance, and each user's decision to install.

References: [Grok plugin documentation](https://docs.x.ai/build/features/skills-plugins-marketplaces),
[MCP configuration](https://docs.x.ai/build/features/mcp-servers), and
[xAI marketplace contribution guide](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md).

## License and support

MIT. See [LICENSE](LICENSE). Maintained by Sync Socials / EvolveAI LLC, with source
published by Damiano Tobasco in the [Sync Socials Agent repository](https://github.com/DamianoTobasco/sync-socials-agent).
Product: [Sync Socials](https://sync-socials.com).
Support: [contactsyncsocials@gmail.com](mailto:contactsyncsocials@gmail.com).
