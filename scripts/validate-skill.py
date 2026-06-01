#!/usr/bin/env python3
"""
Validate AI Agent Skills for awesome-ai-agent-skills repository.

Usage:
    python scripts/validate-skill.py skills/my-skill/
    python scripts/validate-skill.py --all
"""

import os
import re
import sys
import yaml
from pathlib import Path
from typing import List, Tuple

# Required fields in SKILL.md frontmatter
REQUIRED_FIELDS = ['name', 'description', 'version', 'author', 'tags', 'agents']

# Valid agents
VALID_AGENTS = ['hermes', 'claude', 'cursor', 'windsurf', 'copilot', 'aider', 'continue', 'other']

# Valid tags (lowercase, hyphenated)
VALID_TAG_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')

# Max lengths
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 200


class SkillValidator:
    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate(self) -> bool:
        """Validate a skill directory. Returns True if valid."""
        self.errors = []
        self.warnings = []

        # Check SKILL.md exists
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            self.errors.append("SKILL.md not found")
            return False

        # Parse SKILL.md
        content = skill_md.read_text(encoding='utf-8')
        frontmatter, body = self._parse_frontmatter(content)

        if frontmatter is None:
            self.errors.append("Invalid or missing YAML frontmatter")
            return False

        # Validate frontmatter
        self._validate_frontmatter(frontmatter)

        # Validate body
        self._validate_body(body)

        # Check README.md
        self._validate_readme()

        # Check for common issues
        self._check_common_issues()

        return len(self.errors) == 0

    def _parse_frontmatter(self, content: str) -> Tuple[dict, str]:
        """Parse YAML frontmatter from markdown content."""
        if not content.startswith('---'):
            return None, content

        try:
            end = content.index('---', 3)
            yaml_content = content[3:end].strip()
            body = content[end + 3:].strip()
            frontmatter = yaml.safe_load(yaml_content)
            return frontmatter, body
        except (ValueError, yaml.YAMLError) as e:
            self.errors.append(f"Failed to parse frontmatter: {e}")
            return None, content

    def _validate_frontmatter(self, fm: dict):
        """Validate frontmatter fields."""
        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in fm:
                self.errors.append(f"Missing required field: {field}")

        # Validate name
        if 'name' in fm:
            name = fm['name']
            if not isinstance(name, str):
                self.errors.append("name must be a string")
            elif len(name) > MAX_NAME_LENGTH:
                self.errors.append(f"name too long (max {MAX_NAME_LENGTH} chars)")
            elif not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name):
                self.errors.append("name must be lowercase, hyphenated (e.g., my-skill)")

        # Validate description
        if 'description' in fm:
            desc = fm['description']
            if not isinstance(desc, str):
                self.errors.append("description must be a string")
            elif len(desc) > MAX_DESCRIPTION_LENGTH:
                self.warnings.append(f"description is long ({len(desc)} chars, recommended max {MAX_DESCRIPTION_LENGTH})")

        # Validate version
        if 'version' in fm:
            version = str(fm['version'])
            if not re.match(r'^\d+\.\d+\.\d+$', version):
                self.warnings.append(f"version '{version}' not in semver format (x.y.z)")

        # Validate tags
        if 'tags' in fm:
            tags = fm['tags']
            if not isinstance(tags, list):
                self.errors.append("tags must be a list")
            else:
                for tag in tags:
                    if not isinstance(tag, str):
                        self.errors.append(f"tag must be a string: {tag}")
                    elif not VALID_TAG_PATTERN.match(tag):
                        self.errors.append(f"invalid tag format: '{tag}' (use lowercase, hyphenated)")

        # Validate agents
        if 'agents' in fm:
            agents = fm['agents']
            if not isinstance(agents, list):
                self.errors.append("agents must be a list")
            else:
                for agent in agents:
                    if not isinstance(agent, str):
                        self.errors.append(f"agent must be a string: {agent}")
                    elif agent.lower() not in VALID_AGENTS:
                        self.warnings.append(f"unknown agent: '{agent}' (valid: {', '.join(VALID_AGENTS)})")

    def _validate_body(self, body: str):
        """Validate the body content."""
        # Check for required sections
        required_sections = ['When to Use', 'Instructions']
        for section in required_sections:
            if f'## {section}' not in body and f'# {section}' not in body:
                self.warnings.append(f"Missing recommended section: {section}")

        # Check for examples
        if '## Examples' not in body and '### Example' not in body:
            self.warnings.append("No examples section found")

        # Check for pitfalls
        if '## Pitfalls' not in body and '## Troubleshooting' not in body:
            self.warnings.append("No pitfalls/troubleshooting section found")

        # Check for verification
        if '## Verification' not in body:
            self.warnings.append("No verification section found")

    def _validate_readme(self):
        """Check if README.md exists and has content."""
        readme = self.skill_path / 'README.md'
        if not readme.exists():
            self.warnings.append("README.md not found (recommended for user-facing docs)")
        else:
            content = readme.read_text(encoding='utf-8')
            if len(content) < 100:
                self.warnings.append("README.md seems too short")

    def _check_common_issues(self):
        """Check for common issues."""
        # Check for empty files
        for file in self.skill_path.rglob('*'):
            if file.is_file() and file.stat().st_size == 0:
                self.warnings.append(f"Empty file: {file.name}")

        # Check for placeholder content
        skill_md = self.skill_path / 'SKILL.md'
        if skill_md.exists():
            content = skill_md.read_text(encoding='utf-8')
            placeholders = ['TODO', 'FIXME', 'XXX', 'PLACEHOLDER']
            for ph in placeholders:
                if ph in content.upper():
                    self.warnings.append(f"Found placeholder: {ph}")

    def print_report(self):
        """Print validation report."""
        name = self.skill_path.name

        if self.errors:
            print(f"\n❌ {name}: FAILED")
            for err in self.errors:
                print(f"   ERROR: {err}")
        elif self.warnings:
            print(f"\n⚠️  {name}: PASSED with warnings")
            for warn in self.warnings:
                print(f"   WARNING: {warn}")
        else:
            print(f"\n✅ {name}: PASSED")

        return len(self.errors) == 0


def find_all_skills(base_path: Path) -> List[Path]:
    """Find all skill directories."""
    skills_dir = base_path / 'skills'
    if not skills_dir.exists():
        return []

    return [
        d for d in skills_dir.iterdir()
        if d.is_dir() and (d / 'SKILL.md').exists()
    ]


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/validate-skill.py skills/my-skill/")
        print("  python scripts/validate-skill.py --all")
        sys.exit(1)

    base_path = Path(__file__).parent.parent

    if sys.argv[1] == '--all':
        # Validate all skills
        skills = find_all_skills(base_path)
        if not skills:
            print("No skills found in skills/ directory")
            sys.exit(0)

        results = []
        for skill_path in sorted(skills):
            validator = SkillValidator(skill_path)
            valid = validator.validate()
            validator.print_report()
            results.append((skill_path.name, valid))

        # Summary
        total = len(results)
        passed = sum(1 for _, v in results if v)
        failed = total - passed

        print(f"\n{'='*50}")
        print(f"Summary: {passed}/{total} passed, {failed} failed")

        if failed > 0:
            sys.exit(1)
    else:
        # Validate single skill
        skill_path = Path(sys.argv[1])
        if not skill_path.is_absolute():
            skill_path = base_path / skill_path

        if not skill_path.exists():
            print(f"Error: Skill directory not found: {skill_path}")
            sys.exit(1)

        validator = SkillValidator(skill_path)
        valid = validator.validate()
        validator.print_report()

        if not valid:
            sys.exit(1)


if __name__ == '__main__':
    main()
