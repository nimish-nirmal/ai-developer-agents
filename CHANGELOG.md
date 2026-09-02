# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-09-02

### Added
- **3 new agents**:
  - `general_engineer.md` — End-to-end solo engineer for any task
  - `debugger.md` — Root cause analysis and minimal bug fixes
  - `refactoring_specialist.md` — Legacy code modernization and technical debt reduction
- **Ponytail Decision Ladder** added to `developer_agent.md`, `code_reviewer.md`, and `architecture_reviewer.md` to prevent over-engineering and bloat.
- **2 new specialized agents**:
  - `cyber_security_expert.md` — Offensive security, penetration testing, threat hunting, and hardening
  - `business_documentation_specialist.md` — Marketing, sales docs, PPTs, presentations, and content scraping
- **Multi-agent workflow examples** in README showing how to use multiple AI tools (Cursor, Copilot, Kilo, Claude) together.
- **Expanded usage guide** (`docs/usage.md`) with detailed instructions for Kiro, Kilo, GitHub Copilot, Cline, Cursor, Claude Projects, ChatGPT, and Windsurf.
- **Expanded agent reference** (`docs/agents.md`) with beginner-friendly descriptions, key concepts, and workflow examples.

### Changed
- Updated `orchestrator.md` to dispatch to all 20 agents.
- Updated README.md with Mermaid diagram, status badges, and expanded examples.
- Updated all documentation to reference the full 20-agent suite.

## [0.1.0] - 2026-08-20

### Added
- Initial release of the AI Developer Agents suite.
- Orchestrator agent for central task coordination.
- 13 specialized subagents:
  - Code Generator (`developer_agent.md`)
  - Test Writer (`test_writer.md`)
  - Documentation Creator (`document_creator.md`)
  - Code Reviewer (`code_reviewer.md`)
  - Architecture Reviewer (`architecture_reviewer.md`)
  - Database Expert (`database_expert.md`)
  - Security Auditor (`security_auditor.md`)
  - DevOps Reviewer (`devops_reviewer.md`)
  - Performance Analyst (`performance_analyst.md`)
  - API Specialist (`api_specialist.md`)
  - Frontend Reviewer (`frontend_reviewer.md`)
  - Integration Reviewer (`integration_reviewer.md`)
  - IoT Protocol Specialist (`iot_protocol_specialist.md`)
- CI workflow for agent validation (`.github/workflows/lint-agents.yml`).
- Validation script (`scripts/validate_agents.py`).
- Issue and PR templates.
- Comprehensive README with quickstart and example workflow.
