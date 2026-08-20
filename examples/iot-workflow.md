# Example: IoT Edge Gateway Workflow

This example demonstrates how to use the AI Developer Agents suite for an IoT-focused project.

## Input

> **User Request:** "Design an IoT edge gateway that aggregates sensor data from Modbus devices, buffers it locally, and streams to cloud via MQTT."

## Orchestrator Execution

### 1. Task Decomposition

- Design edge gateway architecture (`architecture_reviewer`)
- Validate IoT protocol specifications (`iot_protocol_specialist`)
- Implement gateway service (`developer_agent`)
- Design time-series data schema (`database_expert`)
- Generate tests (`test_writer`)
- Create technical documentation (`document_creator`)
- Review code quality (`code_reviewer`)
- Audit security (`security_auditor`)
- Review DevOps/deployment (`devops_reviewer`)
- Analyze performance (`performance_analyst`)
- Review cloud integration (`integration_reviewer`)

### 2. Dispatch & Aggregate

**Architecture Reviewer** designs:
- Edge gateway with local buffering and cloud sync
- Failover strategy for network outages
- Device discovery and registration flow

**IoT Protocol Specialist** evaluates:
- Modbus polling strategy for sensor data
- MQTT topic structure and QoS levels
- Edge processing for data filtering/compression
- Protocol gateway for Modbus-to-MQTT translation

**Developer Agent** implements:
- Modbus device driver with polling scheduler
- MQTT client with buffered publishing
- Local SQLite storage for offline data
- Edge aggregation rules

**Database Expert** designs:
- Time-series schema for sensor readings
- Partitioning strategy for high-volume data
- Retention policies and downsampling

**Integration Reviewer** evaluates:
- Cloud ingestion API design
- Event schema consistency
- Retry and dead-letter queue patterns

**DevOps Reviewer** designs:
- Docker image for edge gateway
- OTA update mechanism
- Device monitoring and alerting

### 3. Synthesis

The Orchestrator merges outputs into a complete IoT edge gateway design with:
- Edge architecture with local buffering
- Modbus-to-MQTT protocol translation
- Time-series data model with retention policies
- Cloud integration with retry and DLQ
- OTA update and monitoring strategy

## Output

A complete IoT edge gateway design with implementation artifacts.
