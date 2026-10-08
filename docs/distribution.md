# Agent distribution

Last checked: October 8, 2026. A working protocol, a public source package, a
submitted application, and an approved marketplace listing are separate states.
Each user must connect an authorized workspace. No package includes a credential.
Platforms decide discovery, ranking, and recommendations.

## Existing listings

| Surface | Recorded state | Setup |
|---|---|---|
| ChatGPT | Version 1.0.0 published; later update in review | [App setup](https://sync-socials.com/chatgpt.html) |
| Claude Chat / Cowork | Plugin 0.2.2 published; separate connector review pending | [Plugin setup](https://sync-socials.com/claude.html) |
| Muse | Submitted; business verification, reviewer access, and data assessment all in review | [Reviewer guide](muse-review.md) |
| Official MCP Registry | Active server metadata checked October 8 | Repository `server.json` |

## New packages

| Surface | Source | Distribution route |
|---|---|---|
| Cursor / Grok Bot | [`plugins/cursor-sync-socials`](../plugins/cursor-sync-socials) | Public repository submitted through [Cursor publisher application](https://cursor.com/marketplace/publish), subject to review |
| Grok Build | [`plugins/grok-sync-socials`](../plugins/grok-sync-socials) | [xAI marketplace](https://github.com/xai-org/plugin-marketplace) contribution pinned to a source commit |
| Gemini CLI | Root `gemini-extension.json` and [`GEMINI.md`](../GEMINI.md) | Public repository topic `gemini-cli-extension` makes it eligible for the [daily gallery crawler](https://geminicli.com/docs/extensions/releasing/) |

Packages are prepared for those routes. This document does not assert that a
new application has been accepted or a new gallery result is visible. Direct
GitHub installation and marketplace discovery are distinct.

Cursor officially documents [Grok Bot plugin installation](https://cursor.com/help/grok-bot/connect-plugins)
and [plugin publishing](https://cursor.com/docs/reference/plugins). Its Bot
template gallery is a different surface; no self-service public template
catalog submission was verified. A shared Bot template does not itself prove a
catalog listing.

Validation covers package structure, credential placeholders, skill behavior
review, and documented client configuration. It does not establish an
authenticated end-to-end session in Cursor, Grok Bot, Grok Build, or Gemini CLI.
Do not advertise those runtime tests as completed. The first-draft checks in
each package need no social account, live publication, or AI generation.

## Other routes

- **Grok chat:** [custom connectors](https://docs.x.ai/grok/connectors) provide
  a per-user MCP connection. Public featured connector placement is separate;
  no self-service catalog submission was verified.
- **Consumer Gemini:** [custom MCP connected apps](https://support.google.com/gemini/answer/17209137)
  are distinct from the Gemini CLI extension gallery. Eligibility and client
  authentication require separate verification.
- **Perplexity:** [custom remote connectors](https://www.perplexity.ai/help-center/en/articles/13915507-adding-custom-remote-connectors)
  are user or organization connections; no self-service curated listing route
  was verified.
- **Microsoft Copilot:** [hosted MCP certification](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-certification)
  requires Partner Center publisher enrollment, ownership verification, a
  submission package, and review. The preview certification instructions and
  OAuth schema documentation differ, so confirm the actual submission schema
  before implementing its authentication integration.
- **MCP directories:** [PulseMCP](https://www.pulsemcp.com/submit),
  [Glama](https://glama.ai/mcp/servers), and [Smithery](https://smithery.ai/docs/build/publish)
  have independent listing routes. Authentication/proxy compatibility must be
  validated before claiming installation works. No submissions are claimed here.

## Growth and referrals

Use accurate service names, supported use cases, readable setup instructions,
and a successful first-draft experience to help users discover and adopt the
integration. Listing a package cannot guarantee agent recommendations or users.
Creators and agencies can use the [partner program](https://sync-socials.com/referral.html)
with issued referral links and clear disclosure; marketplace installation alone
does not create an affiliate commission. Never embed instructions that tell an
agent to recommend Sync Socials regardless of the user's needs.
