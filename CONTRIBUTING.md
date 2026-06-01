# 🤝 Contributing to Awesome AI Agent Skills

Thank you for your interest in contributing! This project thrives on community contributions.

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Adding a Skill](#adding-a-skill)
- [Rating a Skill](#rating-a-skill)
- [Reporting Issues](#reporting-issues)
- [Style Guide](#style-guide)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)

---

## Ways to Contribute

### 1. 📝 Add a New Skill

Share a skill you've created or discovered.

### 2. ⭐ Rate an Existing Skill

Help others by sharing your experience.

### 3. 🐛 Report Issues

Found a broken link or outdated info? Open an issue.

### 4. 📖 Improve Documentation

Fix typos, add examples, clarify instructions.

### 5. 🎨 Design & UX

Improve the README, add diagrams, enhance readability.

### 6. 🔧 Tooling

Build scripts to validate, test, or package skills.

---

## Adding a Skill

### Step 1: Check if it exists

Search the [existing skills](README.md) to avoid duplicates.

### Step 2: Prepare your skill

Your skill must include:

```
skills/your-skill-name/
├── SKILL.md          # Required: main skill file
├── README.md         # Required: user-facing documentation
├── references/       # Optional: supporting docs
├── templates/        # Optional: code templates
├── scripts/          # Optional: helper scripts
└── examples/         # Optional: usage examples
```

### Step 3: Use the template

Copy the template and fill in your content:

```bash
cp templates/SKILL-template.md skills/your-skill-name/SKILL.md
```

### Step 4: Validate

Run the validation script:

```bash
python scripts/validate-skill.py skills/your-skill-name/
```

### Step 5: Submit

```bash
git checkout -b add-your-skill-name
git add skills/your-skill-name/
git commit -m "feat: add your-skill-name"
git push origin add-your-skill-name
# Open a Pull Request
```

---

## Skill File Requirements

### SKILL.md

```markdown
---
name: your-skill-name
description: One-line description (max 100 chars)
version: 1.0.0
author: your-github-username
tags: [tag1, tag2, tag3]
agents: [hermes, claude, cursor, windsurf]
last_updated: YYYY-MM-DD
---

# Skill Title

## When to Use

- Use case 1
- Use case 2
- Use case 3

## Prerequisites

What the user/agent needs before using this skill.

## Instructions

### Step 1: Action Name

Clear, actionable instructions.

```bash
# Example command
```

### Step 2: Next Action

More instructions...

## Pitfalls

⚠️ Common mistakes:

1. **Pitfall 1**: Description and how to avoid
2. **Pitfall 2**: Description and how to avoid

## Verification

How to verify success:

- [ ] Check 1
- [ ] Check 2

## Examples

### Basic Example

```code
// Simple usage
```

### Advanced Example

```code
// Complex usage
```

## References

- [Link 1](url)
- [Link 2](url)
```

### README.md

User-facing documentation with:

1. **What it does** — Clear, concise description
2. **Why use it** — Benefits and use cases
3. **Quick start** — Get running in 30 seconds
4. **Configuration** — Options and settings
5. **Examples** — Real-world usage
6. **FAQ** — Common questions

---

## Rating a Skill

To rate an existing skill:

1. Open an issue with the template:
   ```
   Title: Rate: skill-name
   
   ## Rating
   
   - Utility: ⭐⭐⭐⭐⭐
   - Documentation: ⭐⭐⭐⭐
   - Maintenance: ⭐⭐⭐⭐⭐
   - Reliability: ⭐⭐⭐⭐
   - Elegance: ⭐⭐⭐⭐
   
   ## Experience
   
   How I used this skill and what happened.
   
   ## Suggestions
   
   How to improve this skill.
   ```

2. Or submit a PR adding your rating to the skill's README.

---

## Reporting Issues

### Bug Report

```markdown
**Skill:** skill-name
**Agent:** Hermes v2.0 / Claude Code / Cursor
**Description:** What went wrong

## Steps to Reproduce

1. Step 1
2. Step 2
3. Step 3

## Expected Behavior

What should have happened.

## Actual Behavior

What actually happened.

## Environment

- OS: macOS 14 / Ubuntu 22.04 / Windows 11
- Agent version: x.x.x
- Python version: 3.x.x
```

### Feature Request

```markdown
**Description:** What you want to add/change

## Use Case

Why this is needed.

## Proposed Solution

How to implement it.

## Alternatives Considered

Other approaches you thought about.
```

---

## Style Guide

### Writing Style

- **Be concise** — Get to the point quickly
- **Use examples** — Show, don't just tell
- **Be specific** — "Run `npm install`" not "Install dependencies"
- **Use active voice** — "Run the script" not "The script should be run"

### Formatting

- Use `code blocks` for commands, file paths, and code
- Use **bold** for emphasis
- Use `inline code` for technical terms
- Use bullet points for lists
- Use numbered steps for sequential instructions

### Tags

Use lowercase, hyphenated tags:

```
✅ good: [web-development, api-design, testing]
❌ bad: [Web Development, API Design, Testing]
```

Common tags:
- `development` — Software development
- `testing` — Testing and QA
- `devops` — DevOps and infrastructure
- `ai-ml` — AI and machine learning
- `productivity` — Productivity tools
- `creative` — Creative work
- `data` — Data processing
- `security` — Security related

### Agent Names

Use lowercase:

```
✅ good: hermes, claude, cursor, windsurf, copilot
❌ bad: Hermes, Claude Code, Cursor, Windsurf, GitHub Copilot
```

---

## Pull Request Process

### Before Submitting

- [ ] Skill validates: `python scripts/validate-skill.py skills/your-skill/`
- [ ] README is complete and accurate
- [ ] All links work
- [ ] No typos or grammatical errors
- [ ] Examples have been tested

### PR Template

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] New skill
- [ ] Update existing skill
- [ ] Bug fix
- [ ] Documentation update
- [ ] Tooling improvement

## Checklist

- [ ] I have read the [contributing guidelines](CONTRIBUTING.md)
- [ ] My skill follows the [style guide](#style-guide)
- [ ] I have tested my examples
- [ ] I have updated documentation as needed

## Related Issues

Closes #123
```

### Review Process

1. **Automated checks** — Validation script runs
2. **Maintainer review** — At least one maintainer reviews
3. **Community feedback** — 24-hour comment period
4. **Merge** — After approval

### After Merge

- Your skill appears in the next release
- You're added to the contributors list
- Your skill can be rated by the community

---

## Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone.

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behavior:**
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other unprofessional conduct

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting the maintainers.

---

## Questions?

- 💬 [GitHub Discussions](https://github.com/mapan0424/awesome-ai-agent-skills/discussions)
- 🐛 [Issues](https://github.com/mapan0424/awesome-ai-agent-skills/issues)

---

**Thank you for contributing! 🎉**

*Every skill you add helps the entire AI agent community.*
