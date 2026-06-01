---
name: quick-commit
description: Generate meaningful git commit messages from staged changes
version: 1.0.0
author: mapan0424
tags: [git, productivity, development]
agents: [hermes, claude, cursor, windsurf]
last_updated: 2026-06-02
---

# Quick Commit

> Automatically generate clear, conventional commit messages from your staged changes.

## When to Use

✅ **Use this skill when:**
- You've made changes and need a commit message
- You want to follow conventional commit format
- You're committing multiple related changes
- You want clear, searchable git history

❌ **Do NOT use when:**
- You need to split changes into multiple commits
- Your changes are too complex to summarize automatically

## Prerequisites

- Git repository initialized
- Changes staged with `git add`

## Quick Start

```bash
# Stage your changes
git add .

# Generate and commit
git commit -m "$(git diff --cached --stat | head -20)"
```

## Instructions

### Step 1: Analyze Staged Changes

```bash
# See what's staged
git diff --cached --stat
git diff --cached
```

### Step 2: Identify Change Type

| Type | Prefix | When to Use |
|------|--------|-------------|
| Feature | `feat:` | New functionality |
| Fix | `fix:` | Bug fixes |
| Docs | `docs:` | Documentation only |
| Style | `style:` | Formatting, no logic change |
| Refactor | `refactor:` | Code restructuring |
| Test | `test:` | Adding/fixing tests |
| Chore | `chore:` | Build, deps, config |

### Step 3: Write the Message

Format: `<type>(<scope>): <description>`

Examples:
```
feat(auth): add JWT token refresh mechanism
fix(api): handle null response from user endpoint
docs(readme): update installation instructions
refactor(utils): extract validation logic to separate module
```

### Step 4: Commit

```bash
git commit -m "feat(auth): add JWT token refresh mechanism"
```

## Pitfalls

⚠️ **Common Mistakes:**

### 1. Too vague messages

**Wrong:** `git commit -m "fix bug"`
**Right:** `git commit -m "fix(auth): prevent token expiration during long sessions"`

### 2. Committing too much

**Problem:** One commit with unrelated changes

**Solution:** Split into logical commits:
```bash
git add src/auth/
git commit -m "feat(auth): add password reset flow"

git add src/api/
git commit -m "feat(api): add password reset endpoint"
```

### 3. Wrong type prefix

**Problem:** Using `feat` for a bug fix

**Solution:** Be precise:
- New feature → `feat:`
- Fixing broken behavior → `fix:`
- Improving code structure → `refactor:`

## Verification

After committing:

- [ ] **Message is clear:** Can someone understand the change from the message alone?
  ```bash
  git log -1 --oneline
  ```

- [ ] **Scope is correct:** Does the scope match the changed files?
  ```bash
  git diff HEAD~1 --stat
  ```

- [ ] **Type is accurate:** Does the type reflect the change nature?

## Examples

### Single File Change

```bash
# Modified: src/api/users.js
git add src/api/users.js
git commit -m "fix(api): handle missing user profile gracefully"
```

### Multiple Related Files

```bash
# Modified: src/auth/login.js, src/auth/middleware.js, tests/auth.test.js
git add src/auth/ tests/auth.test.js
git commit -m "feat(auth): implement refresh token rotation"
```

### Documentation Update

```bash
# Modified: README.md, docs/api.md
git add README.md docs/
git commit -m "docs: add API authentication guide"
```

### Configuration Change

```bash
# Modified: .eslintrc.js, package.json
git add .eslintrc.js package.json
git commit -m "chore: upgrade ESLint to v9 and update rules"
```

## Advanced: Auto-Generate Message

Use git to suggest a message:

```bash
# Show changes summary
git diff --cached --stat | tail -1

# Show changed function names
git diff --cached | grep "^+" | grep -E "(function|def |class |const )" | head -5

# Suggest message based on file types
echo "Changed files:"
git diff --cached --name-only | sed 's/.*\.//' | sort | uniq -c
```

## References

- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://cbea.ms/git-commit/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)

---

*Part of [Awesome AI Agent Skills](https://github.com/mapan0424/awesome-ai-agent-skills)*
