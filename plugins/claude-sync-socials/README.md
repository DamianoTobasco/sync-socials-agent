# Sync Socials for Claude

Manage social drafts, existing media, scheduled posts, and publishing status from
Claude through your Sync Socials workspace. This plugin bundles the hosted Sync
Socials MCP connector and one social-publishing skill.

**Sync Socials is published in the Claude directory for Claude apps and Cowork.**
[View the public plugin](https://claude.ai/customize/plugins/id/f091ce5c-7b5a-4d77-9f15-30495acd504a%40anthropic-plugin-directory).
The connector remains in review. The published package passed hosted tests
using an existing custom connection, and a separate fresh custom-connector test
passed with public OAuth and PKCE, without a client secret. The directory now
uses that tested public-client configuration; fresh sign-in through the directory
listing and connector/plugin pairing are not yet verified. In Claude Code, the
tools come from a Sync Socials connector connected in your Claude account;
Claude Code's own sign-in to the server URL is not supported.

## What you can do

- Inspect your workspace, connected social accounts, media library, and queue.
- Save caption ideas as drafts without choosing an account.
- Create or edit posts using existing images and videos.
- Upload images and videos from your computer when Claude can run commands
  there, as in Claude Code or Cowork.
- Schedule or publish selected posts when you explicitly request it.
- Check results or cancel a selected scheduled post before publication.

The skill defaults to drafts. It preserves post fields you did not ask to change
and verifies write results before reporting success. Available destinations and
allowances depend on your workspace and connected accounts.

Facebook Pages and Instagram professional accounts are available to new and
existing Sync Socials customers following Meta approval. Connect each destination
in [Sync Socials Connections](https://app.sync-socials.com/app/connections) and
grant publishing access. Instagram requires a business or creator account linked
to a Facebook Page and image or video content. Personal Facebook profiles and
personal Instagram accounts cannot be publishing destinations. Reconnect an older
connection if it is missing publishing access. Meta approval and Claude directory
connector review are separate processes.

The same workspace tools also support TikTok, YouTube, LinkedIn personal
profiles, Threads, Bluesky, Telegram, Discord, and Slack when those destinations
are connected and enabled. TikTok needs your privacy level and posting consent
before scheduling or publishing. X is available on active paid Growth; trials and
unpaid review access exclude it.

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
to add the connector for the organization. These connection steps require a
working hosted OAuth configuration. The directory configuration is saved; fresh
sign-in through the directory connector remains unverified while its review and
pairing are pending.

This release is listed for Claude apps and Cowork. In Claude Code, connect Sync
Socials in your Claude account first; Claude Code signed in with that account
loads the connector in a new session, and the plugin's skill uses its tools.
Claude Code's own sign-in to the plugin's URL-only server uses a local callback
that Sync Socials does not accept. The separately documented agent-neutral
API-key setup is not this plugin's authentication flow.

The new public OAuth client uses the authorization-code flow with required
S256 PKCE and no client secret. Fresh custom-connector sign-in, workspace access,
and token refresh have passed testing. The directory connector is configured to
use this tested public client with no client secret, replacing the earlier
confidential-client handoff requirement. Those tests do not yet verify sign-in
through the actual directory listing. Never
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
privacy choices. To upload a file from your computer, Claude sends its name,
type, and size, then runs one `curl` command that sends only that file to Sync
Socials over HTTPS with a one-time upload token. Sync Socials stores drafts and
schedules, imports requested media, and sends approved posts to selected social
services. Concept requests
can fetch a supplied website and use the workspace's configured AI provider.
The [Sync Socials privacy policy](https://app.sync-socials.com/privacy) applies.

## Validation and availability

Version 0.2.5 combines the two unsubmitted updates and the platforms production
reported on October 27. From 0.2.4, the publishing skill uploads images and
videos from the user's computer with the hosted `syncsocials_create_media_upload`
and `syncsocials_complete_media_upload` tools when Claude can run shell commands,
and still asks for a media-library upload without a shell. From 0.2.3, it adds
X on paid Growth: eligibility, workspace/account allowances, weighted caption and
media limits, and recovery instructions for ambiguous X outcomes. It also adds
TikTok, Threads, and Bluesky details and the Claude Code connection path. The MCP
URL and authentication flow are unchanged. Version 0.2.2 remains the recorded
published directory package until 0.2.5 passes its scan and is published; a
local version bump is not publication.

The hosted MCP already supports X through the existing post tools. Before
selecting X, read workspace `xUsage` and `postingCapabilities`, then the selected
connection's capabilities. Trials and unpaid review access exclude X. See the
bundled [X workflow](skills/social-publishing/SKILL.md#x-publishing) for limits.

Version 0.2.2 updated the publishing skill for Facebook Pages and linked Instagram
professional accounts, added explicit queue lookup guidance, and corrected the
unsupported Claude Code OAuth instruction.

The public 0.2.0 package passed directory validation and its security scan, was
published, and was installed through its public listing. Hosted tests verified
the public plugin's skill and a successful workspace read in both Chat and
Cowork. An isolated untargeted text draft was created, updated, and fetched to
verify its final caption and draft status, with no accounts, media, or schedule.
That test did not publish content.

The public-package checks above used an existing custom OAuth connection. A
separate fresh custom connector completed reviewer sign-in, workspace consent,
the hosted callback, discovery of all 14 tools, and a live workspace read using
the new public OAuth client without a secret. Protocol checks against the
canonical endpoint verified required S256 PKCE, rejection of a wrong verifier,
authorization-code exchange without a secret, and refresh-token rotation with
successful access afterward.

The public-client directory configuration is saved. Fresh sign-in through the
actual directory listing, disconnect/reconnect, connector review/pairing, and
broader workflow tests remain outstanding. Directory publication and local
syntax validation do not establish those results.

## Source

This plugin lives at [`plugins/claude-sync-socials`](https://github.com/DamianoTobasco/sync-socials-agent/tree/main/plugins/claude-sync-socials)
in the public [Sync Socials Agent repository](https://github.com/DamianoTobasco/sync-socials-agent).
The repository's root agent-neutral skill and API-key setup are separate from
this Claude OAuth bundle. The directory listing is linked above; publishing
source and installing the plugin do not complete its authentication setup.

To reproduce the six-file ZIP from the repository root, run:

```bash
python3 scripts/build-claude-plugin.py /tmp/sync-socials-claude.zip
```

The builder checks the manifest, credential-free connector declaration, and skill
tool names, then prints the archive SHA-256. File order, timestamps, and permissions
are fixed, so the same source produces the same bytes. This structural check does
not replace the directory's validation or hosted connection tests.

## License and support

MIT, copyright 2026 Damiano Tobasco. See [LICENSE](LICENSE).

Product: [Sync Socials](https://sync-socials.com). Documentation:
[Claude setup guide](https://sync-socials.com/claude.html). Support:
[contactsyncsocials@gmail.com](mailto:contactsyncsocials@gmail.com).
