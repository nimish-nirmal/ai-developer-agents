# Example: Git Workflow and CI Pipeline Review

This example demonstrates using the GitHub expert and pipeline manager to review version control and CI/CD workflows.

## Input

> **User Request:** "Review our Git branching strategy and CI/CD pipeline. We want to enforce branch protection, test coverage, and deployment gates before merging to main."

## Orchestrator Execution

### 1. Task Decomposition

- Review Git workflow and branching model (`github_expert`)
- Review CI/CD pipeline and deployment readiness (`pipeline_manager`)
- Validate branch protection and test gates (`devops_reviewer`)

### 2. Dispatch & Aggregate

**GitHub Expert** evaluates:
- Branching strategy fit for team size and release cadence
- Commit message conventions and history quality
- PR/MR workflow completeness
- Protection rules and merge strategy
- Signed commit enforcement and secret scanning

**Pipeline Manager** reviews:
- PR existence and review status before main integration
- Test coverage and test case creation for changed functionality
- CI/CD workflow completeness for changed scope
- Deployment artifact readiness and validation
- Pre-deployment checklist completion
- Rollback and recovery readiness

**DevOps Reviewer** validates:
- Build optimization and caching
- Deployment strategy (blue-green, canary, rolling)
- Monitoring and alerting setup
- Artifact validation and bundle size thresholds

### 3. Synthesis

The Orchestrator merges outputs into a governance improvement plan:
- Critical: Enforce branch protection and PR requirements
- High: Add test coverage gates and deployment artifact validation
- Medium: Improve commit message conventions and PR descriptions
- Low: Automate rollback procedures and incident response docs

## Output

A complete Git and CI/CD governance plan with:
- Branching strategy recommendations
- Branch protection rules and enforcement
- CI/CD workflow improvements
- Deployment readiness checklist
- Rollback and recovery procedures