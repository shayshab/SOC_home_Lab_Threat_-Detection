#!/usr/bin/env python3
"""
Wazuh Active Response Script for Jira Integration
Creates Jira tickets when Wazuh detects security threats
"""

import argparse
import sys
import os
import logging
from datetime import datetime

# Add the scripts directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))

try:
    from jira_integration import JiraIntegration
except ImportError:
    print("Error: Could not import JiraIntegration. Make sure jira_integration.py is in the scripts directory.")
    sys.exit(1)

def setup_logging():
    """Setup logging for the Wazuh active response"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('/var/ossec/logs/jira_active_response.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Create Jira ticket from Wazuh alert')
    
    parser.add_argument('--jira-url', required=True, help='Jira instance URL')
    parser.add_argument('--username', required=True, help='Jira username')
    parser.add_argument('--api-token', required=True, help='Jira API token')
    parser.add_argument('--project-key', default='SEC', help='Jira project key')
    parser.add_argument('--summary', required=True, help='Ticket summary')
    parser.add_argument('--description', required=True, help='Ticket description')
    parser.add_argument('--severity', default='Medium', help='Incident severity')
    parser.add_argument('--mitre-technique', help='MITRE ATT&CK technique ID')
    parser.add_argument('--source-ip', help='Source IP address')
    parser.add_argument('--affected-user', help='Affected username')
    
    return parser.parse_args()

def main():
    """Main function"""
    logger = setup_logging()
    args = parse_arguments()
    
    try:
        # Initialize Jira integration
        jira = JiraIntegration(
            args.jira_url,
            args.username,
            args.api_token,
            args.project_key
        )
        
        # Create Jira ticket
        issue_key = jira.create_security_incident(
            summary=args.summary,
            description=args.description,
            severity=args.severity,
            mitre_technique=args.mitre_technique,
            source_ip=args.source_ip,
            affected_user=args.affected_user
        )
        
        if issue_key:
            logger.info(f"Successfully created Jira ticket: {issue_key}")
            
            # Add Wazuh context as comment
            context_comment = f"""
**Wazuh Alert Context:**
- Alert Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
- Alert Source: Wazuh Endpoint Detection
- Severity: {args.severity}
"""
            
            if args.mitre_technique:
                context_comment += f"- MITRE ATT&CK Technique: {args.mitre_technique}\n"
            if args.source_ip:
                context_comment += f"- Source IP: {args.source_ip}\n"
            if args.affected_user:
                context_comment += f"- Affected User: {args.affected_user}\n"
            
            jira.add_comment(issue_key, context_comment)
            
            print(f"Jira ticket created: {issue_key}")
            sys.exit(0)
        else:
            logger.error("Failed to create Jira ticket")
            print("Failed to create Jira ticket")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error creating Jira ticket: {str(e)}")
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 