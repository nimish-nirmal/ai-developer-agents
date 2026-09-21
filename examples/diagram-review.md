# Example: Architecture Diagram Review Workflow

This example demonstrates using diagram and Mermaid experts to review and improve technical documentation.

## Input

> **User Request:** "Review our system architecture diagram and improve the Mermaid flowchart in our README."

## Orchestrator Execution

### 1. Task Decomposition

- Review architecture diagram clarity (`diagram_expert`)
- Improve Mermaid syntax and layout (`mermaid_expert`)
- Validate against documentation standards (`document_creator`)

### 2. Dispatch & Aggregate

**Diagram Expert** evaluates:
- Notation consistency and standards compliance
- Label completeness and information density
- Color scheme and accessibility
- File format compatibility

**Mermaid Expert** reviews:
- Syntax correctness and valid grammar
- Node ordering and layout readability
- Subgraph organization and grouping
- Direction and flow clarity

**Document Creator** validates:
- Alignment with system design documents
- Consistency across documentation
- Audience appropriateness

### 3. Synthesis

The Orchestrator merges outputs into improved diagrams:
- Fixes syntax errors and invalid constructs
- Reorganizes nodes for left-to-right flow
- Adds missing labels and annotations
- Groups related components into subgraphs

## Output

Improved architecture diagrams with:
- Valid Mermaid syntax
- Clear left-to-right flow with grouped subgraphs
- Complete labeling and annotations
- Standards-compliant notation