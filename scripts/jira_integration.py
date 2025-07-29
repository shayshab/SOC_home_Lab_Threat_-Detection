#!/usr/bin/env python3
"""
Jira Integration Script for SOC Project
Creates and manages Jira tickets from security alerts
"""

import requests
import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional

class JiraIntegration:
    def __init__(self, jira_url: str, username: str, api_token: str, project_key: str):
        """
        Initialize Jira integration
        
        Args:
            jira_url: Jira instance URL (e.g., https://company.atlassian.net)
            username: Jira username or email
            api_token: Jira API token
            project_key: Jira project key for creating tickets
        """
        self.jira_url = jira_url.rstrip('/')
        self.username = username
        self.api_token = api_token
        self.project_key = project_key
        self.session = requests.Session()
        self.session.auth = (username, api_token)
        self.session.headers.update({'Content-Type': 'application/json'})
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def create_security_incident(self, 
                                summary: str, 
                                description: str, 
                                severity: str = "Medium",
                                mitre_technique: Optional[str] = None,
                                source_ip: Optional[str] = None,
                                affected_user: Optional[str] = None) -> Optional[str]:
        """
        Create a security incident ticket in Jira
        
        Args:
            summary: Ticket summary
            description: Detailed description
            severity: Incident severity (Low, Medium, High, Critical)
            mitre_technique: MITRE ATT&CK technique ID
            source_ip: Source IP address
            affected_user: Affected username
            
        Returns:
            Jira ticket key (e.g., SEC-123) or None if failed
        """
        try:
            # Map severity to Jira priority
            priority_map = {
                "Low": "Low",
                "Medium": "Medium", 
                "High": "High",
                "Critical": "Highest"
            }
            priority = priority_map.get(severity, "Medium")
            
            # Build description with structured information
            full_description = f"""
{description}

**Security Details:**
- Severity: {severity}
- Detection Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
"""
            
            if mitre_technique:
                full_description += f"- MITRE ATT&CK Technique: {mitre_technique}\n"
            if source_ip:
                full_description += f"- Source IP: {source_ip}\n"
            if affected_user:
                full_description += f"- Affected User: {affected_user}\n"
            
            full_description += f"""
**Response Actions Required:**
- [ ] Investigate the incident
- [ ] Determine root cause
- [ ] Implement remediation
- [ ] Update detection rules if needed
- [ ] Document lessons learned

**Automated Response:**
This ticket was automatically created by the SOC monitoring system.
"""
            
            # Create Jira issue
            issue_data = {
                "fields": {
                    "project": {"key": self.project_key},
                    "summary": summary,
                    "description": full_description,
                    "issuetype": {"name": "Security Incident"},
                    "priority": {"name": priority},
                    "labels": ["soc-automated", "security-incident"]
                }
            }
            
            # Add custom fields if available
            if mitre_technique:
                issue_data["fields"]["customfield_mitre_technique"] = mitre_technique
            
            response = self.session.post(
                f"{self.jira_url}/rest/api/2/issue",
                data=json.dumps(issue_data)
            )
            
            if response.status_code == 201:
                issue_key = response.json()["key"]
                self.logger.info(f"Created Jira ticket: {issue_key}")
                return issue_key
            else:
                self.logger.error(f"Failed to create Jira ticket: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error creating Jira ticket: {str(e)}")
            return None
    
    def update_incident_status(self, issue_key: str, status: str, comment: str = "") -> bool:
        """
        Update incident status in Jira
        
        Args:
            issue_key: Jira ticket key
            status: New status (e.g., "In Progress", "Resolved")
            comment: Optional comment
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Get available transitions
            response = self.session.get(f"{self.jira_url}/rest/api/2/issue/{issue_key}/transitions")
            if response.status_code != 200:
                return False
            
            transitions = response.json()["transitions"]
            target_transition = None
            
            for transition in transitions:
                if status.lower() in transition["to"]["name"].lower():
                    target_transition = transition["id"]
                    break
            
            if not target_transition:
                self.logger.error(f"Status '{status}' not found in available transitions")
                return False
            
            # Perform transition
            transition_data = {
                "transition": {"id": target_transition}
            }
            
            if comment:
                transition_data["update"] = {
                    "comment": [{"add": {"body": comment}}]
                }
            
            response = self.session.post(
                f"{self.jira_url}/rest/api/2/issue/{issue_key}/transitions",
                data=json.dumps(transition_data)
            )
            
            if response.status_code == 204:
                self.logger.info(f"Updated {issue_key} status to {status}")
                return True
            else:
                self.logger.error(f"Failed to update status: {response.status_code}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error updating incident status: {str(e)}")
            return False
    
    def add_comment(self, issue_key: str, comment: str) -> bool:
        """
        Add comment to Jira ticket
        
        Args:
            issue_key: Jira ticket key
            comment: Comment text
            
        Returns:
            True if successful, False otherwise
        """
        try:
            comment_data = {"body": comment}
            
            response = self.session.post(
                f"{self.jira_url}/rest/api/2/issue/{issue_key}/comment",
                data=json.dumps(comment_data)
            )
            
            if response.status_code == 201:
                self.logger.info(f"Added comment to {issue_key}")
                return True
            else:
                self.logger.error(f"Failed to add comment: {response.status_code}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error adding comment: {str(e)}")
            return False
    
    def get_incident_details(self, issue_key: str) -> Optional[Dict[str, Any]]:
        """
        Get incident details from Jira
        
        Args:
            issue_key: Jira ticket key
            
        Returns:
            Incident details dictionary or None if failed
        """
        try:
            response = self.session.get(f"{self.jira_url}/rest/api/2/issue/{issue_key}")
            
            if response.status_code == 200:
                return response.json()
            else:
                self.logger.error(f"Failed to get incident details: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error getting incident details: {str(e)}")
            return None

def main():
    """Example usage of Jira integration"""
    
    # Load configuration from environment variables
    jira_url = os.getenv("JIRA_URL")
    username = os.getenv("JIRA_USERNAME")
    api_token = os.getenv("JIRA_API_TOKEN")
    project_key = os.getenv("JIRA_PROJECT_KEY", "SEC")
    
    if not all([jira_url, username, api_token]):
        print("Please set JIRA_URL, JIRA_USERNAME, and JIRA_API_TOKEN environment variables")
        return
    
    # Initialize Jira integration
    jira = JiraIntegration(jira_url, username, api_token, project_key)
    
    # Example: Create a security incident
    issue_key = jira.create_security_incident(
        summary="Brute Force Attack Detected",
        description="Multiple failed login attempts detected from IP address 192.168.1.100",
        severity="High",
        mitre_technique="T1110",
        source_ip="192.168.1.100",
        affected_user="admin"
    )
    
    if issue_key:
        print(f"Created incident: {issue_key}")
        
        # Example: Add a comment
        jira.add_comment(issue_key, "Automated response: IP address has been blocked")
        
        # Example: Update status
        jira.update_incident_status(issue_key, "In Progress", "Investigation started")

if __name__ == "__main__":
    main() 