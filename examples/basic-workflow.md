# Example: Basic Feature Implementation Workflow

This example demonstrates how to use the AI Developer Agents suite to implement a simple feature end-to-end.

## Input

> **User Request:** "Add a password reset feature to the existing user authentication system."

## Orchestrator Execution

### 1. Task Decomposition

The Orchestrator identifies the following subtasks:
- Review existing auth architecture (`architecture_reviewer`)
- Validate API design for password reset endpoints (`api_specialist`)
- Implement password reset service (`developer_agent`)
- Design database schema for reset tokens (`database_expert`)
- Generate tests for the new feature (`test_writer`)
- Create documentation (`document_creator`)
- Review implementation (`code_reviewer`)
- Audit security (`security_auditor`)

### 2. Dispatch & Aggregate

**Architecture Reviewer** assesses the existing auth system and recommends:
- Stateless JWT-based reset tokens with short expiry
- Email delivery via existing notification service
- Rate limiting on reset endpoints

**API Specialist** validates the proposed endpoints:
- `POST /api/auth/password-reset/request`
- `POST /api/auth/password-reset/confirm`
- Ensures proper status codes and error responses

**Developer Agent** implements:
- `PasswordResetService` with token generation and validation
- Email integration with existing notification service
- Rate limiting middleware

**Database Expert** designs:
- `password_reset_tokens` table with `user_id`, `token_hash`, `expires_at`
- Index on `token_hash` for fast lookup
- Automatic cleanup job for expired tokens

**Test Writer** generates:
- Unit tests for token generation and validation
- Integration tests for the reset flow
- Negative tests for expired/invalid tokens
- Security tests for token brute-forcing

**Document Creator** generates:
- API specification for the new endpoints
- HLD section for password reset flow
- LLD for the `PasswordResetService`

**Code Reviewer** identifies:
- Missing input validation on email field
-建议 add rate limiting to prevent abuse
- Suggests adding audit logging for reset attempts

**Security Auditor** flags:
- Token should be hashed in database (not plaintext)
- Reset link should use HTTPS only
- Recommend adding CAPTCHA for abuse prevention

### 3. Synthesis

The Orchestrator merges all outputs into a cohesive implementation plan:
- Incorporates security recommendations (token hashing, HTTPS)
- Adds rate limiting and audit logging
- Ensures database schema supports cleanup job
- Validates test coverage meets 90% threshold

## Output

A complete implementation plan with:
- `src/services/password-reset.service.ts`
- `src/migrations/001_add_password_reset_tokens.ts`
- `src/middleware/rate-limiter.ts`
- `tests/unit/password-reset.service.test.ts`
- `tests/integration/password-reset.e2e.test.ts`
- `docs/api-spec.md` (updated)
- `docs/hld/authentication.md` (updated)
