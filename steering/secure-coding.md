# Secure Coding Guidelines

## Authentication & Authorization
- Implement authentication by default
- Use established authentication frameworks
- Never create custom authentication schemes
- Implement proper session management
- Use multi-factor authentication where applicable

## Input Validation
- Never trust user input
- Implement input validation and sanitization
- Use parameterized queries for database operations
- Validate file uploads and restrict file types
- Implement rate limiting for APIs

## Data Protection
- Encrypt sensitive data at rest and in transit
- Use strong encryption algorithms
- Implement proper key management
- Never store secrets in code or configuration files
- Use secure communication protocols (HTTPS/TLS)

## Error Handling & Logging
- Implement comprehensive error handling
- Don't expose sensitive information in error messages
- Log security-relevant events
- Implement proper log retention policies
- Monitor for suspicious activities

## Dependencies & Libraries
- Keep dependencies updated
- Use vulnerability scanning tools
- Minimize third-party dependencies
- Choose libraries with active maintenance
- Review security advisories regularly

## Code Quality
- Follow secure coding standards
- Implement code reviews
- Use static analysis tools
- Write comprehensive tests
- Document security considerations
