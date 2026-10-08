# Sync Socials for Cursor and Grok Bot

Manage your social content from your agent: save drafts, import existing media,
check the queue, edit posts, and schedule or publish to connected accounts.
This package uses the Cursor plugin format shared by the Cursor marketplace and
Grok Bot's plugin interface. Public listing requires Cursor review; this source
package alone is not a marketplace approval.

## Connect your workspace

1. Create or sign in to your [Sync Socials workspace](https://app.sync-socials.com).
   API access requires an eligible plan or trial and is subject to its quotas.
2. Use your workspace API key from Sync Socials settings. Growth supports one
   active key; replacing it disconnects other clients using that key.
3. After installing the plugin, open **Plugins → Configure** in Cursor's
   dashboard and set `SYNC_SOCIALS_API_KEY`. For a team installation, an admin
   may need to configure or approve it. Do not paste the key into a Bot chat.
4. Ask the agent to read your Sync Socials workspace and confirm its name.

The key grants read/write access across the selected workspace, including its
publishing tools. It is not limited to drafts and has no automatic expiration.
Use a separate workspace for testing and revoke the key in Sync Socials to
disconnect. Each customer uses their own key; no credentials ship in this repo.
The MCP endpoint is `https://app.sync-socials.com/api/mcp` (Streamable HTTP).

## Try your first draft

> Read my Sync Socials workspace, then save an untargeted draft titled
> "Getting started" with the caption "Our first post is coming soon."
> Return its draft ID and status. Do not schedule or publish it.

No social account or AI provider is required for this draft workflow. Connect
social accounts inside Sync Socials when you are ready to publish. Supported
destinations include TikTok, Facebook Pages, linked Instagram professional
accounts, YouTube, LinkedIn personal profiles, Telegram, Discord, and Slack.
X/Twitter publishing is not supported by MCP v1.

Other prompts:

- Show my scheduled posts for this week.
- Save three launch captions as drafts for review.
- Move the selected scheduled post to Friday at 9am in my workspace timezone.

AI concept generation through Sync Socials needs a configured workspace AI
provider and consumes its allowance. Video assembly uses existing footage,
text, and music. Local files on a user's or Bot's computer must be uploaded
through the media library or made available as a usable HTTPS media URL.

## Development and review

The repository's `.cursor-plugin/marketplace.json` points to this package.
The manifest declares the API-key variable used by `mcp.json`; public source
contains only its placeholder. There are no install scripts, hooks, background
routines, or bundled executables. Follow the
[Cursor local plugin instructions](https://cursor.com/docs/plugins) to test a
copy before marketplace installation. A schema check does not substitute for
an authenticated Cursor or Grok Bot runtime test.

## Support and policies

- [Setup and service information](https://sync-socials.com/ai-social-media-agent.html)
- [Privacy](https://app.sync-socials.com/privacy) · [Terms](https://app.sync-socials.com/terms)
- Support: contactsyncsocials@gmail.com
- Maintained by EvolveAI LLC. Plugin source: MIT; hosted service access has its
  own plan and usage terms.
