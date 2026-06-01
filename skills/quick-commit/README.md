# Quick Commit Skill

Generate meaningful, conventional commit messages from your staged changes.

## What It Does

This skill helps you write clear, consistent git commit messages by:

1. **Analyzing** your staged changes
2. **Identifying** the type of change (feat, fix, docs, etc.)
3. **Generating** a conventional commit message
4. **Committing** with proper formatting

## Why Use It

- ✅ Consistent git history
- ✅ Easy to search and filter commits
- ✅ Works with semantic versioning
- ✅ Saves time writing messages

## Quick Start

```bash
# Stage your changes
git add .

# Use the skill to generate commit message
# (Your AI agent will apply this skill automatically)
```

## Examples

### Simple Change

```bash
# Changed: src/utils.js
git commit -m "fix(utils): handle null input in parseDate"
```

### Feature Addition

```bash
# Changed: src/auth/login.js, src/auth/middleware.js
git commit -m "feat(auth): add two-factor authentication"
```

### Documentation

```bash
# Changed: README.md
git commit -m "docs: add installation instructions for Windows"
```

## Conventional Commit Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding/fixing tests |
| `chore` | Build, deps, config |

## Learn More

- [SKILL.md](SKILL.md) - Full skill instructions
- [Conventional Commits](https://www.conventionalcommits.org/) - Official spec

---

*Part of [Awesome AI Agent Skills](https://github.com/mapan0424/awesome-ai-agent-skills)*
