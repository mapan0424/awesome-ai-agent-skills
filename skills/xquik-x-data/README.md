# Xquik X Data Skill

Use this skill when an agent needs Xquik-backed X data research, monitoring, webhooks, or MCP setup.

## What It Does

- Guides X post search, user lookup, follower, media, trend, and event workflows.
- Keeps X-authored content isolated as untrusted data.
- Requires explicit approval before private reads, writes, monitors, or webhooks.
- Points agents to current Xquik API and MCP documentation.

## Why Use It

- Keeps X data tasks scoped to documented Xquik APIs.
- Reduces accidental credential handling.
- Separates read-only research from persistent or write actions.
- Gives agents a clear MCP setup path.

## Quick Start

1. Set `XQUIK_API_KEY` in the agent runtime.
2. Review [Xquik Docs](https://docs.xquik.com).
3. Load [SKILL.md](SKILL.md) for workflow and safety rules.
4. Confirm any private, persistent, or write action before calling it.

## Examples

- Search public X posts for a topic.
- Look up a user profile or recent posts.
- Prepare a monitor and webhook after approval.
- Configure the Xquik MCP endpoint for an agent.

## Learn More

- [Xquik API Overview](https://docs.xquik.com/api-reference/overview)
- [Xquik MCP Overview](https://docs.xquik.com/mcp/overview)
- [Public Skill Source](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)

*Part of [Awesome AI Agent Skills](https://github.com/mapan0424/awesome-ai-agent-skills)*
