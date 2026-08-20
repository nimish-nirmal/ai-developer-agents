#!/usr/bin/env python3
"""
validate_agents.py

Validates all markdown agent files in the agents/ directory to ensure they
adhere to required formatting guidelines.

Two formats are supported:

1. SYSTEM PROMPT format (legacy/current):
   - Starts with '# SYSTEM PROMPT'
   - Contains '# Agent: <Name>'
   - Contains '## Role', '## Task', '## Output Format', '## Input'

2. YAML frontmatter format (new):
   - YAML frontmatter with required fields: name, description, model
   - Heading '# <Agent Name> Agent'
   - Sections: Role, Core Responsibilities, Input/Output, Best Practices
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REQUIRED_FIELDS = {"name", "description", "model"}
REQUIRED_SECTIONS = ["Role", "Core Responsibilities", "Input/Output", "Best Practices"]
LEGACY_SECTIONS = ["Role", "Task", "Output Format", "Input"]
AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def parse_frontmatter(content: str) -> tuple[dict | None, str | None]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return None, None
    try:
        data = yaml.safe_load(match.group(1))
        return data, match.group(2)
    except yaml.YAMLError:
        return None, None


def validate_new_format(path: Path, content: str, body: str) -> list[str]:
    errors = []
    frontmatter, _ = parse_frontmatter(content)

    if frontmatter is None:
        return ["Missing or invalid YAML frontmatter"]

    missing = REQUIRED_FIELDS - set(frontmatter.keys())
    if missing:
        errors.append(f"Missing required frontmatter fields: {missing}")

    if frontmatter.get("name"):
        expected_filename = f"{slugify(str(frontmatter['name']))}.md"
        if path.name != expected_filename:
            errors.append(
                f"Filename '{path.name}' does not match agent name. Expected '{expected_filename}'"
            )

    agent_name = frontmatter.get("name", "")
    if agent_name and f"# {agent_name} agent" not in body.lower():
        errors.append("Missing required heading '# <Agent Name> Agent'")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing required section '{section}'")

    if len(content.strip()) < 100:
        errors.append("File appears empty or placeholder-only")

    return errors


def validate_legacy_format(path: Path, content: str) -> list[str]:
    errors = []
    body = content

    if not body.strip().startswith("# SYSTEM PROMPT"):
        errors.append("Missing '# SYSTEM PROMPT' header")
        return errors

    if "# Agent:" not in body:
        errors.append("Missing '# Agent: <Name>' declaration")

    for section in LEGACY_SECTIONS:
        if section not in body:
            errors.append(f"Missing required section '{section}'")

    if len(content.strip()) < 100:
        errors.append("File appears empty or placeholder-only")

    return errors


def validate_file(path: Path) -> tuple[list[str], str]:
    """Returns (errors, format_type)."""
    content = path.read_text(encoding="utf-8")

    if content.strip().startswith("# SYSTEM PROMPT"):
        errors = validate_legacy_format(path, content)
        return errors, "legacy"

    _, body = parse_frontmatter(content)
    if body is not None:
        errors = validate_new_format(path, content, body)
        return errors, "new"

    return [f"{path.name}: Unrecognized format"], "unknown"


def main() -> int:
    if not AGENTS_DIR.exists() or not AGENTS_DIR.is_dir():
        print(f"ERROR: Agents directory not found at {AGENTS_DIR}", file=sys.stderr)
        return 1

    agent_files = sorted(AGENTS_DIR.glob("*.md"))
    if not agent_files:
        print("ERROR: No agent markdown files found.", file=sys.stderr)
        return 1

    all_errors = []
    counts = {"legacy": 0, "new": 0, "unknown": 0}

    for path in agent_files:
        errors, fmt = validate_file(path)
        counts[fmt] = counts.get(fmt, 0) + 1
        all_errors.extend([f"{path.name}: {e}" for e in errors])

    print(
        f"Found {len(agent_files)} agent file(s): "
        f"{counts['legacy']} legacy, {counts['new']} new, {counts['unknown']} unknown."
    )

    if all_errors:
        print(f"Validation failed for {len(all_errors)} issue(s):\n", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("Validation passed: all agent(s) validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
