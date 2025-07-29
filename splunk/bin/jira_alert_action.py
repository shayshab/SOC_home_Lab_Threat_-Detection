#!/usr/bin/env python3
"""
Splunk Alert Action Script for Jira Integration
This script is called by Splunk when security alerts are triggered
"""

import sys
import os
import json
import logging
from datetime import datetime

# Add the scripts directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))

try:
    from jira_integration import JiraIntegration
except ImportError:
    print("Error: Could not import JiraIntegration. Make sure jira_integration.py is in the scripts directory.")
    sys.exit(1)

def setup_logging():
    """Setup logging for the alert action"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('/opt/splunk/var/log/splunk/jira_alert_action.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def parse_alert_data():
    """
    Parse alert data from Splunk
    Returns: Dictionary containing alert information
    """
    alert_data = {}
    
    # Read from stdin (Splunk passes alert data via stdin)
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                # Parse JSON data from Splunk
                data = json.loads(line)
                alert_data.update(data)
            except json.JSONDecodeError:
                # Handle non-JSON lines
                if '=' in line:
                    key, value = line.split('=', 1)
                    alert_data[key.strip()] = value.strip()
    
    return alert_data

def determine_severity(alert_data):
    """
    Determine incident severity based on alert data
    """
    # Check for severity indicators in the alert
    severity_indicators = {
        "Critical": ["critical", "emergency", "severe"],
        "High": ["high", "brute force", "privilege escalation", "credential dump"],
        "Medium": ["medium", "suspicious", "unusual"],
        "Low": ["low", "info", "notice"]
    }
    
    alert_text = json.dumps(alert_data).lower()
    
    for severity, indicators in severity_indicators.items():
        for indicator in indicators:
            if indicator in alert_text:
                return severity
    
    return "Medium"  # Default severity

def extract_mitre_technique(alert_data):
    """
    Extract MITRE ATT&CK technique from alert data
    """
    # Common MITRE technique mappings
    technique_mappings = {
        "brute force": "T1110",
        "credential dump": "T1003",
        "privilege escalation": "T1068",
        "lateral movement": "T1021",
        "persistence": "T1053",
        "defense evasion": "T1070"
    }
    
    alert_text = json.dumps(alert_data).lower()
    
    for keyword, technique in technique_mappings.items():
        if keyword in alert_text:
            return technique
    
    return None

def create_jira_ticket(alert_data):
    """
    Create Jira ticket from alert data
    """
    logger = setup_logging()
    
    try:
        # Get Jira configuration from environment or alert data
        jira_url = os.getenv("JIRA_URL") or alert_data.get("jira_url")
        username = os.getenv("JIRA_USERNAME") or alert_data.get("jira_username")
        api_token = os.getenv("JIRA_API_TOKEN") or alert_data.get("jira_api_token")
        project_key = os.getenv("JIRA_PROJECT_KEY", "SEC")
        
        if not all([jira_url, username, api_token]):
            logger.error("Missing Jira configuration. Please set JIRA_URL, JIRA_USERNAME, and JIRA_API_TOKEN")
            return None
        
        # Initialize Jira integration
        jira = JiraIntegration(jira_url, username, api_token, project_key)
        
        # Extract alert information
        summary = alert_data.get("summary", "Security Alert Detected")
        description = alert_data.get("description", "A security alert was triggered by the SOC monitoring system.")
        severity = determine_severity(alert_data)
        mitre_technique = extract_mitre_technique(alert_data)
        source_ip = alert_data.get("src_ip") or alert_data.get("source_ip")
        affected_user = alert_data.get("user") or alert_data.get("affected_user")
        
        # Create the Jira ticket
        issue_key = jira.create_security_incident(
            summary=summary,
            description=description,
            severity=severity,
            mitre_technique=mitre_technique,
            source_ip=source_ip,
            affected_user=affected_user
        )
        
        if issue_key:
            logger.info(f"Successfully created Jira ticket: {issue_key}")
            
            # Add additional context as comment
            context_comment = f"""
**Alert Context:**
- Alert Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
- Alert Source: Splunk SOC Monitoring
- Raw Alert Data: {json.dumps(alert_data, indent=2)}
"""
            jira.add_comment(issue_key, context_comment)
            
            return issue_key
        else:
            logger.error("Failed to create Jira ticket")
            return None
            
    except Exception as e:
        logger.error(f"Error creating Jira ticket: {str(e)}")
        return None

def main():
    """
    Main function - entry point for Splunk alert action
    """
    # Parse alert data from Splunk
    alert_data = parse_alert_data()
    
    if not alert_data:
        print("Error: No alert data received from Splunk")
        sys.exit(1)
    
    # Create Jira ticket
    issue_key = create_jira_ticket(alert_data)
    
    if issue_key:
        print(f"Jira ticket created: {issue_key}")
        sys.exit(0)
    else:
        print("Failed to create Jira ticket")
        sys.exit(1)

if __name__ == "__main__":
    main() 