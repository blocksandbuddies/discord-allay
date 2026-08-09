# Security Policy

## Supported versions

Only the latest commit on `main` is supported. Fixes are not backported.

## Reporting a vulnerability

**Do not open a public issue.**

Report privately through either:

- [GitHub private vulnerability reporting](https://github.com/blocksandbuddies/discord-allay/security/advisories/new)
- Email to <security@blocksandbuddies.com>

Please include:

- A description of the issue and its impact
- Steps to reproduce it
- The affected version or commit

## What to expect

- We aim to acknowledge reports within 72 hours.
- We will confirm the issue and let you know our assessment.
- We will tell you when a fix ships, and credit you unless you prefer otherwise.

Please give us a reasonable chance to fix the issue before disclosing it
publicly.

## Scope

In scope: this repository's source code, dependencies, and the bot's handling of
tokens, permissions, and user input.

Out of scope: vulnerabilities in Discord itself (report those to
[Discord](https://discord.com/security)), and issues that require an already
compromised host or a bot token you were legitimately given.

## Bot tokens

If you believe the bot's token has leaked, email <security@blocksandbuddies.com>
immediately. Reset the token in the
[Discord developer portal](https://discord.com/developers/applications) if you
have access — this invalidates the leaked one right away.

Never commit a token. `.env` is gitignored for this reason.
