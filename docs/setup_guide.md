# SOC Project: Automated Threat Detection & Incident Response

## Overview
This project sets up a Security Operations Center (SOC) using Splunk and Wazuh, leveraging MITRE ATT&CK for threat detection and automated incident response in cloud and hybrid environments.

## Table of Contents
1. Introduction
2. Prerequisites
3. Setup Guide
#### Splunk Add-ons & Apps
- Install Splunk Add-on for AWS, Azure, and GCP to ingest cloud logs
- Install Splunk Security Essentials for guided security use cases
- Install MITRE ATT&CK App for Splunk for mapping and visualization

#### Splunk Data Onboarding
- Configure HTTP Event Collector (HEC) for log ingestion
- Use Universal Forwarder for on-prem log collection
- Validate data sources in Splunk index

#### Splunk Correlation Searches & Alerts
- Create correlation searches for multi-stage attack detection (e.g., brute force + privilege escalation)
- Example SPL for brute force:
  `index=cloud_logs "authentication failure" | stats count by src_ip, user | where count > 5`
- Set up email, Slack, or SOAR integration for alerting

#### Splunk SOAR (Automation)
- Integrate Splunk with SOAR (Security Orchestration, Automation, and Response)
- Example playbooks: auto-block IP, notify SOC team, enrich threat intelligence

#### Splunk Dashboards
- Build dashboards for MITRE ATT&CK coverage, incident trends, and cloud activity
- Use MITRE ATT&CK matrix visualization to show detection coverage
7. Dashboards & Reporting
8. Resources
#### Wazuh MITRE ATT&CK Integration
- Enable MITRE ATT&CK mapping in Wazuh configuration
- Use built-in rules and create custom rules for ATT&CK techniques
- Example: Detect credential dumping (T1003) and trigger active response

#### Wazuh Active Responses
- Configure automated responses (block IP, disable user, kill process)
- Integrate with Splunk for centralized alerting
## 1. Introduction
- Purpose: Detect, analyze, and respond to threats automatically.
#### Practical Steps
- AWS: Set up CloudTrail, configure S3 bucket, use Splunk Add-on for AWS
- Azure: Enable Azure Monitor, use Splunk Add-on for Microsoft Cloud Services
- GCP: Enable Audit Logging, use Splunk Add-on for Google Cloud Platform
## 2. Prerequisites
- Basic Linux/Networking knowledge
#### Example Data Sources
- Windows/Linux server logs
- Cloud authentication and activity logs
- Network/firewall logs
## 3. Setup Guide
### a. Splunk Installation
#### MITRE ATT&CK Mapping in Splunk
- Use MITRE ATT&CK App to map detections to ATT&CK techniques
- Example: Map brute force detection to T1110, privilege escalation to T1068
- Visualize coverage and gaps in ATT&CK matrix

#### MITRE ATT&CK Detection in Wazuh
- Use built-in MITRE rules for common techniques
- Create custom rules for environment-specific threats
- Example: Detect lateral movement (T1021) via suspicious remote logins

#### Reporting & Documentation
- Generate reports showing detected ATT&CK techniques and coverage
- Document detection logic and response actions for each technique

### b. Wazuh Installation
#### Example Automated Responses
- Auto-block IP addresses involved in brute force attacks
- Disable compromised user accounts
- Notify SOC team via email/Slack
- Enrich alerts with threat intelligence feeds

#### Testing & Validation
- Use Atomic Red Team to simulate ATT&CK techniques
- Validate detection and response workflows
### c. Cloud Log Integration
- Enable logging in AWS (CloudTrail), Azure (Monitor), GCP (Logging)
#### Dashboard Examples
- MITRE ATT&CK coverage matrix
- Incident timeline and trends
- Cloud activity overview

#### Scheduled Reports
- Weekly summary of detected techniques
- Incident response actions taken
- Deploy Wazuh agents on cloud/on-prem VMs
- Configure Splunk Add-ons for cloud log ingestion
- Enable MITRE mapping in Wazuh
- Create detection rules for ATT&CK techniques

## 6. Automated Incident Response
- Create Splunk alerts for suspicious activities
- Integrate Splunk with SOAR (optional)
- Configure Wazuh active responses (block IP, kill process)
- Test with simulated attacks (Atomic Red Team)

## 7. Dashboards & Reporting
- Build dashboards in Splunk/Wazuh
- Map detections to MITRE ATT&CK matrix
- Schedule automated reports

## 8. Resources
- Splunk Training: https://www.splunk.com/en_us/training.html
- Wazuh Docs: https://documentation.wazuh.com/current/index.html
- MITRE ATT&CK: https://attack.mitre.org/
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
