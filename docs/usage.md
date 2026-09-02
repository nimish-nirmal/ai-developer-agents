# Agent Usage Guide

This guide shows how to load and use the AI Developer Agents in popular AI coding tools and extensions.

## Table of Contents

1. [General Concept](#general-concept)
2. [Kiro](#kiro)
3. [Kilo](#kilo)
4. [GitHub Copilot & GitHub Tools](#github-copilot--github-tools)
5. [Cline](#cline)
6. [Cursor](#cursor)
7. [Claude Projects](#claude-projects)
8. [ChatGPT Custom GPTs](#chatgpt-custom-gpts)
9. [Windsurf](#windsurf)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)

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

## Kiro

Kiro is an AI coding assistant that supports custom instructions and project-level prompts.

### How to Load Agents

#### Option 1: Chat Instructions (Recommended for Quick Use)
1. Open Kiro in your project.
2. Click the **settings/instructions** icon in the chat panel.
3. Paste the full contents of the desired agent `.md` file.
4. Start chatting with the agent.

#### Option 2: Project Instructions (Recommended for Repeated Use)
1. Create a `.kiro/` directory in your project root.
2. Create a file like `.kiro/instructions.md`.
3. Paste the agent contents into this file.
4. Kiro will load these instructions automatically for your project.

#### Option 3: Global Instructions
1. Open Kiro settings.
2. Navigate to **Instructions** or **Custom Prompts**.
3. Paste the agent contents.
4. These instructions will apply to all projects.

### Recommended Setup
- Use **Option 2** (Project Instructions) for the Orchestrator agent.
- Use **Option 1** (Chat Instructions) for one-off specialist tasks.

### Example
```bash
# Create project instructions
mkdir -p .kiro
cp agents/orchestrator.md .kiro/instructions.md
```

Then open Kiro and start with: *"Build a REST API for a todo app with user authentication."*

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

---

## Quick Reference Card

| Tool | Best Location | File Format | Auto-load? |
|------|---------------|-------------|------------|
| Kiro | `.kiro/instructions.md` | Markdown | Yes (project) |
| Kilo | `.kilo/rules/*.md` | Markdown | Yes |
| GitHub Copilot | `.github/copilot-instructions.md` | Markdown | Yes |
| Cline | `.cline/instructions.md` | Markdown | Maybe |
| Cursor | `.cursor/rules/*.md` | Markdown | Yes |
| Claude Projects | Upload / Instructions | Markdown | Yes |
| ChatGPT GPTs | Instructions field | Markdown | Yes |
| Windsurf | `.windsurf/rules/*.md` | Markdown | Yes |

---

## Need Help?

- **Getting started?** See [README.md](../README.md).
- **Agent details?** See [docs/agents.md](../docs/agents.md).
- **Adding agents?** See [CONTRIBUTING.md](../CONTRIBUTING.md).
- **Validation issues?** Run `python scripts/validate_agents.py`.
