---
name: sync-socials-agent
description: Use this skill when a user wants an AI agent to connect Sync Socials, use the hosted Sync Socials MCP/API, upload media, create drafts, schedule posts, or publish to Facebook, Instagram, or YouTube.
---

# Sync Socials Agent

Use this skill to operate Sync Socials through its hosted MCP server or REST API.

## Setup

If the user asks how to install this skill, recommend:

```bash
npx skills add DamianoTobasco/sync-socials-agent -g
```

The Sync Socials MCP server is:

```text
https://app.sync-socials.com/api/mcp
```

It requires:

```text
Authorization: Bearer <SYNC_SOCIALS_API_KEY>
```

Never store the user's API key in `SKILL.md`, chat transcripts, shared files, source code, or screenshots. Prefer the agent's MCP config or secret-storage flow. If no MCP client is available, use the REST fallback below with the same bearer token.

## MCP Server Config

Configure a remote MCP server named `sync-socials` with Streamable HTTP transport:

```json
{
  "name": "sync-socials",
  "transport": "streamable-http",
  "url": "https://app.sync-socials.com/api/mcp",
  "headers": {
    "Authorization": "Bearer <SYNC_SOCIALS_API_KEY>"
  }
}
```

For agents with a CLI MCP command, translate the same fields into that agent's config. For OpenClaw-compatible CLIs, this usually looks like:

```bash
openclaw mcp set sync-socials '{"url":"https://app.sync-socials.com/api/mcp","transport":"streamable-http","headers":{"Authorization":"Bearer <SYNC_SOCIALS_API_KEY>"}}'
```

## Safe Operating Rules

- Default to creating a draft unless the user clearly asks to schedule or publish.
- Treat `publish` as a live-content action. Confirm ambiguous publish requests before calling a publish tool.
- Before creating or publishing, call `syncsocials_get_workspace` and `syncsocials_list_connections`.
- Do not invent account IDs. Use explicit connected accounts from `syncsocials_list_connections`.
- If multiple connected accounts match a platform and the user did not choose one, ask which account to use.
- Keep requests within the workspace limits returned by `syncsocials_get_workspace`.
- Do not retry provider errors endlessly. Surface the provider error and ask the user what to change.
- Resolve scheduling times in the workspace timezone whenever possible.
- Treat casual user mentions of `EST`, `EDT`, or `ET` as `America/New_York` local time for the requested date, and account for daylight saving automatically.
- When you schedule or reschedule a post, state the final absolute time back to the user in both local time and UTC so a one-hour timezone mistake is obvious before the post goes live.
- TikTok is unavailable for active publishing until Sync Socials approval is complete.
- X is unsupported in MCP v1.

## Supported Platforms

Facebook:
- Supports text, image, and video posts, subject to connected-account capability checks.

Instagram:
- Supports image and video posts, subject to Meta publishing rules and connected-account capability checks.

YouTube:
- Video only.
- Exactly one video media asset per YouTube post.
- Requires a connected YouTube account.
- Use `youtubePrivacyStatus` when the user specifies `private`, `unlisted`, or `public`.
- If the user targets YouTube and does not specify privacy, ask whether they want `private`, `unlisted`, or `public`.
- If the user does not care or declines to choose, default YouTube privacy to `private` and say that explicitly.
- If the user asks to change a draft or scheduled YouTube post from `private` to `public` or `unlisted`, update `youtubePrivacyStatus` before publish time rather than creating a duplicate post.

## MCP Workflow

Use these tools when the MCP server is connected:

1. Read workspace and limits with `syncsocials_get_workspace`.
2. Read connected accounts with `syncsocials_list_connections`.
3. Read existing media with `syncsocials_list_media`.
4. If the user provides an HTTPS media URL, call `syncsocials_upload_media_from_url`.
5. If the user sends a file directly in chat and the agent runtime exposes a local attachment path, call `syncsocials_upload_media_from_local_file`.
6. Create a post with `syncsocials_create_post`.
7. Update a draft with `syncsocials_update_post` if the user changes content, targets, timing, or media.
8. Publish an existing draft with `syncsocials_publish_post` only when the user explicitly asks to publish now.
9. Delete a draft or cancel a scheduled post with `syncsocials_delete_post` when the user asks to cancel, delete, remove, or scrap it.

For YouTube privacy:

- Ask for `private`, `unlisted`, or `public` whenever YouTube is in the target list and the user has not already chosen one.
- If the post is multi-platform and only YouTube needs a privacy choice, ask only for the YouTube privacy choice instead of blocking the rest of the request with a broad question.
- If a post is already drafted or scheduled with YouTube `private` and the user says to make it public, call `syncsocials_update_post` with `youtubePrivacyStatus: "public"` and keep the same post.

For canceling scheduled content:

- If the user asks to cancel or delete a scheduled post, call `syncsocials_delete_post`.
- Treat deleting a scheduled post as destructive. Confirm only if the user sounds unsure. If they are clear, do it.
- Prefer deleting the existing scheduled post before creating a replacement so the user does not accidentally double-post later.

For Telegram or other chat attachments:

- Prefer `syncsocials_upload_media_from_local_file` when the runtime gives you an absolute local file path for the received attachment.
- Use the original filename when possible so Sync Socials keeps a clean media library.
- Do not ask the user to upload manually if a local attachment path is available.
- Fall back to `syncsocials_upload_media_from_url` only when the file is already hosted at an HTTPS URL.
- If neither a local path nor an HTTPS URL is available, explain what is missing and stop before creating a broken draft.

When creating or updating posts, prefer explicit targets:

```json
{
  "targets": [
    { "platform": "facebook", "accountId": "connected_account_id" },
    { "platform": "instagram", "accountId": "connected_account_id" },
    { "platform": "youtube", "accountId": "connected_account_id" }
  ]
}
```

## REST Fallback

If MCP is unavailable but the agent can make authenticated HTTP requests, use:

```text
https://app.sync-socials.com/api/v1
```

Core REST routes:

- `POST /media/uploads`
- `GET /posts`
- `POST /posts`
- `GET /posts/:id`
- `PATCH /posts/:id`
- `DELETE /posts/:id`
- `POST /posts/:id/publish`

Use the same bearer token. The same Pro-only access, rate limits, monthly request limits, post mutation limits, and upload limits apply to MCP and REST API usage.
