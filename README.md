# Sync Socials Agent Skill

Install the Sync Socials agent skill for agents that support the open Agent Skills format:

```bash
npx skills add DamianoTobasco/sync-socials-agent -g
```

The skill teaches compatible agents how to use the hosted Sync Socials MCP server and REST API for Facebook, Instagram, and YouTube publishing workflows.

## MCP Endpoint

```text
https://app.sync-socials.com/api/mcp
```

Use a Sync Socials Pro API key as a bearer token:

```text
Authorization: Bearer <SYNC_SOCIALS_API_KEY>
```

## Notes

- Facebook, Instagram, and YouTube are supported.
- YouTube posts must use exactly one video asset.
- TikTok is unavailable for active publishing until Sync Socials approval is complete.
- API access is Pro-only and counts against the same paid usage limits as the Sync Socials REST API.
