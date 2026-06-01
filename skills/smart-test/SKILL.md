---
name: smart-test
description: Intelligently run and fix tests based on code changes
version: 1.0.0
author: mapan0424
tags: [testing, quality, development, ci-cd]
agents: [hermes, claude, cursor, windsurf]
last_updated: 2026-06-02
---

# Smart Test

> Automatically identify and run relevant tests based on your code changes, then fix failures.

## When to Use

✅ **Use this skill when:**
- You've made code changes and need to verify they work
- You want to run only relevant tests (not the full suite)
- Tests are failing and you need to fix them
- You want to improve test coverage

❌ **Do NOT use when:**
- Writing tests from scratch (use test-driven-development instead)
- Debugging production issues (use systematic-debugging)

## Prerequisites

- Test framework installed (Jest, pytest, JUnit, etc.)
- Existing test suite
- Code changes ready to test

## Quick Start

```bash
# Find tests related to changed files
git diff --name-only | grep -E "\.(js|ts|py|java)$" | while read f; do
  echo "Related test: ${f%.*}.test.${f##*.}"
done

# Run relevant tests
npm test -- --findRelatedTests $(git diff --name-only)
```

## Instructions

### Step 1: Identify Changed Files

```bash
# What files changed?
git diff --name-only HEAD~1

# Or for staged changes
git diff --cached --name-only
```

### Step 2: Map to Test Files

| Source File | Test File Pattern |
|-------------|-------------------|
| `src/auth/login.js` | `tests/auth/login.test.js` |
| `lib/utils.py` | `tests/test_utils.py` |
| `src/User.java` | `test/UserTest.java` |

Common patterns:
```bash
# JavaScript/TypeScript
echo "src/components/Button.tsx" | sed 's|src/|tests/|;s|\.tsx$|.test.tsx|'

# Python
echo "lib/utils.py" | sed 's|lib/|tests/test_|;s|\.py$||'

# Java
echo "src/main/User.java" | sed 's|src/main/|src/test/|;s|\.java$|Test.java|'
```

### Step 3: Run Targeted Tests

```bash
# Jest (JavaScript)
npx jest --findRelatedTests src/auth/login.js

# pytest (Python)
pytest tests/test_utils.py -v

# Gradle (Java)
./gradlew test --tests "*UserTest*"

# All changed files
git diff --name-only | xargs -I {} sh -c 'echo "Testing: {}" && npm test -- --findRelatedTests {}'
```

### Step 4: Analyze Failures

```bash
# Run with verbose output
npm test -- --verbose 2>&1 | tee test-output.log

# Show only failures
grep -A 5 "FAIL" test-output.log
```

### Step 5: Fix and Re-run

```bash
# Fix the code or test
vim src/auth/login.js

# Re-run failing test
npm test -- --testPathPattern="login" --watch
```

## Pitfalls

⚠️ **Common Mistakes:**

### 1. Running all tests every time

**Problem:** Full test suite takes too long

**Solution:** Use targeted test runs:
```bash
# Instead of
npm test  # Runs everything

# Do this
npm test -- --findRelatedTests src/changed-file.js
```

### 2. Ignoring test output

**Problem:** Just checking pass/fail, not reading errors

**Solution:** Read the actual error message:
```bash
# Show full error details
npm test -- --verbose 2>&1 | grep -B 5 -A 10 "Error"
```

### 3. Fixing tests to pass (not fixing code)

**Problem:** Changing tests to match broken behavior

**Solution:** 
1. Understand what the test verifies
2. Fix the source code, not the test
3. Only modify test if requirements changed

### 4. Not testing edge cases

**Problem:** Tests pass with happy path only

**Solution:** Add tests for:
- Null/undefined inputs
- Empty arrays/strings
- Boundary values
- Error conditions

## Verification

After running tests:

- [ ] **All tests pass**
  ```bash
  npm test 2>&1 | tail -5
  # Should show: Tests: X passed, X total
  ```

- [ ] **Coverage is maintained**
  ```bash
  npm test -- --coverage
  # Check coverage didn't decrease
  ```

- [ ] **No skipped tests**
  ```bash
  grep -r "skip\|xit\|xdescribe" tests/
  # Should be empty
  ```

## Examples

### Example 1: JavaScript with Jest

```bash
# Changed file
git diff --name-only
# src/utils/validation.js

# Run related tests
npx jest --findRelatedTests src/utils/validation.js

# Output:
# PASS tests/utils/validation.test.js
#   validateEmail
#     ✓ should validate correct email
#     ✓ should reject invalid email
#     ✓ should handle empty string
#
# Test Suites: 1 passed, 1 total
# Tests:       3 passed, 3 total
```

### Example 2: Python with pytest

```bash
# Changed file
git diff --name-only
# lib/database.py

# Run related tests
pytest tests/test_database.py -v

# Output:
# tests/test_database.py::TestDatabase::test_connection PASSED
# tests/test_database.py::TestDatabase::test_query PASSED
# tests/test_database.py::TestDatabase::test_transaction PASSED
```

### Example 3: Fixing a Failing Test

```bash
# Run tests
npm test 2>&1 | grep "FAIL"
# FAIL tests/auth/login.test.js

# See the error
npm test -- --testPathPattern="login" 2>&1 | grep -A 10 "Error"
# Expected: { success: true }
# Received: { success: false, error: "Invalid credentials" }

# Fix the code
vim src/auth/login.js

# Re-run
npm test -- --testPathPattern="login"
# PASS tests/auth/login.test.js
```

## Advanced: Watch Mode

```bash
# Jest watch mode - re-runs on file changes
npm test -- --watch

# pytest watch mode (with pytest-watch)
ptw tests/test_utils.py

# Run only failed tests
npm test -- --onlyFailures
```

## References

- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [pytest Documentation](https://docs.pytest.org/)
- [Testing Library](https://testing-library.com/)
- [Test Driven Development](../../skills/test-driven-development/)

---

*Part of [Awesome AI Agent Skills](https://github.com/mapan0424/awesome-ai-agent-skills)*
