# Sync Socials Muse connector review

Sync Socials was submitted to Muse on September 28, 2026 and entered review on
October 3. It is not yet an approved public Muse connector. This guide describes
the isolated reviewer connection, tool effects and validation steps.

## Connection and access

- Endpoint: `https://app.sync-socials.com/api/mcp`
- Transport: Streamable HTTP.
- Reviewer authentication: the dedicated API key supplied privately in Muse's
  credential form, sent as `Authorization: Bearer <reviewer-api-key>`.
- The key permits reads and writes within the separate Muse review workspace.
  It is not a read-only or per-tool-scoped credential. No production/customer
  credentials or data should be supplied to reviewers.
- Unpaid review access is temporary and revocable. Its end time is supplied with
  the private reviewer credential. It does not create a paid subscription.
  API keys have no native expiry field; the server enforces the review access
  deadline separately.
- Server-local file import is unavailable to this reviewer workspace. Import
  HTTPS media URLs instead. An agent's local file path is not a remote upload.
- Customer OAuth onboarding for Muse remains pending its confirmed callback and
  registration requirements. Do not infer Muse OAuth compatibility from a
  successful API-key test or another assistant's OAuth integration.

Current limits are 30 API requests per minute, 5,000 counted API requests per
month, 500 post mutations per month and 25 GiB of uploads per month, shared within
the workspace. Use `syncsocials_get_workspace` for current limits and usage.
Production/video allowances are separate. Review access preserves ordinary
workspace quotas and plan entitlements.

## Tool review reference

The connection exposes 14 tools. The live `tools/list` response is authoritative
for required fields, enums, descriptions and MCP annotations. These proposed
review classifications are conservative; Muse makes its own classification and
approval decisions. A tool that can publish remains sensitive even when a
particular call only saves a draft.

The [sanitized tool-definition snapshot](muse-tools.json), captured October 8,
2026, contains the reviewer-visible schemas and annotations without credentials,
workspace content or dynamic defaults. Fetch `tools/list` for the current schema.

| Tool | Classification | Inputs and returned outcome |
| --- | --- | --- |
| `syncsocials_get_workspace` | Read | No inputs; workspace, capabilities, limits and usage. |
| `syncsocials_list_connections` | Read | Optional platform; connected account IDs and publishing capabilities, excluding social secrets. |
| `syncsocials_list_media` | Read | Optional type and limit; reusable workspace media assets. |
| `syncsocials_list_posts` | Read | Optional status and limit; workspace posts and their state. |
| `syncsocials_get_post` | Read | Post ID; the post, processing state and available media previews. |
| `syncsocials_get_brand_profile` | Read | No inputs; saved workspace brand profile. |
| `syncsocials_upload_media_from_url` | Write | HTTPS URL and optional name; downloads media and returns asset IDs. Uses storage/upload allowance. |
| `syncsocials_create_content_draft` | Write | Title, optional caption/tags; saves an untargeted draft. Never schedules or publishes. |
| `syncsocials_generate_viral_concepts` | Write | Business/profile and concept options; may save brand information and returns generated concepts. Uses a configured AI provider. |
| `syncsocials_create_post` | Sensitive write | Content, media, destinations and draft/schedule/publish action; returns the saved post and delivery information. Optional generation requires its configured provider. |
| `syncsocials_update_post` | Sensitive write | Existing post ID and changed fields; modifies that post, including approved timing/action changes. |
| `syncsocials_publish_post` | Sensitive write | Existing post ID; requests immediate delivery. Inspect returned state before claiming publication. |
| `syncsocials_delete_post` | Sensitive write | Existing post ID; deletes a draft or cancels a scheduled post. Does not retract already-published social content. |
| `syncsocials_produce_viral_video` | Sensitive write | Approved concept, production options and optional selected destinations; assembles existing footage/text/music and saves or schedules the result. Uses production allowance. |

Tool successes include human-readable text and `structuredContent`; a JSON text
copy supports clients that do not expose structured content. Check tool errors
and transport failures before interpreting a response as success. Media preview
links expire; `get_post` supplies fresh links. Rendering may return
`processing: true`; retrieve the same post until processing completes.

## Reviewer workflow

1. Read workspace and connections. Confirm the dedicated review workspace and
   the expected test data. The initial workspace has no connected destinations.
2. List sample drafts, media and the saved brand profile. Retrieve one draft by ID.
3. Save an untargeted draft titled `Muse review sample` with a harmless sample
   caption. Retrieve it and update that same draft's caption.
4. Import an authorized HTTPS image into the review media library. Confirm the
   returned asset exists and no post was published.
5. Delete only the disposable draft created in step 3. Confirm it is no longer
   returned. Preserve the original samples for later reviewers.
6. Test AI concepts only with a configured provider and its allowance. Test video
   assembly with available existing footage, soundtracks and production allowance;
   that tool does not generate new footage or speech through an AI model. A
   missing-provider or missing-footage error is not a successful production test.
7. Scheduling and live publishing require an explicitly selected disposable test
   destination and the user's approved content, time, timezone, privacy and
   platform disclosures. Do not substitute a company/customer account. Test
   status, rescheduling and cancellation as well as publication.
8. Test revocation/reconnection with the operator so the active reviewer key is
   not unexpectedly invalidated. Expired unpaid review access must fail.

A draft test does not establish live publishing or Muse end-to-end compatibility.
Use a separate result for each exercised workflow and preserve failure details.

### Operator checks completed October 8, 2026

Live checks passed for authenticated workspace identity, 14-tool discovery,
brand retrieval, empty connections, and disposable draft creation, update,
status retrieval and deletion. Server-local import was absent from discovery,
reported unavailable in capabilities and rejected when explicitly requested.
The original three sample drafts were preserved. The review workspace started
with one fictional brand and no social accounts, media or AI providers.

These checks did not exercise HTTPS media import, AI generation, video
production, scheduling, live publishing or a Muse end-to-end session. They do
not establish approval by Muse.

## Errors and recovery

Missing/invalid/revoked credentials fail authentication. Missing plan entitlement
or expired unpaid review access denies API use. Rate and monthly limits return
quota errors; wait for the reported reset or request a legitimate limit change.
Invalid schemas, unavailable providers, missing media and unsupported destinations
must be surfaced to the user. After an uncertain mutation outcome, check existing
posts/status before retrying to avoid duplicates. A queued or scheduled post is
not proof of publication on a social platform.

## Data and support

The connection processes workspace identifiers, brand briefs, selected account
labels, user-provided posts/media, publishing settings and operational usage.
Requested generation and publishing involve the selected service providers.
Disconnecting access does not cancel schedules or remove content already shared.

[Privacy policy](https://app.sync-socials.com/privacy) ·
[Deletion instructions](https://sync-socials.com/data-deletion.html) ·
[Product terms](https://app.sync-socials.com/terms)

Support and reviewer coordination: `contactsyncsocials@gmail.com`.

[Muse connector guidelines](https://muse.ai/platform/docs) describe the platform's
review process. Approval, featuring and traffic are not guaranteed.
