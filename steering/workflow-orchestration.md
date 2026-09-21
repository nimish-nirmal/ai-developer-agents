# Workflow Orchestration Handler

## Purpose
Provide a platform-agnostic workflow orchestration pattern for multi-step tasks across any AI coding tool or agent runtime.

## Core Concepts

### Workflow Structure
A workflow consists of:
- **Inputs**: What is needed to start
- **Steps**: Ordered or conditional tasks
- **Outputs**: What is produced at each stage
- **Handoffs**: How output from one step becomes input to the next

### Step Design Principles
1. Each step should have a clear, single responsibility
2. Steps should be independently executable where possible
3. Steps should produce artifacts that can be reviewed
4. Steps should validate their inputs before proceeding

### Orchestration Patterns

#### Sequential Pipeline
Steps execute in order, each depending on the previous step's output.

#### Parallel Execution
Independent steps execute simultaneously, then merge results.

#### Conditional Branching
Steps execute based on decisions or conditions from previous steps.

#### Iterative Refinement
Steps repeat until a quality threshold is met.

## Execution Protocol

### Step 0: Load Context
- Read all inputs and constraints
- Identify available tools and capabilities
- Confirm scope and exclusions

### Step 1: Execute
- Run the step's task
- Produce artifacts
- Document decisions and assumptions

### Step 2: Validate
- Check outputs against acceptance criteria
- Identify gaps or issues
- Decide: proceed, fix, or escalate

### Step 3: Handoff
- Package outputs for the next step
- Document any context needed downstream
- Flag blockers or decisions needed

## State Management
- Track completion status for each step
- Preserve artifacts between steps
- Maintain a running summary of decisions
- Surface blockers immediately

## Quality Gates
Define explicit quality gates:
- **Pass**: Proceed to next step
- **Conditional**: Proceed with documented assumptions
- **Fail**: Stop and escalate

## Communication Protocol
When working in a multi-agent or multi-step workflow:
- Share findings, not raw data
- Use structured output formats
- Flag dependencies explicitly
- Surface blockers with suggested resolutions
