---
name: social-publishing
description: Manage drafts, media, schedules, and publishing in a connected Sync Socials workspace. Use when the user asks to save social content in Sync Socials, check its queue, edit its posts, or schedule or publish to its connected accounts.
---

# Sync Socials publishing

This plugin declares the hosted Sync Socials connector, which the user must
connect and authenticate in Claude before its tools can operate. Use the
available Sync Socials MCP tools. Tool names below may have a client-added
prefix; match the `syncsocials_` name. Discover the current tool schemas before
calling them. Do not register another MCP server or construct a REST or API-key
workaround when this connector is unavailable.

## Establish the workspace

Call `syncsocials_get_workspace` to check the workspace identity, timezone,
capabilities, and allowances. For targeted drafts, schedules, or publishing, call
`syncsocials_list_connections` and use only the returned connected account IDs.
Do not infer that a destination is available from its platform name. When more
than one account matches and the user has not selected one, ask them to choose.
Use `syncsocials_list_posts` to inspect the queue or locate a requested post.

Facebook publishing targets Facebook Pages, not personal profiles. Instagram
publishing requires a business or creator account linked to a Facebook Page and
an image or video; text-only Instagram posts are unsupported. Use each platform's
own returned account ID, including when Facebook and Instagram share a linked
Page. If a destination is missing or needs reauthorization, direct the user to
Sync Socials Connections to connect or reconnect, allow publishing, and select
the correct Page or linked Instagram account. Recheck the connection before
targeting it; app approval does not replace the customer's account consent.

If the tools are absent or authentication fails, explain that a connected Sync
Socials workspace is required. In Chat or Cowork, direct the user to the plugin's
Connectors tab. This bundle supports Claude apps and Cowork; direct Claude Code
OAuth is unsupported. Use the setup guide for the supported connection flow.
Installing the plugin alone does not authenticate the workspace.
Do not claim that a directory listing or a working public sign-in flow exists
unless verified. Never request OAuth client secrets, access tokens, or social
passwords in conversation. Stop on missing access or quota errors and explain the
specific remedy returned by the service.

## Save and edit drafts

- Default every create operation to `action: "draft"`. A request to draft,
  brainstorm, or prepare content does not authorize scheduling or publication.
- For ideas without destinations or media, use
  `syncsocials_create_content_draft`. It saves an untargeted text draft.
- For content tied to selected accounts or existing assets, use
  `syncsocials_create_post` with explicit `targets` and `mediaAssetIds`.
- `title` is the internal post name; `body` is the published caption. A title-only
  request leaves `body` empty. A request to write captions authorizes putting the
  requested copy in `body`. Use `tags: []` when the user requests no hashtags;
  omitted tags can be filled automatically by the server.
- Before editing, fetch the specific post with `syncsocials_get_post`. Use
  `syncsocials_update_post` with only the fields the user asked to change.
  Preserve its media, targets, timing, and privacy choices unless changing them
  is part of the request. If a named post is ambiguous, resolve it before writing.

## Use existing media and text concepts

Use `syncsocials_list_media` for existing images or videos. Import an existing
user-provided HTTPS media URL with `syncsocials_upload_media_from_url`, then use
the returned asset ID. Hosted OAuth tools cannot read a file path on the user's
computer. If an attachment has no usable HTTPS URL or asset ID, ask the user to
upload it to the Sync Socials media library; do not invent a URL.

For Sync Socials campaign concepts, inspect `syncsocials_get_brand_profile`, then
use `syncsocials_generate_viral_concepts` when the user requests concepts. Select
the correct business if several exist. This operation creates text, can save a
brand profile, requires a configured workspace AI provider, and uses its
allowance. Show concepts for review before rendering one.

If the user requests an existing-media edit and the tool is available,
`syncsocials_produce_viral_video` assembles library clips or uploaded brand footage
with text and an existing soundtrack. Pass the approved concept object through
unchanged, choose only `library` or `remix`, and default to a draft. This connector
does not generate images, video footage, speech, or music through AI models.
Do not send media-generation prompt fields or switch authentication methods to
get around that restriction.

## Schedule, publish, and cancel

Only schedule or publish when the user explicitly requests that action. Resolve
the intended content, destination account IDs, and any required privacy,
commercial-content, or music declarations first. Do not invent consent or choose
an audience on the user's behalf. A clear request already containing these
details is sufficient; avoid asking the same question twice.

For scheduling, resolve the date and time in the workspace's IANA timezone unless
the user explicitly chooses another zone. Account for daylight saving. Clarify
an ambiguous or nonexistent local time before scheduling. Set `action: "schedule"`
and `scheduledFor` using an ISO timestamp with an explicit offset. For immediate
publication of an existing post, use `syncsocials_publish_post`.

Use `syncsocials_delete_post` only for the user's selected draft deletion or
cancellation of a scheduled post. It does not retract a post already published
on a social platform. Do not mass-delete or republish as a repair strategy.

## Verify and report

Read each mutation's result. Use `syncsocials_get_post` to verify the resulting
status and, after media processing, obtain its preview link. Queued publishing or
processing is still pending: do not call it published or ready until the returned
state confirms completion. If a write times out, inspect the queue or post before
retrying so that the action is not duplicated.

Report the post title and ID, resulting status, chosen accounts, and returned
preview or publishing link when available. For schedules, include the absolute
date and local time with its timezone, plus UTC. For failures, identify the
affected destination and the returned error without claiming the whole post
succeeded. Do not promise engagement or sales results.
