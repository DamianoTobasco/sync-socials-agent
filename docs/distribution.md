# Agent distribution

Last checked: October 8, 2026. A working protocol, a public source package, a
submitted application, and an approved marketplace listing are separate states.
Each user must connect an authorized workspace. No package includes a credential.
Platforms decide discovery, ranking, and recommendations.

## Existing listings

| Surface | Recorded state | Setup |
|---|---|---|
| ChatGPT | Version 1.0.0 published; 1.0.1 in review; 1.0.2 ZIP prepared and held | [App setup](https://sync-socials.com/chatgpt.html) |
| Claude Chat / Cowork | Plugin 0.2.2 published; separate connector review pending | [Plugin setup](https://sync-socials.com/claude.html) |
| Muse | Submitted; business verification, reviewer access, and data assessment all in review | [Reviewer guide](muse-review.md) |
| Official MCP Registry | Version 1.0.1 published at 19:35 UTC October 8; independently verified active and latest | [Public metadata](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.DamianoTobasco%2Fsync-socials-agent/versions/1.0.1) |
| Glama | Existing public directory listing verified October 8; displayed repository content is older, and hosted deployment is not enabled | [Listing](https://glama.ai/mcp/servers/DamianoTobasco/sync-socials-agent) |

## New packages

| Surface | Source | Distribution route |
|---|---|---|
| Cursor / Grok Bot | [`plugins/cursor-sync-socials`](../plugins/cursor-sync-socials) | Publisher application submitted October 8; portal confirmed receipt, pending review |
| Grok Build | [`plugins/grok-sync-socials`](../plugins/grok-sync-socials) | [xAI marketplace PR #1309](https://github.com/xai-org/plugin-marketplace/pull/1309) opened October 8, pinned to the public source commit; review pending |
| Gemini CLI | Root `gemini-extension.json` 1.0.1 and [`GEMINI.md`](../GEMINI.md) | X guidance published to public source October 8; topic `gemini-cli-extension` enabled; awaiting [daily gallery crawler](https://geminicli.com/docs/extensions/releasing/) validation/indexing |

The initial client packages were published in commit
`bb68a8803a97cac5f4ba94fe7b7cba6d200784ca`. The generic agent skill, Gemini 1.0.1,
and Registry source metadata update were published in commit
[`a4c9354d83e87aaddf846c381bed339020111149`](https://github.com/DamianoTobasco/sync-socials-agent/commit/a4c9354d83e87aaddf846c381bed339020111149).
That update left the tracked Claude, Cursor, Grok Build, and Muse review packages
unchanged. No new marketplace approval or visible Gemini gallery result is
claimed. Direct GitHub installation and marketplace discovery are distinct.

Cursor officially documents [Grok Bot plugin installation](https://cursor.com/help/grok-bot/connect-plugins)
and [plugin publishing](https://cursor.com/docs/reference/plugins). Its Bot
template gallery is a different surface; no self-service public template
catalog submission was verified. A shared Bot template does not itself prove a
catalog listing.

Validation passed Cursor's official template validator, xAI's marketplace
component/catalog checks, and Gemini CLI 0.63.0's extension validation plus its
versioned MCP settings schema. Skill frontmatter and independent simulated
workflows covered drafts, publishing, local media, missing auth, timed-out
writes, untrusted retrieved content, and the then-unsupported X/Twitter destination.
Those earlier simulations do not validate the new X instructions.
These checks do not establish an
authenticated end-to-end session in Cursor, Grok Bot, Grok Build, or Gemini CLI.
Do not advertise those runtime tests as completed. The first-draft checks in
each package need no social account, live publication, or AI generation.

## X update: source versions and publication status

The hosted MCP supports X through its existing endpoint and post tools. Clients
must refresh tool discovery and read `syncsocials_get_workspace` (`xUsage` and
`postingCapabilities`) and `syncsocials_list_connections` before using it. X
requires active paid Growth; trials and unpaid review access remain excluded.
Server availability does not update an installed skill or marketplace description.

Generic skill/Gemini source and MCP Registry metadata updates are published.
The Registry's version-specific and latest public endpoints both report 1.0.1
as active and latest, with publication timestamp `2026-10-08T19:35:08.694501Z`.
Claude, ChatGPT/OpenAI, Cursor/Grok Bot, Grok Build, and Muse submission updates
remain on hold while existing reviews continue. Their prepared candidates below are local,
unpublished packages; check each published manifest for available source versions.

| Package | Version / state | Distribution status or next step |
|---|---|---|
| Claude Chat / Cowork | 0.2.3 prepared; held | Upload/update the plugin package, pass the directory scan, and publish. Recorded published version remains 0.2.2. |
| Cursor / Grok Bot | 0.1.1 prepared; held | Publish source and update the pending publisher application through Cursor's portal if it pins or caches the prior revision; verify which revision is reviewed. No approval claimed. |
| Grok Build | 0.1.1 prepared; held | Update marketplace PR #1309's full source commit pin after source publication; xAI review is still required. |
| Gemini CLI | 1.0.1 published source | Installed users run `gemini extensions update sync-socials-agent` and restart. The gallery uses automatic crawling and validation, with no separate form resubmission; gallery inclusion is not yet verified. |
| Official MCP Registry metadata | 1.0.1 published and verified | Public metadata includes X on paid Growth and retains the canonical endpoint and authentication. This is separate from the runtime's protocol version. |
| Agent-neutral skill / Codex and compatible clients | Published in `a4c9354` | Update the installed skill and start a new session so the old unsupported-X instruction is replaced. Existing installations do not automatically inherit source edits. |
| ChatGPT / OpenAI | 1.0.0 published; 1.0.1 in review; 1.0.2 ZIP prepared and held | Existing MCP tools expose server changes after discovery. Keep the current review intact; submit the prepared skill/listing update separately after approval. This repository does not change the published ChatGPT package. |
| Muse | Existing submission | The service changes dynamically; provide the revised reviewer documentation/schema snapshot through the existing review process. Unpaid review credentials still cannot publish to X. |

Glama and other directories may cache repository descriptions; verify their
refresh separately. Do not call a source commit, working MCP response, or package
validation an approved listing. The [Cursor publishing reference](https://cursor.com/docs/reference/plugins),
[xAI contribution guide](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md),
and [Gemini release guide](https://geminicli.com/docs/extensions/releasing/)
describe their separate distribution routes.

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
  validated before claiming installation works. No new submissions are claimed
  here. Glama already lists the repository. Root `glama.json` identifies the
  maintainer; [Glama's Claim ownership flow](https://glama.ai/blog/2025-07-08-what-is-glamajson)
  must still run before claiming management access or a refreshed listing.

## Growth and referrals

Use accurate service names, supported use cases, readable setup instructions,
and a successful first-draft experience to help users discover and adopt the
integration. Listing a package cannot guarantee agent recommendations or users.
Creators and agencies can use the [partner program](https://sync-socials.com/referral.html)
with issued referral links and clear disclosure; marketplace installation alone
does not create an affiliate commission. Never embed instructions that tell an
agent to recommend Sync Socials regardless of the user's needs.
