# Jira Integration Setup Guide

## Overview
This guide explains how to integrate Jira with the SOC project for automated incident management and ticket creation.

## Prerequisites
- Jira instance (Cloud or Server)
- Jira API access token
- Python 3.6+ installed
- Splunk and/or Wazuh configured

## Table of Contents
1. Jira Configuration
2. Splunk Integration
3. Wazuh Integration
4. Dashboard Setup
5. Testing and Validation

## 1. Jira Configuration

### 1.1 Create Jira Project
1. Log into your Jira instance
2. Create a new project called "Security Incidents" with key "SEC"
3. Create issue types:
   - Security Incident
   - Security Alert
   - Threat Intelligence

### 1.2 Generate API Token
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Name it "SOC Integration"
4. Copy the token (you'll need this for configuration)

### 1.3 Configure Custom Fields (Optional)
Create custom fields for better incident tracking:
- MITRE ATT&CK Technique (Text field)
- Source IP (Text field)
- Affected User (Text field)
- Alert Source (Select field: Splunk, Wazuh)

## 2. Splunk Integration

### 2.1 Install Python Dependencies
```bash
pip install requests
```

### 2.2 Configure Environment Variables
```bash
export JIRA_URL="https://your-company.atlassian.net"
export JIRA_USERNAME="your-email@company.com"
export JIRA_API_TOKEN="your-api-token"
export JIRA_PROJECT_KEY="SEC"
```

### 2.3 Setup Splunk Alert Actions
1. Copy `splunk/bin/jira_alert_action.py` to your Splunk bin directory
2. Make it executable: `chmod +x jira_alert_action.py`
3. Configure `splunk/jira_alert_action.conf` with your Jira settings
4. Restart Splunk

### 2.4 Configure Splunk Alerts
In Splunk, create alerts that trigger Jira ticket creation:

```spl
# Example: Brute Force Detection Alert
index=cloud_logs "authentication failure" | stats count by src_ip, user | where count > 5
```

Configure the alert action to run the Jira script.

## 3. Wazuh Integration

### 3.1 Install Active Response Scripts
1. Copy `wazuh/bin/jira_create_ticket` to `/var/ossec/active-response/bin/`
2. Copy `wazuh/bin/jira_create_ticket.py` to `/var/ossec/active-response/bin/`
3. Make scripts executable:
   ```bash
   chmod +x /var/ossec/active-response/bin/jira_create_ticket
   chmod +x /var/ossec/active-response/bin/jira_create_ticket.py
   ```

### 3.2 Configure Wazuh Active Response
1. Add `wazuh/jira_active_response.xml` to your Wazuh configuration
2. Restart Wazuh manager:
   ```bash
   systemctl restart wazuh-manager
   ```

### 3.3 Test Active Response
```bash
# Test the active response manually
/var/ossec/active-response/bin/jira_create_ticket.py \
  --jira-url "https://your-company.atlassian.net" \
  --username "your-email@company.com" \
  --api-token "your-api-token" \
  --project-key "SEC" \
  --summary "Test Security Alert" \
  --description "This is a test alert" \
  --severity "Medium"
```

## 4. Dashboard Setup

### 4.1 Import Jira Dashboard
1. Import `dashboards/jira_dashboard.json` into Splunk
2. Configure data sources for Jira incident data
3. Set up data collection from Jira API

### 4.2 Configure Data Collection
Create a script to collect Jira data:

```python
# Example: Collect Jira incidents
python3 scripts/jira_integration.py --collect-incidents
```

## 5. Testing and Validation

### 5.1 Test Splunk Integration
1. Trigger a test alert in Splunk
2. Verify Jira ticket creation
3. Check ticket details and severity mapping

### 5.2 Test Wazuh Integration
1. Simulate a security event on a monitored endpoint
2. Verify Wazuh rule triggers
3. Confirm Jira ticket creation with proper details

### 5.3 Validate Dashboard
1. Check incident creation trends
2. Verify MITRE ATT&CK mapping
3. Test incident status updates

## 6. Advanced Configuration

### 6.1 Custom Severity Mapping
Modify `scripts/jira_integration.py` to customize severity mapping:

```python
priority_map = {
    "Critical": "Highest",
    "High": "High", 
    "Medium": "Medium",
    "Low": "Low"
}
```

### 6.2 Custom MITRE Mapping
Add custom MITRE ATT&CK technique mappings:

```python
technique_mappings = {
    "brute force": "T1110",
    "credential dump": "T1003",
    "privilege escalation": "T1068",
    "lateral movement": "T1021",
    "persistence": "T1053",
    "defense evasion": "T1070",
    "your_custom_technique": "T1234"
}
```

### 6.3 Automated Response Workflows
Configure automated responses based on Jira ticket status:

```python
# Example: Auto-block IP when ticket is created
if issue_key:
    # Block source IP
    block_ip(source_ip)
    # Add comment to Jira ticket
    jira.add_comment(issue_key, f"Automated response: IP {source_ip} has been blocked")
```

## 7. Troubleshooting

### 7.1 Common Issues
- **Authentication errors**: Check API token and username
- **Permission errors**: Verify Jira project permissions
- **Script execution errors**: Check Python dependencies and file permissions

### 7.2 Log Files
- Splunk: `/opt/splunk/var/log/splunk/jira_alert_action.log`
- Wazuh: `/var/ossec/logs/jira_active_response.log`

### 7.3 Debug Mode
Enable debug logging in `scripts/jira_integration.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

## 8. Security Considerations

### 8.1 API Token Security
- Store API tokens securely (use environment variables)
- Rotate tokens regularly
- Use least privilege principle

### 8.2 Network Security
- Use HTTPS for all Jira API communications
- Implement proper firewall rules
- Monitor API access logs

### 8.3 Data Privacy
- Ensure incident data is handled according to privacy policies
- Implement data retention policies
- Audit access to incident tickets

## 9. Maintenance

### 9.1 Regular Tasks
- Monitor Jira API usage limits
- Review and update MITRE mappings
- Clean up resolved tickets
- Update integration scripts

### 9.2 Performance Optimization
- Implement rate limiting for API calls
- Cache frequently accessed data
- Optimize dashboard queries

## 10. Resources
- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Splunk Alert Actions](https://docs.splunk.com/Documentation/Splunk/latest/AdvancedDev/ModAlertsIntro)
- [Wazuh Active Response](https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.html)
- [MITRE ATT&CK Framework](https://attack.mitre.org/) 