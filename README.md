# SOC Project

This project sets up an Automated Threat Detection and Incident Response Framework using Splunk, Wazuh, MITRE ATT&CK, and Jira for cloud and hybrid environments.

## Structure
- docs/setup_guide.md: Step-by-step setup and learning guide
- docs/jira_setup_guide.md: Jira integration setup and configuration guide
- scripts/cloud_log_forwarding.sh: Example script for forwarding cloud logs
- scripts/jira_integration.py: Jira API integration for incident management
- splunk/detection_rules.conf: Example Splunk detection rules
- splunk/jira_alert_action.conf: Splunk alert actions for Jira integration
- splunk/bin/jira_alert_action.py: Splunk alert action script for Jira
- wazuh/mitre_rules.xml: Example Wazuh MITRE ATT&CK mapping rules
- wazuh/jira_active_response.xml: Wazuh active response for Jira integration
- wazuh/bin/jira_create_ticket: Wazuh active response script for Jira
- wazuh/bin/jira_create_ticket.py: Python script for Wazuh-Jira integration
- dashboards/: Example dashboard configs for Splunk, Wazuh, and Jira
- requirements.txt: Python dependencies for Jira integration

## How to Use
1. Follow `docs/setup_guide.md` to set up Splunk, Wazuh, and cloud log integration
2. Follow `docs/jira_setup_guide.md` to configure Jira integration for incident management
3. Use `scripts/cloud_log_forwarding.sh` to forward logs from AWS CloudTrail to Splunk
4. Import detection rules and dashboards into Splunk and Wazuh
5. Configure Jira integration for automated ticket creation
6. Test with simulated attacks and review dashboards and incident tickets

## Features
- **Automated Threat Detection**: Real-time monitoring with Splunk and Wazuh
- **MITRE ATT&CK Integration**: Standardized threat categorization and mapping
- **Cloud Security Monitoring**: Support for AWS, Azure, and GCP
- **Automated Incident Response**: IP blocking, user disabling, and other responses
- **Jira Integration**: Automated ticket creation and incident management
- **Comprehensive Dashboards**: Real-time monitoring and reporting
- **SOAR Capabilities**: Security Orchestration, Automation, and Response

## Resources
- Splunk: https://www.splunk.com/en_us/download.html
- Wazuh: https://documentation.wazuh.com/current/index.html
- MITRE ATT&CK: https://attack.mitre.org/
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
- Jira API: https://developer.atlassian.com/cloud/jira/platform/rest/v3/
