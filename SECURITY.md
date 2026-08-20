# Security Policy

## Reporting Security Vulnerabilities

We take security seriously. If you discover a security vulnerability in any
agent prompt or associated tooling, please report it responsibly.

**Do not** open a public issue for security vulnerabilities.

Instead, please email us at security@example.com with:
- A description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested remediation (if any)

We will acknowledge receipt within 48 hours and provide a detailed response
within 7 days.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Agent Prompt Security

When contributing new or updated agent prompts, please ensure:
- No secrets, API keys, or credentials are hardcoded
- No instructions that could lead to unsafe code generation
- Clear boundaries around system commands and file operations

## Dependencies

We recommend periodically scanning agent dependencies and associated
tooling with your organization's standard vulnerability scanners.
