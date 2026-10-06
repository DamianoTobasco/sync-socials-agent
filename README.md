# Sync Socials Agent

**Let your AI agent run your social media.** Sync Socials is a hosted MCP server that lets Claude Code, OpenClaw, Codex and any MCP compatible agent generate content, upload media, create drafts, schedule posts and publish to TikTok, Instagram, Facebook and YouTube.

[Website](https://sync-socials.com) · [For AI agents](https://sync-socials.com/ai-social-media-agent.html) · [App](https://app.sync-socials.com)

For Claude apps and Cowork, use the [Claude plugin](plugins/claude-sync-socials/README.md)
and its hosted OAuth connection. The API-key setup below is for agent clients.

---

## Install

```bash
npx skills add DamianoTobasco/sync-socials-agent -g
```

Works with any agent that supports the open Agent Skills format.

## Connect the MCP server

The server is remote, so there is nothing to run locally.

| | |
|---|---|
| **Endpoint** | `https://app.sync-socials.com/api/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | `Authorization: Bearer <SYNC_SOCIALS_API_KEY>` |

Generate an API key from your workspace settings at [app.sync-socials.com](https://app.sync-socials.com). Requires a Sync Socials plan; a free 7 day trial is available.

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

For OpenClaw compatible CLIs:

```bash
openclaw mcp set sync-socials '{"url":"https://app.sync-socials.com/api/mcp","transport":"streamable-http","headers":{"Authorization":"Bearer <SYNC_SOCIALS_API_KEY>"}}'
```

## Tools

| Tool | What it does |
|---|---|
| `syncsocials_get_workspace` | Read workspace settings, timezone and plan limits |
| `syncsocials_list_connections` | List connected social accounts and their IDs |
| `syncsocials_list_media` | Browse the media library |
| `syncsocials_upload_media_from_url` | Upload media from an HTTPS URL |
| `syncsocials_upload_media_from_local_file` | Upload media from a local file path |
| `syncsocials_create_content_draft` | Save an untargeted content concept for later |
| `syncsocials_get_brand_profile` | Read saved business profiles |
| `syncsocials_generate_viral_concepts` | Generate content concepts from a brand brief |
| `syncsocials_produce_viral_video` | Produce a short form video from a concept |
| `syncsocials_create_post` | Create a draft or scheduled post with platform targets |
| `syncsocials_get_post` | Read a single post |
| `syncsocials_list_posts` | List drafts, scheduled and published posts |
| `syncsocials_update_post` | Edit content, targets, timing or media |
| `syncsocials_publish_post` | Publish an existing draft now |
| `syncsocials_delete_post` | Delete a draft or cancel a scheduled post |

## Example prompts

Once connected, talk to your agent normally:

- Post this Reel to TikTok, Instagram, Facebook and YouTube Shorts at 6pm.
- Queue five posts from the drafts folder across this week at 9am.
- Generate a month of content from sync-socials.com and schedule the best twelve.
- What is scheduled for the rest of the week? Move Friday's post to Saturday morning.

## Platforms

| Platform | Support |
|---|---|
| TikTok | Direct post and scheduling |
| Instagram | Image and video posts to a business or creator account linked to a Facebook Page |
| Facebook | Text, image and video posts to Pages; personal profiles are unsupported |
| YouTube | Video only, exactly one video asset per post, privacy control |
| LinkedIn | Text, image and video posts to personal profiles |
| Telegram, Discord, Slack | Posts to connected chat destinations, within their media limits |
| X / Twitter | Not supported in MCP v1 |

New and existing customers can connect Facebook Pages and linked Instagram
professional accounts after Meta approval. Each customer must grant publishing
access and select the intended accounts in Sync Socials Connections.

## Safety

- The skill defaults to creating **drafts**. It only schedules or publishes when you clearly ask.
- Access is scoped to an API key you generate and can revoke at any time.
- Social accounts connect through each platform's official OAuth login. Sync Socials never sees your passwords.
- Never commit your API key. Store it in your agent's MCP config or secret storage.

## REST fallback

If MCP is unavailable, the same operations are available over REST at `https://app.sync-socials.com/api/v1` using the same bearer token:

```text
POST   /media/uploads
GET    /posts
POST   /posts
GET    /posts/:id
PATCH  /posts/:id
DELETE /posts/:id
POST   /posts/:id/publish
```

The same plan access, rate limits and usage limits apply to both MCP and REST.

## License

MIT. See [LICENSE](LICENSE).
