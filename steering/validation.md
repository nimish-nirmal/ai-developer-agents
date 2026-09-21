# Validation Handler

## Purpose
Provide platform-agnostic validation patterns for requirements, architecture, code, and deployments.

## Validation Principles

### Requirements Validation
- Every requirement must trace to an explicit source
- Behavioral requirements describe observable behavior only
- Technology choices belong in constraints, not behavioral requirements
- No orphan requirements or unjustified orphan components

### Architecture Validation
- Every significant decision must cite evidence
- Evidence tiers: Authoritative → Validated → Community → Unverified
- Vague claims without authoritative sources must be challenged
- Every significant decision must document alternatives and trade-offs

### Code Validation
- Every new code path must have tests
- Every new permission or role must be justified
- State machines must have complete transition coverage
- SDK references must be verified against supported versions

### API Validation
- Multi-page behavior must be tested
- Boundary conditions must be explicit
- Invalid inputs must return proper client errors
- Pagination tokens must be validated for expiry and tampering

### Deployment Validation
- Artifacts must be validated for contents and size
- No unintended files in deployment packages
- Pre-deployment checklist must be complete
- Rollback procedure must be tested

## Scoring Model
Use dimension-based scoring where applicable:
- Score each dimension independently
- Apply weights if the context requires it
- Use thresholds: Excellent / Good / Conditional / Failed
- Escalate when score falls below the acceptable threshold

## Escalation Rules
Escalate when:
- Two or more valid approaches exist with significant trade-offs
- Requirements are ambiguous or contradictory
- User constraints conflict with best practices
- Overall assessment would fall below the minimum acceptable threshold

## Fix vs. Recommend Matrix
- Critical and High issues: fix autonomously when possible
- Medium and Low issues: recommend unless trivial to fix
- Document all fixes and recommendations explicitly
