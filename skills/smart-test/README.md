# Smart Test Skill

Intelligently run and fix tests based on your code changes.

## What It Does

This skill helps you test efficiently by:

1. **Detecting** which files changed
2. **Mapping** changes to related tests
3. **Running** only relevant tests
4. **Fixing** failures with clear guidance

## Why Use It

- ✅ Faster feedback loop
- ✅ Run only relevant tests
- ✅ Clear failure analysis
- ✅ Works with any test framework

## Quick Start

```bash
# Make your code changes
vim src/auth/login.js

# The skill will automatically:
# 1. Find related tests
# 2. Run them
# 3. Report results
```

## Supported Frameworks

| Language | Framework | Command |
|----------|-----------|---------|
| JavaScript | Jest | `npx jest --findRelatedTests` |
| Python | pytest | `pytest tests/test_*.py` |
| Java | JUnit | `./gradlew test` |
| Go | testing | `go test ./...` |
| Ruby | RSpec | `rspec spec/` |

## Examples

### JavaScript (Jest)

```bash
# Changed: src/utils/validation.js
# Skill runs: npx jest --findRelatedTests src/utils/validation.js

# Output:
# PASS tests/utils/validation.test.js
#   validateEmail ✓
#   validatePassword ✓
```

### Python (pytest)

```bash
# Changed: lib/database.py
# Skill runs: pytest tests/test_database.py -v

# Output:
# tests/test_database.py::TestDB::test_connection PASSED
# tests/test_database.py::TestDB::test_query PASSED
```

## Common Patterns

### Find Related Tests

```bash
# JavaScript
find tests -name "*.test.js" | grep -i "$(basename src/file.js .js)"

# Python
find tests -name "test_*.py" | grep -i "$(basename lib/module.py .py)"
```

### Run Failed Tests Only

```bash
# Jest
npm test -- --onlyFailures

# pytest
pytest --lf
```

## Learn More

- [SKILL.md](SKILL.md) - Full skill instructions
- [Test Driven Development](../test-driven-development/) - TDD workflow

---

*Part of [Awesome AI Agent Skills](https://github.com/mapan0424/awesome-ai-agent-skills)*
