# Sync Socials Agent Skill

Install the Sync Socials agent skill for agents that support the open Agent Skills format:

```bash
npx skills add DamianoTobasco/sync-socials-agent -g
```

The skill teaches compatible agents how to generate content from a brand brief, save reviewable concepts, and use the hosted Sync Socials MCP server or REST API for publishing workflows.

## MCP Endpoint

```text
https://app.sync-socials.com/api/mcp
```

Use a Sync Socials Growth API key as a bearer token:

```text
Authorization: Bearer <SYNC_SOCIALS_API_KEY>
```

## Notes

- Facebook, Instagram, and YouTube are supported.
- Agents can save generated concepts as untargeted drafts before media or destination accounts are selected.
- YouTube posts must use exactly one video asset.
- TikTok is unavailable for active publishing until Sync Socials approval is complete.
- API access requires a paid plan and counts against the same usage limits as the Sync Socials REST API.
