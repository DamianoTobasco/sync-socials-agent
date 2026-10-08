# Sync Socials for Gemini CLI

Use Sync Socials from Gemini CLI to prepare drafts, browse media, and schedule
or publish to social accounts you have connected in Sync Socials. The extension
connects to `https://app.sync-socials.com/api/mcp` with Streamable HTTP.

This package is for **Gemini CLI**. It is separate from custom connected apps
and the app catalog in the consumer Gemini web and mobile apps. A repository
or gallery listing does not establish Google endorsement or automatic access
for other users.

## Install and configure

1. Install a current [Gemini CLI](https://geminicli.com/docs/get-started/installation/)
   and complete its normal Google authentication setup.
2. Open your workspace settings at [app.sync-socials.com](https://app.sync-socials.com)
   and use your workspace API key, or create one if needed. Your workspace needs
   agent/API access. Growth supports one active key; replacing it can disconnect
   other clients using that key.
3. Install the extension from the public repository:

   ```bash
   gemini extensions install https://github.com/DamianoTobasco/sync-socials-agent
   ```

4. Review the extension's requested access. At the **Sync Socials API key** prompt,
   enter your key without a `Bearer` prefix. Do not paste it into an AI chat or
   put it in the install command.
5. Restart your Gemini CLI session. Use `/mcp` to inspect the `sync-socials`
   connection and `/extensions list` to check the extension.

The manifest declares `SYNC_SOCIALS_API_KEY` as a sensitive setting. Gemini CLI
uses its sensitive-settings storage, documented as the system keychain, and
substitutes the value into the Authorization header. No credential is included
in this repository. If secure credential storage fails, resolve that setup
problem before entering the key; do not save it in the repository as a workaround.

If you skipped configuration or need to replace the key, use the interactive
configuration command:

```bash
gemini extensions config sync-socials-agent
```

Installing the extension does not connect social accounts. Connect those in
Sync Socials when you are ready to target a platform. Each Gemini CLI user
supplies a key for their own authorized workspace.

The API key grants read/write access across its workspace and has no automatic
expiry. Store it securely. Revoking or replacing a shared key affects every
client using it; update those clients when you rotate the key.

## First check and first draft

Start with a read-only check:

> Use Sync Socials to read my workspace and list my connected social accounts.
> Report the timezone and available publishing destinations. Do not change anything.

Then ask for a small draft:

> Create an untargeted Sync Socials draft titled "Getting started" with the
> caption "Our first post is coming soon." Return its draft ID. Do not schedule
> or publish it.

An untargeted draft needs no social connection or workspace AI provider. Hosted
concept generation requires a configured workspace AI provider and uses its
allowance. Video assembly uses existing footage. Available tools and capabilities
are determined by the connected workspace and server.

For media, use an existing workspace asset, an authorized HTTPS URL, or the
upload screen in Sync Socials. The hosted server cannot read files on your
computer; this extension excludes its server-local file import tool.

## Troubleshooting and removal

- If authentication fails, re-enter your workspace key through `gemini extensions config
  sync-socials-agent`. Confirm that it belongs to the intended workspace and
  has not been revoked. Never print the key or credential store.
- If `sync-socials` is already defined in your Gemini `settings.json`, that
  configuration takes precedence over the extension. Check for duplicate
  entries before troubleshooting the extension's credentials.
- If a social connection is missing or expired, reconnect it in Sync Socials.
- If a write times out, inspect existing content before repeating the write.

Update or remove the extension with:

```bash
gemini extensions update sync-socials-agent
gemini extensions uninstall sync-socials-agent
```

Uninstalling the extension does not revoke its Sync Socials API key or cancel
scheduled posts. Revoke the key in Sync Socials workspace settings when its
access should end, accounting for other clients sharing it. Manage scheduled
posts separately in the app.

## Maintainer validation and gallery publication

From the repository root, run:

```bash
gemini extensions validate .
```

This validates the extension package without running a model prompt. It does
not establish a successful authenticated connection or end-to-end publishing.
Test those separately with a dedicated test workspace before claiming them.

For the Gemini CLI extension gallery:

1. Publish the extension in this public GitHub repository with
   `gemini-extension.json` at the repository root.
2. Add the GitHub topic `gemini-cli-extension` to the repository's About section.
3. Check the [gallery](https://geminicli.com/extensions/) after its daily crawl.
   The extension appears only if it passes the gallery's validation.

Google documents automatic discovery; no issue or email submission is required.
Installing directly from GitHub and appearing in the gallery are separate steps.

Official references: [extension format and sensitive settings](https://geminicli.com/docs/extensions/reference/),
[Streamable HTTP configuration](https://geminicli.com/docs/tools/mcp-server/),
[gallery publication](https://geminicli.com/docs/extensions/releasing/).
