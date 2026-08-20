# Contributing to AI Developer Agents

Thank you for your interest in contributing! This guide will walk you through everything you need to know to add or improve agents in this repository.

## Table of Contents

1. [Before You Start](#before-you-start)
2. [Ways to Contribute](#ways-to-contribute)
3. [Adding a New Agent](#adding-a-new-agent)
4. [Improving Existing Agents](#improving-existing-agents)
5. [Testing Your Changes](#testing-your-changes)
6. [Submitting a Pull Request](#submitting-a-pull-request)
7. [Community Guidelines](#community-guidelines)

---

## Before You Start

### What You Need
- **Git**: To clone the repository and submit changes
- **Python 3**: To run the validation script
- **A GitHub account**: To submit issues and pull requests

### First Time Contributing?
If you're new to open source or GitHub, don't worry! Here's a quick primer:
1. **Fork** the repository (make your own copy)
2. **Clone** your fork to your computer
3. Make changes on a **branch**
4. **Push** your branch to GitHub
5. Open a **Pull Request** (PR) to propose your changes

---

## Ways to Contribute

### 1. Report a Bug
Found something wrong? Let us know!
- Search existing [issues](https://github.com/nimish-nirmal/ai-developer-agents/issues) to make sure it hasn't been reported
- Open a new issue with:
  - What you expected to happen
  - What actually happened
  - Steps to reproduce the issue
  - Your environment (OS, Python version, AI tool used)

### 2. Request a Feature
Have an idea for a new agent or improvement?
- Check if someone already suggested it
- Open an issue describing the feature and why it's useful

### 3. Add a New Agent
Want to create a new specialist agent? Great! See the detailed guide below.

### 4. Improve Existing Agents
Spot a way to make an agent better? Fix a typo, add more detail, or improve the structure.

---

## Adding a New Agent

### Step 1: Open an Issue
Before writing code, open an issue using the [New Agent Request](.github/ISSUE_TEMPLATE/new-agent.md) template. This helps us:
- Discuss if the agent fits the repository
- Agree on the agent's scope and name
- Avoid duplicate work

### Step 2: Understand the Agent Format

All agents follow one of two formats:

#### Legacy Format (current agents)
```markdown
# SYSTEM PROMPT
You MUST follow all instructions in this file strictly.
Do not ignore any section.
Do not generate generic output.

## EXECUTION RULE
When this file is loaded, immediately execute the task using provided input.
Do not repeat instructions. Only produce structured output.

# Agent: <Agent Name>

## Role
Describe the agent's expertise and personality.

## Task
Explain what the agent does when given input.

## Output Format
Define the structure of the agent's response:
- ### Summary
- ### Detailed sections
- ### Recommendations

## Input
Describe what input the user should provide.
```

#### New Format (optional, for future agents)
```markdown
---
name: <agent-name>
description: <brief description>
model: claude-sonnet-4-5
---

# <Agent Name> Agent

## Role
...

## Core Responsibilities
...

## Input/Output
...

## Best Practices
...
```

### Step 3: Create Your Agent File

Create a new file in the `agents/` directory:
- Use snake_case for filenames: `my_new_agent.md`
- Follow the legacy format (all current agents use this)
- Make the agent focused on ONE specific domain
- Include clear Role, Task, Output Format, and Input sections

**Good agent names:**
- `security_auditor.md` — specific domain (security)
- `database_expert.md` — specific domain (databases)
- `iot_protocol_specialist.md` — specific domain (IoT)

**Bad agent names:**
- `helper.md` — too vague
- `backend.md` — too broad (use specific: database, API, auth, etc.)

### Step 4: Write Great Agent Content

A great agent prompt includes:
- **Clear role definition**: What the AI knows and how it behaves
- **Specific evaluation criteria**: What to look for in the input
- **Structured output format**: Exactly what sections to return
- **Input guidance**: What the user should provide

Example from `code_reviewer.md`:
```markdown
## Role
You are a senior software engineer specializing in backend systems, APIs, and performance optimization.
You focus on correctness, maintainability, and production readiness.

## Task
Review the given code.

Evaluate:
- **Logical Correctness** (bugs, logic errors, off-by-one errors, race conditions)
- **Code Structure & Readability** (naming, complexity, duplication, abstractions)
- **Performance** (inefficient algorithms, memory leaks, unnecessary allocations, network calls)
...

## Output Format

### Summary
Provide overall code quality assessment with reasoning:
- Quality grade (A / B / C / D / F)
- Estimated refactoring effort
- Immediate action items
- Deployment risk assessment

### Critical Bugs
List defects that can break functionality or produce incorrect results:
...
```

### Step 5: Validate Your Agent

Run the validation script:
```bash
python scripts/validate_agents.py
```

This checks:
- The file has a `# SYSTEM PROMPT` header
- Required sections exist (`Role`, `Task`, `Output Format`, `Input`)
- The file isn't empty or a placeholder

### Step 6: Update Documentation

If you added a new agent:
1. Add it to the `Agent Directory` table in `README.md`
2. Add it to the `docs/agents.md` reference guide
3. Update the `orchestrator.md` to include your agent in the dispatch list

### Step 7: Submit a Pull Request

1. Create a new branch: `git checkout -b add-my-agent`
2. Add your files: `git add agents/my_new_agent.md`
3. Commit: `git commit -m "Add <Agent Name> agent"`
4. Push: `git push origin add-my-agent`
5. Open a PR using the pull request template

---

## Improving Existing Agents

### How to Improve
- Fix typos or unclear instructions
- Add missing evaluation criteria
- Improve the output format for better results
- Update the agent to cover new best practices

### Process
1. Open an issue describing the improvement
2. Make your changes in a feature branch
3. Run `python scripts/validate_agents.py` to ensure the agent still validates
4. Submit a PR with a clear description of what changed and why

---

## Testing Your Changes

### Local Validation
```bash
# Validate all agents
python scripts/validate_agents.py

# Test a specific agent by loading it into your AI tool
# (Cursor, Claude, ChatGPT, etc.) and running a sample task
```

### Manual Testing
After writing your agent:
1. Load it into your AI tool
2. Give it a sample task relevant to its domain
3. Verify the output follows your specified format
4. Check that the recommendations are actionable and accurate

---

## Submitting a Pull Request

### PR Title Format
- `Add <Agent Name> agent` — for new agents
- `Improve <Agent Name> agent` — for improvements
- `Fix <Agent Name> agent` — for bug fixes

### PR Description
Use the pull request template and include:
- What you changed and why
- How you tested it
- Screenshots or examples of the agent's output (if applicable)

### Checklist Before Submitting
- [ ] I ran `python scripts/validate_agents.py` and it passed
- [ ] I tested the agent with a real-world example
- [ ] I updated `README.md` if I added a new agent
- [ ] I updated `docs/agents.md` if I added a new agent
- [ ] I followed the existing code style and conventions

---

## Community Guidelines

### Be Respectful
- Provide constructive feedback
- Welcome newcomers and help them get started
- Respect different skill levels and backgrounds

### Be Clear
- Write clear, descriptive issue titles
- Provide context and examples
- Link to related issues or PRs

### Be Patient
- Maintainers review PRs in their spare time
- It may take a few days to get feedback
- If you haven't heard back in a week, a polite comment is okay

---

## Code of Conduct

By participating, you agree to uphold our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Questions?

If you're stuck or have questions:
1. Check the [README.md](../README.md) for general usage
2. Read [docs/agents.md](../docs/agents.md) for agent reference
3. Open an issue with your question

We're here to help!
