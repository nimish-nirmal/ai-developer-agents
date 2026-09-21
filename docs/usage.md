# Agent Usage Guide

This guide shows how to load and use the AI Developer Agents in popular AI coding tools and extensions.

## Table of Contents

1. [General Concept](#general-concept)
2. [GitHub Copilot & GitHub Tools](#github-copilot--github-tools)
3. [Cline](#cline)
4. [Cursor](#cursor)
5. [Claude Projects](#claude-projects)
6. [ChatGPT Custom GPTs](#chatgpt-custom-gpts)
7. [Kilo](#kilo)
8. [Windsurf](#windsurf)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## General Concept

All agents in this repository are **markdown files** (`.md`) that contain:
- A **system prompt** that defines the AI's role, expertise, and behavior
- An **output format** that structures the AI's responses
- **Input guidance** that tells users what to provide

To use any agent, you need to:
1. **Copy the contents** of the `.md` file
2. **Paste it** into your AI tool's system prompt, instructions, or project rules area
3. **Provide your task input** as you normally would

The AI will then "become" that agent and respond according to its specialized instructions.

---

## GitHub Copilot & GitHub Tools

### GitHub Copilot (VS Code / JetBrains)

GitHub Copilot supports project-level instructions through a special file.

#### How to Load Agents

1. In your repository, create `.github/copilot-instructions.md`.
2. Paste the contents of your chosen agent file.
3. Commit the file.
4. Copilot will automatically use these instructions as project context.

**Note**: Only one set of instructions can be active at a time. For multi-agent workflows, use the Orchestrator agent.

#### Example
```bash
# Create Copilot instructions
mkdir -p .github
cp agents/orchestrator.md .github/copilot-instructions.md
git add .github/copilot-instructions.md
git commit -m "Add Copilot instructions for project"
```

### GitHub Actions (CI Validation)

The repository includes a GitHub Actions workflow that validates all agent files on every PR.

#### How It Works
- Triggered on: PRs that modify `agents/**/*.md`, `scripts/**`, or `.github/workflows/**`
- Runs: `python scripts/validate_agents.py`
- Fails the check if any agent file is malformed

#### Viewing Results
1. Go to your repository on GitHub.
2. Click **Actions** tab.
3. Click on the latest workflow run.
4. Check the validation results.

### GitHub Issues & PRs

- Use `.github/ISSUE_TEMPLATE/new-agent.md` to propose new agents.
- Use `.github/pull_request_template.md` when submitting agent changes.

---

## Cline

Cline is a VS Code extension that brings AI coding assistance with support for custom prompts.

### How to Load Agents

#### Option 1: Chat Prompt
1. Open Cline in VS Code.
2. Click the **prompt** or **instructions** button.
3. Paste the agent contents.
4. Start your task.

#### Option 2: Project-Level Instructions
1. Create a `.cline/` directory in your project.
2. Create `.cline/instructions.md` or similar.
3. Paste the agent contents.
4. Cline may automatically detect these (check Cline's documentation for exact behavior).

#### Option 3: VS Code Settings
1. Open VS Code Settings (`Ctrl+,` / `Cmd+,`).
2. Search for "Cline" or "Cline Instructions".
3. Paste the agent contents in the instructions field.

### Recommended Setup
```bash
# Create Cline project instructions
mkdir -p .cline
cp agents/orchestrator.md .cline/instructions.md
```

### Pro Tip
Cline works best when you provide **context** along with the agent prompt:
1. Load the agent instructions.
2. Open the relevant files in VS Code.
3. Cline will use both the agent instructions and your open files as context.

---

## Cursor

Cursor is an AI-first code editor with built-in support for custom rules.

### How to Load Agents

#### Option 1: Project Rules (Recommended)
1. Open your project in Cursor.
2. Create a `.cursor/rules/` directory.
3. Copy agent `.md` files into `.cursor/rules/`.
4. Cursor automatically detects and loads these rules.

```bash
mkdir -p .cursor/rules
cp agents/orchestrator.md .cursor/rules/
```

#### Option 2: Global Rules
1. Open Cursor Settings.
2. Go to **Rules** or **AI Rules**.
3. Paste agent contents.
4. These apply to all projects.

#### Option 3: Chat Instructions
1. Open Cursor Chat (`Cmd+L` / `Ctrl+L`).
2. Click the **@** symbol or instructions icon.
3. Paste the agent contents.

### Using Multiple Agents
Cursor supports multiple rule files. You can:
- Keep `orchestrator.md` as a project rule for general tasks
- Load specialist agents in chat when needed for specific tasks

### Pro Tip
Use **@-mentions** in Cursor Chat to reference specific files or rules:
```
@orchestrator.md Build a REST API for a todo app
```

---

## Claude Projects

Claude Projects allows you to upload files and set custom instructions for a project.

### How to Load Agents

#### Option 1: Upload as Knowledge
1. Go to [Claude Projects](https://claude.ai/projects).
2. Create a new project.
3. Click **Upload** and select the agent `.md` files.
4. Claude will use these as project knowledge.

#### Option 2: Paste as Instructions
1. Open the project.
2. Click **Instructions** or **Project Settings**.
3. Paste the agent contents into the instructions field.
4. Save.

#### Option 3: Conversation-Level Prompt
1. Start a new conversation in the project.
2. Paste the agent contents at the start of your message.
3. Follow with your task.

### Recommended Setup
- Upload all 14 agent files to the project.
- Set the **Orchestrator** as the default instructions.
- Reference other agents in your prompts: *"Use the database_expert agent to design the schema..."*

### Pro Tip
Claude Projects maintains **persistent context**. Upload all agents once, then reference them in future conversations without re-uploading.

---

## ChatGPT Custom GPTs

ChatGPT Custom GPTs let you create specialized AI assistants with custom instructions.

### How to Load Agents

#### Option 1: Create a Custom GPT (Recommended)
1. Go to [GPT Store](https://chat.openai.com/gpts) or ChatGPT Settings.
2. Click **Create a GPT** or **My GPTs** → **Create a GPT**.
3. In the **Instructions** field, paste the agent contents.
4. Optionally upload supporting files from `examples/`.
5. Save and publish (or keep private).

#### Option 2: Use in Custom Instructions
1. Go to ChatGPT Settings → **Personalization** → **Custom instructions**.
2. Paste the agent contents.
3. These will apply to all conversations.

#### Option 3: Conversation Prompt
1. Start a new chat.
2. Paste the agent contents as your first message.
3. Follow with your task.

### Creating Multiple GPTs
You can create one GPT per agent:
- **Orchestrator GPT** — paste `orchestrator.md`
- **Code Reviewer GPT** — paste `code_reviewer.md`
- **Database Expert GPT** — paste `database_expert.md`
- etc.

Or create a single **Developer Team GPT** with the Orchestrator instructions and reference other agents.

### Pro Tip
Use **Custom Actions** or **Knowledge** uploads to add project-specific context to your GPTs.

---

## Kilo

Kilo is an AI agent platform that supports markdown-based agent definitions.

### How to Load Agents

#### Option 1: Direct Chat
1. Open Kilo.
2. In the chat input, use the `/agent` command or paste the agent contents directly.
3. Provide your task.

#### Option 2: Project Configuration
1. Create a `.kilo/` directory in your project.
2. Place agent `.md` files in `.kilo/agents/`.
3. Reference them in your `.kilo/config.json` or `.kilo.json` if applicable.

#### Option 3: Workspace Rules
1. Create a `.kilo/rules/` directory.
2. Place agent `.md` files there.
3. Kilo will detect and load these rules automatically.

### Recommended Setup
```bash
# Create Kilo workspace rules
mkdir -p .kilo/rules
cp agents/orchestrator.md .kilo/rules/
```

### Pro Tip
Kilo supports **model selection** per agent. You can specify a different model for each agent in your Kilo configuration if needed.

---

## Windsurf

Windsurf is an AI-powered IDE with support for custom rules and instructions.

### How to Load Agents

#### Option 1: Project Rules (Recommended)
1. Open your project in Windsurf.
2. Create a `.windsurf/rules/` directory.
3. Copy agent `.md` files into `.windsurf/rules/`.
4. Windsurf automatically loads these rules.

```bash
mkdir -p .windsurf/rules
cp agents/orchestrator.md .windsurf/rules/
```

#### Option 2: Global Rules
1. Open Windsurf Settings.
2. Navigate to **Rules** or **AI Rules**.
3. Paste agent contents.
4. These apply to all projects.

#### Option 3: Chat Instructions
1. Open Windsurf Chat.
2. Paste the agent contents in the chat input.
3. Windsurf will follow these instructions for the conversation.

### Using Multiple Agents
Windsurf supports multiple rule files. You can:
- Set `orchestrator.md` as a project rule
- Load specialist agents in chat when needed

---

## Best Practices

### 1. Start with the Orchestrator
For any non-trivial task, start with `agents/orchestrator.md`. It will automatically delegate to the right specialists.

### 2. Provide Good Context
The better your input, the better the output. Include:
- Project structure and tech stack
- Existing code examples
- Specific requirements and constraints
- Any relevant documentation

### 3. Use the Right Tool for the Job
| Task | Recommended Agent |
|------|-------------------|
| Solo project / everything at once | `general_engineer.md` |
| Debugging a bug or crash | `debugger.md` |
| Refactoring legacy code | `refactoring_specialist.md` |
| Deep security assessment / pentesting | `cyber_security_expert.md` |
| Marketing, sales docs, PPTs, content scraping | `business_documentation_specialist.md` |
| Building something new (team mode) | `orchestrator.md` |
| Reviewing code | `code_reviewer.md` |
| Designing a system | `architecture_reviewer.md` |
| Writing tests | `test_writer.md` |
| Designing a database | `database_expert.md` |
| Security check | `security_auditor.md` |
| Performance issues | `performance_analyst.md` |
| API design | `api_specialist.md` |
| Frontend review | `frontend_reviewer.md` |
| IoT/edge systems | `iot_protocol_specialist.md` |
| Infrastructure review | `devops_reviewer.md` |
| Integration review | `integration_reviewer.md` |

### 4. Validate Agents Locally
Before committing or sharing:
```bash
python scripts/validate_agents.py
```

### 5. Customize for Your Stack
Feel free to modify agents to match your tech stack:
- Add your company's coding standards
- Include domain-specific requirements
- Adjust evaluation criteria for your use case

---

## Steering Files

The `steering/` directory contains generic, platform-agnostic handler files that encode reusable patterns for task execution, validation, security, and workflow orchestration.

### What Are Steering Files?

Steering files are **shared behavioral templates** that agents can reference to ensure consistent execution across different AI tools and runtimes. They cover:
- Task execution phases and decision guidance
- Validation principles for requirements, architecture, code, APIs, and deployments
- Secure coding guidelines
- Workflow orchestration patterns
- Technical writing standards
- Version control practices
- Implementation pitfalls to avoid

### How to Use Steering Files

#### Option 1: Include in Agent Prompts
Paste the relevant steering file content into an agent's system prompt when you want that agent to follow a specific protocol:

```text
# Agent: Coding Expert

## Execution Protocol
[Paste contents of steering/task-execution.md here]

## Role
...
```

#### Option 2: Load as Project Rules
Copy steering files into your AI tool's rules directory so they apply globally:

```bash
# Cursor
mkdir -p .cursor/rules
cp steering/*.md .cursor/rules/

# Kilo
mkdir -p .kilo/rules
cp steering/*.md .kilo/rules/
```

#### Option 3: Reference in Orchestrator
The Orchestrator can load steering files as context when dispatching tasks that require specific protocols:

```text
User: "Implement a secure payment feature with full validation."
Orchestrator: Loads steering/task-execution.md and steering/secure-coding.md as context, then dispatches to developer_agent and security_auditor.
```

### Available Steering Files

| File | Purpose |
|------|---------|
| `task-execution.md` | 6-phase execution protocol: Analyze, Design, Implement, Validate, Document, Deliver |
| `validation.md` | Validation principles for requirements, architecture, code, APIs, and deployments |
| `secure-coding.md` | Authentication, input validation, data protection, error handling, and dependency security |
| `workflow-orchestration.md` | Patterns for coordinating multi-agent workflows |
| `collaboration.md` | Guidelines for agent-to-agent communication and context sharing |
| `development-principles.md` | Core software engineering principles and best practices |
| `technical-writing.md` | Standards for documentation, API specs, and inline comments |
| `version-control.md` | Git workflow, commit conventions, and branch management |
| `implementation-pitfalls.md` | Common mistakes and anti-patterns to avoid |

### Pro Tip
Steering files are designed to be **tool-agnostic**. Use them to standardize how agents execute tasks regardless of whether you're using Cursor, Claude, Copilot, Kilo, Cline, or Windsurf.

---

## FAQ

**Q: Which agent should I start with?**
- For complex projects, start with `orchestrator.md`. For solo work or simple tasks, use `general_engineer.md`.

**Q: Can I use multiple agents at once?**
- Yes. Use the Orchestrator to coordinate multiple agents. In chat-based tools, load one agent per conversation.

**Q: Are these agents free to use?**
- Yes. The agent definitions are open source. You only pay for the underlying AI tool usage.

**Q: Can I modify agents for my project?**
- Yes. Feel free to customize agents to match your tech stack, coding standards, and domain requirements.

**Q: How do I verify agents are formatted correctly?**
- Run `python scripts/validate_agents.py` locally. This checks required sections, headers, and file completeness.

**Q: Do agents work offline?**
- No. Agents are prompts for AI tools and require an active connection to the tool's model.

**Q: Can I use agents with multiple tools?**
- Yes. Agent `.md` files are tool-agnostic and can be loaded into Cursor, Claude, Copilot, Kilo, Cline, Windsurf, and others.

**Q: How do I add a new agent?**
- Create a new `.md` file in `agents/` following the existing format: system prompt header, Role, Task, Output Format, and Input sections.

---

## Troubleshooting

### Agent Not Loading
- **Check file format**: Ensure the `.md` file is valid markdown.
- **Check file location**: Verify the file is in the correct directory for your tool.
- **Restart the tool**: Some tools need a restart to pick up new rules.

### Agent Giving Generic Responses
- **Ensure strict mode**: All agents start with `# SYSTEM PROMPT` and strict execution rules.
- **Provide specific input**: Generic input leads to generic output.
- **Check file integrity**: Make sure the full file was copied, not just part of it.

### Multiple Agents Conflict
- **Use Orchestrator**: Let the Orchestrator coordinate multiple agents.
- **Load one at a time**: In chat-based tools, load one agent per conversation.
- **Clear instructions**: Explicitly state which agent to use when.

### CI Validation Failing
- **Check Python version**: Requires Python 3.11+
- **Install PyYAML**: `pip install pyyaml`
- **Run locally first**: `python scripts/validate_agents.py` to see exact errors

### Agent Output Is Too Long
- **Use structured output**: All agents define an output format; ask them to respect it.
- **Break into subtasks**: Let the Orchestrator split large tasks instead of one giant output.
- **Specify constraints**: Add length or section limits to your task input.

### Tool-Specific Issues

#### Cursor
- Rules may not load if the `.cursor/rules/` directory is missing or misnamed.
- Ensure files have `.md` extension.

#### Claude Projects
- Large agent files may need to be split into multiple project knowledge files.
- Use the Instructions field for the primary agent; upload others as knowledge.

#### GitHub Copilot
- `.github/copilot-instructions.md` must be at the repo root.
- Copilot may not reload automatically; restart VS Code after changes.

#### Kilo
- Use `.kilo/rules/*.md` for workspace rules.
- Kilo supports model selection per agent in `.kilo/config.json` or `.kilo.json`.

#### Windsurf
- Rules go in `.windsurf/rules/` at the project root.
- Global rules apply across all projects.

### Validation Errors

**"Unrecognized format"**
- The file does not start with `# SYSTEM PROMPT` and lacks YAML frontmatter.
- Ensure the agent header matches the standard format.

**"Missing required section"**
- Add the missing section: `Role`, `Task`, `Output Format`, `Input`.

**"Filename does not match agent name"**
- Rename the file to match the agent name in the frontmatter or header.

---

## Quick Reference Card

| Tool | Best Location | File Format | Auto-load? |
|------|---------------|-------------|------------|
| GitHub Copilot | `.github/copilot-instructions.md` | Markdown | Yes |
| Cline | `.cline/instructions.md` | Markdown | Maybe |
| Cursor | `.cursor/rules/*.md` | Markdown | Yes |
| Claude Projects | Upload / Instructions | Markdown | Yes |
| ChatGPT GPTs | Instructions field | Markdown | Yes |
| Windsurf | `.windsurf/rules/*.md` | Markdown | Yes |
| Kilo | `.kilo/rules/*.md` | Markdown | Yes |

---

## Need Help?

- **Getting started?** See [README.md](../README.md).
- **Agent details?** See [docs/agents.md](../docs/agents.md).
- **Adding agents?** See [CONTRIBUTING.md](../CONTRIBUTING.md).
- **Validation issues?** Run `python scripts/validate_agents.py`.
