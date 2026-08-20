# Detailed Agent Reference

This guide explains each agent in plain language, what it does, when to use it, and what kind of input/output to expect.

## Table of Contents

1. [How to Use Agents](#how-to-use-agents)
2. [Agent Catalog](#agent-catalog)
3. [Agent Workflow Examples](#agent-workflow-examples)
4. [Tips for Beginners](#tips-for-beginners)

---

## How to Use Agents

### What You Need
- An AI-powered tool: Cursor, Claude, ChatGPT, GitHub Copilot, Windsurf, or any tool that accepts system prompts.
- The agent `.md` files from this repository.

### Basic Workflow
1. **Choose your entry point**: For most tasks, start with `orchestrator.md`. For focused tasks, you can use individual agents directly.
2. **Load the agent**: Copy the contents of the `.md` file into your AI tool's system prompt, instructions, or project rules.
3. **Provide your input**: Describe what you want to build, review, or analyze.
4. **Review the output**: The agent will return structured results based on its expertise.

### Pro Tip for Beginners
Start with the Orchestrator for everything. It will automatically call the right specialists for you. You only need to load individual agents if you want to do one specific task repeatedly.

---

## Agent Catalog

### Coordination

#### `orchestrator.md` — The Team Lead
**What it does:** Breaks big tasks into smaller pieces, sends each piece to the right specialist, and combines everything into a final result.

**When to use:** Always use this as your starting point. Give it a high-level task like "Build a todo app" or "Review my authentication code."

**Input:** A natural-language description of what you want to build or fix.

**Output:** A complete, integrated result—working code, documentation, tests, and recommendations.

---

### Design & Architecture

#### `architecture_reviewer.md` — System Designer
**What it does:** Evaluates how your system is structured. Checks if it can handle growth, if parts can fail safely, and if it follows good design principles.

**When to use:** When you're planning a new system or reviewing an existing architecture.

**Input:** Architecture diagrams, system specs, or descriptions of how components connect.

**Output:** An assessment covering scalability, reliability, disaster recovery, security, and cost—with prioritized recommendations.

**Key concepts it knows about:**
- **Scalability** — Can the system handle more users/data as it grows?
- **Reliability** — What happens when something breaks?
- **Availability** — How often is the system up and running?
- **Disaster Recovery** — How fast can you recover from a major failure?

#### `api_specialist.md` — API Designer
**What it does:** Reviews your API endpoints and specifications to make sure they follow REST standards, are consistent, and are easy to use.

**When to use:** When designing or reviewing REST APIs, OpenAPI specs, or API documentation.

**Input:** API endpoints, OpenAPI YAML/JSON files, or API implementation code.

**Output:** Assessment of API design quality, consistency across endpoints, schema validation issues, and recommendations.

**Key concepts it knows about:**
- **REST principles** — Standard ways to design web APIs
- **HTTP methods** — GET (read), POST (create), PUT (update), DELETE (remove)
- **Status codes** — 200 (success), 404 (not found), 500 (server error)
- **Pagination** — How to return large lists in chunks

#### `database_expert.md` — Database Designer
**What it does:** Designs efficient database schemas, optimizes slow queries, and plans how to update databases without downtime.

**When to use:** When designing a new database, optimizing slow queries, or planning schema migrations.

**Input:** SQL schemas, ORM models, query code, or data model descriptions.

**Output:** Schema definitions, migration scripts, index recommendations, and query optimizations.

**Key concepts it knows about:**
- **Normalization** — Organizing data to avoid duplication
- **Indexing** — Making searches faster
- **N+1 problem** — A common performance issue where too many small queries are run
- **Migrations** — Safely changing database structure over time

---

### Implementation

#### `developer_agent.md` — Code Writer
**What it does:** Writes production-ready code following your project's existing patterns and best practices.

**When to use:** When you need to implement a feature, fix a bug, or write new code.

**Input:** Feature requirements, existing code examples, project structure, and technology stack.

**Output:** Clean, working code with explanations of design decisions, testing strategy, and configuration needs.

**Key concepts it knows about:**
- **Design patterns** — Reusable solutions to common problems
- **Error handling** — Gracefully managing failures
- **Security best practices** — Preventing common vulnerabilities
- **Testing strategy** — How to verify the code works

---

### Quality & Review

#### `code_reviewer.md` — Code Inspector
**What it does:** Reviews code line-by-line to find bugs, security issues, performance problems, and maintainability concerns.

**When to use:** Before merging code, after writing new features, or when debugging mysterious issues.

**Input:** Pull request diffs, source code, or specific code snippets.

**Output:** Structured review with severity-ranked findings (Critical, Major, Minor) and suggested fixes.

**Key concepts it checks:**
- **Logical correctness** — Does the code do what it's supposed to?
- **Code smells** — Patterns that indicate deeper problems
- **Thread safety** — Can the code run safely at the same time?
- **Memory leaks** — Is memory being properly released?

#### `security_auditor.md` — Security Checker
**What it does:** Scans your system for security vulnerabilities, checks compliance with standards, and recommends fixes.

**When to use:** Before launch, after major changes, or when handling sensitive data (payments, user data, etc.).

**Input:** Architecture, source code, deployment configurations, or API specs.

**Output:** Security posture assessment, list of vulnerabilities with severity ratings, and prioritized remediations.

**Key concepts it checks:**
- **OWASP Top 10** — The 10 most common web security risks
- **Authentication & authorization** — Who can access what?
- **Input validation** — Preventing malicious data from causing harm
- **Encryption** — Protecting data in transit and at rest

#### `devops_reviewer.md` — Infrastructure Reviewer
**What it does:** Reviews your deployment setup, CI/CD pipelines, containers, and infrastructure code.

**When to use:** When setting up deployment, reviewing infrastructure changes, or optimizing operations.

**Input:** Dockerfiles, Kubernetes manifests, Terraform, CI/CD configs, or architecture diagrams.

**Output:** Infrastructure maturity assessment, deployment risks, monitoring gaps, and automation opportunities.

**Key concepts it checks:**
- **Containerization** — Packaging apps for consistent deployment
- **CI/CD** — Automating build, test, and deployment
- **Infrastructure as Code** — Managing infrastructure through code (Terraform, CloudFormation)
- **Observability** — Logging, metrics, and tracing

#### `performance_analyst.md` — Speed Optimizer
**What it does:** Analyzes how fast your system runs, finds bottlenecks, and suggests optimizations.

**When to use:** When your app feels slow, before launch, or when planning for scale.

**Input:** Application code, architecture, performance profiles, or SLA requirements.

**Output:** Performance baselines, identified bottlenecks, optimization recommendations, and load testing scenarios.

**Key concepts it analyzes:**
- **Throughput** — How many requests the system can handle per second
- **Latency** — How long each request takes (p50, p95, p99)
- **Bottlenecks** — The slowest parts of your system
- **Caching** — Storing frequently used data in memory for speed

#### `frontend_reviewer.md` — UI/UX Inspector
**What it does:** Reviews web interfaces for usability, accessibility, performance, and code quality.

**When to use:** When building or reviewing web UIs, React/Vue components, or mobile web apps.

**Input:** HTML, CSS, JavaScript/TypeScript code, React/Vue/Angular components, or design mockups.

**Output:** Frontend quality assessment with UX issues, accessibility gaps, performance problems, and code quality findings.

**Key concepts it checks:**
- **Accessibility (WCAG)** — Can people with disabilities use your app?
- **Responsive design** — Does it work on phones, tablets, and desktops?
- **Bundle size** — How much code does the browser download?
- **Browser compatibility** — Does it work in Chrome, Firefox, Safari?

#### `integration_reviewer.md` — System Connector
**What it does:** Reviews how different systems communicate with each other, checks for data consistency, and evaluates middleware setups.

**When to use:** When connecting multiple services, reviewing APIs between systems, or debugging data flow issues.

**Input:** Architecture diagrams, event schemas, integration code, or middleware configurations.

**Output:** Integration maturity assessment, coupling analysis, message/event issues, and observability recommendations.

**Key concepts it checks:**
- **Coupling** — How tightly connected are your systems?
- **Event-driven architecture** — Systems communicating via events
- **Idempotency** — Handling duplicate messages safely
- **Distributed tracing** — Tracking requests across multiple services

#### `iot_protocol_specialist.md` — IoT Expert
**What it does:** Reviews IoT architectures, protocol implementations (MQTT, OPCUA, Modbus), and edge computing setups.

**When to use:** When building IoT systems, connecting devices, or implementing edge computing solutions.

**Input:** IoT architecture, protocol definitions, device integration code, or MQTT/OPCUA/Modbus configurations.

**Output:** Protocol analysis, device integration assessment, edge processing recommendations, and reliability improvements.

**Key concepts it knows about:**
- **MQTT** — Lightweight messaging for IoT devices
- **OPC UA** — Industrial automation protocol
- **Modbus** — Serial communication protocol for industrial devices
- **Edge computing** — Processing data close to where it's generated

---

### Testing & Documentation

#### `test_writer.md` — Test Generator
**What it does:** Creates comprehensive test plans and test cases covering functional, security, performance, and edge cases.

**When to use:** After implementing a feature, when improving test coverage, or before a release.

**Input:** Requirements, API specs, feature details, or source code.

**Output:** Structured test cases, edge cases, negative scenarios, load test scenarios, and automation suggestions.

**Key concepts it covers:**
- **Unit tests** — Testing individual functions/methods
- **Integration tests** — Testing how components work together
- **E2E tests** — Testing complete user workflows
- **Edge cases** — Testing unusual or extreme inputs
- **Negative testing** — Testing what happens when things go wrong

#### `document_creator.md` — Technical Writer
**What it does:** Generates clear, structured technical documentation including HLD (High-Level Design), LLD (Low-Level Design), and API specifications.

**When to use:** When documenting a new system, writing design docs, or creating API documentation.

**Input:** Requirements, architecture notes, system designs, or API details.

**Output:** Structured technical documents with full traceability to requirements.

**Key concepts it produces:**
- **HLD (High-Level Design)** — Big-picture system design
- **LLD (Low-Level Design)** — Detailed component designs
- **API specifications** — Endpoint definitions, request/response formats
- **Data flow diagrams** — How data moves through the system

---

## Agent Workflow Examples

### Example 1: Building a REST API

**Your task:** "Build a REST API for a task management app."

**Orchestrator flow:**
1. `architecture_reviewer` — Designs the overall system structure
2. `api_specialist` — Validates the API design against REST standards
3. `developer_agent` — Implements the API endpoints
4. `database_expert` — Designs the database schema
5. `test_writer` — Creates tests for all endpoints
6. `document_creator` — Writes API documentation
7. `code_reviewer` — Reviews the implementation
8. `security_auditor` — Checks for vulnerabilities

**Result:** A complete, tested, documented, and secure REST API.

### Example 2: Reviewing Existing Code

**Your task:** "Review my authentication code for issues."

**Orchestrator flow:**
1. `code_reviewer` — Finds bugs and code quality issues
2. `security_auditor` — Checks for security vulnerabilities
3. `performance_analyst` — Identifies performance bottlenecks

**Result:** A prioritized list of issues with fixes.

---

## Tips for Beginners

### 1. Start Small
Don't try to build a massive system in one go. Start with a simple task like "Create a hello world API" and let the Orchestrator show you how it works.

### 2. Provide Good Input
The better your input, the better the output. Instead of "make an API," try "create a REST API for a todo app with user authentication using JWT and PostgreSQL."

### 3. Review Agent Outputs
Agents give you recommendations and code, but you should review everything before using it in production.

### 4. Iterate
If an agent's output isn't quite right, give it more specific feedback. For example: "The database schema looks good, but add an index on the email column."

### 5. Combine Agents
For complex projects, let the Orchestrator handle the workflow. For quick tasks, you can use individual agents directly (e.g., just `code_reviewer` for a quick review).

### 6. Learn from the Outputs
Each agent returns structured, educational output. Read through the recommendations—you'll learn about security patterns, performance optimization, and best practices just by using them.

### 7. Customize Agents
Feel free to modify the agent files to match your project's specific needs. Add your company's coding standards, tech stack preferences, or domain-specific requirements.

---

## Need Help?

- **Getting started?** See the main [README.md](../README.md) for installation and setup.
- **Adding new agents?** See [CONTRIBUTING.md](../CONTRIBUTING.md).
- **Found a bug?** Open an issue with details about what happened.
