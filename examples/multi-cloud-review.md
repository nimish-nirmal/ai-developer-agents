# Example: Multi-Cloud Architecture Review Workflow

This example demonstrates using cloud expert agents to review and optimize a multi-cloud architecture.

## Input

> **User Request:** "Review our AWS and GCP architecture for cost, reliability, and security. We run EKS on AWS and GKE on GCP, with shared PostgreSQL on Cloud SQL."

## Orchestrator Execution

### 1. Task Decomposition

- Review AWS architecture (`aws_expert`)
- Review GCP architecture (`gcp_expert`)
- Evaluate cross-cloud reliability (`architecture_reviewer`)
- Identify cost optimizations (`performance_analyst`)
- Audit security posture (`security_auditor`)
- Review deployment strategy (`deployment_reviewer`)

### 2. Dispatch & Aggregate

**AWS Expert** reviews:
- EKS cluster configuration and node group sizing
- VPC, subnets, and security groups
- IAM roles and least-privilege gaps
- Cost optimization: Reserved Instances, Spot, storage tiers

**GCP Expert** reviews:
- GKE cluster configuration and autoscaling
- VPC firewall rules and private connectivity
- IAM roles and service account permissions
- Cost optimization: Committed Use Discounts, storage lifecycle

**Architecture Reviewer** evaluates:
- Multi-region or multi-zone strategy
- Cross-cloud networking and data consistency
- Disaster recovery and backup strategy
- Service limits and quotas

**Security Auditor** flags:
- Encryption at rest and in transit
- Audit logging completeness
- Compliance program alignment
- Network segmentation gaps

**Deployment Reviewer** checks:
- CI/CD pipeline design
- Rollback and disaster recovery procedures
- Artifact validation and bundle size
- Secrets management in deployment

### 3. Synthesis

The Orchestrator merges outputs into a prioritized improvement plan:
- Critical: Fix open security groups and missing encryption
- High: Implement cross-cloud failover and backup strategy
- Medium: Optimize costs with reserved capacity and storage tiers
- Low: Improve observability and alerting coverage

## Output

A complete multi-cloud architecture review with:
- AWS and GCP service alignment assessment
- Security and compliance findings
- Cost optimization recommendations
- Deployment and disaster recovery improvements