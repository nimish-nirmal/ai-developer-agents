# Task Execution Handler

## Purpose
Provide a platform-agnostic task execution pattern that works across AI coding tools, IDEs, and agent runtimes.

## Execution Protocol

### Phase 1: Analyze
- Understand the requirements fully
- Identify the tech stack and constraints
- Note existing codebase patterns
- Determine the simplest viable solution

### Phase 2: Design
- Choose the simplest architecture that meets requirements
- Design data models and APIs
- Plan the implementation approach
- Identify test scenarios

### Phase 3: Implement
- Write clean, minimal code following existing patterns
- Include proper error handling and validation
- Add essential inline documentation

### Phase 4: Validate
- Write tests for critical paths
- Review for security vulnerabilities
- Check performance implications
- Verify accessibility requirements

### Phase 5: Document
- Write or update documentation
- Document API endpoints
- Add inline documentation for complex logic
- Include setup and deployment instructions

### Phase 6: Deliver
- Provide a complete, working solution
- Include all files with their paths
- Explain key design decisions
- Note any assumptions or constraints

## Decision Guidance
Before implementing, apply a simplicity check:
1. Is this actually needed?
2. Can existing code solve this?
3. Does the standard library cover it?
4. Can the platform handle this natively?
5. Does an existing dependency solve it?
6. Can this be a concise one-liner?
7. What is the smallest change that works?

## Safety Guards
Never skip:
- Input validation at trust boundaries
- Error handling that prevents data loss or crashes
- Security controls and accessibility requirements
- Any explicit user constraints
