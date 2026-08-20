# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-08-20

### Added
- Initial release of the AI Developer Agents suite.
- Orchestrator agent for central task coordination.
- 9 specialized subagents:
  - Code Generator
  - Test Writer
  - Documentation Creator
  - Code Reviewer
  - Architecture Reviewer
  - Database Expert
  - Security Auditor
  - DevOps Engineer
  - Performance Optimizer
- CI workflow for agent validation (`.github/workflows/lint-agents.yml`).
- Validation script (`scripts/validate_agents.py`).
- Issue and PR templates.
- Comprehensive README with quickstart and example workflow.
