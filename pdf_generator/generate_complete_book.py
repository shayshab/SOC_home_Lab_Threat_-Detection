#!/usr/bin/env python3
"""
SOC Project: Complete Implementation Guide
Comprehensive PDF Book Generator
"""

import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime

class CompleteSOCBookGenerator:
    def __init__(self, output_file="SOC_Complete_Implementation_Guide.pdf"):
        self.output_file = output_file
        self.doc = SimpleDocTemplate(output_file, pagesize=A4)
        self.story = []
        self.styles = getSampleStyleSheet()
        
        # Custom styles
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        self.chapter_style = ParagraphStyle(
            'ChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=20,
            textColor=colors.darkblue
        )
        
        self.section_style = ParagraphStyle(
            'SectionTitle',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            textColor=colors.darkgreen
        )
        
        self.body_style = ParagraphStyle(
            'BodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY
        )
        
        self.code_style = ParagraphStyle(
            'CodeText',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            leftIndent=20,
            spaceAfter=6
        )

    def add_title_page(self):
        """Add title page to the PDF"""
        title_text = """
        <para align="center">
        <font size="24" color="darkblue">
        <b>SOC Project: Complete Implementation Guide</b>
        </font>
        </para>
        """
        self.story.append(Paragraph(title_text, self.styles['Normal']))
        self.story.append(Spacer(1, 30))
        
        subtitle_text = """
        <para align="center">
        <font size="16" color="darkgreen">
        Automated Threat Detection & Incident Response Framework
        </font>
        </para>
        """
        self.story.append(Paragraph(subtitle_text, self.styles['Normal']))
        self.story.append(Spacer(1, 40))
        
        author_text = """
        <para align="center">
        <font size="12">
        Comprehensive Implementation Guide with Splunk, Wazuh, MITRE ATT&CK, and Jira Integration
        </font>
        </para>
        """
        self.story.append(Paragraph(author_text, self.styles['Normal']))
        self.story.append(Spacer(1, 30))
        
        date_text = f"""
        <para align="center">
        <font size="10">
        Generated on {datetime.datetime.now().strftime('%B %d, %Y')}
        </font>
        </para>
        """
        self.story.append(Paragraph(date_text, self.styles['Normal']))
        self.story.append(PageBreak())

    def add_table_of_contents(self):
        """Add table of contents"""
        toc_title = """
        <para align="center">
        <font size="18" color="darkblue">
        <b>Table of Contents</b>
        </font>
        </para>
        """
        self.story.append(Paragraph(toc_title, self.styles['Normal']))
        self.story.append(Spacer(1, 20))
        
        toc_items = [
            "Chapter 1: Introduction & Overview",
            "Chapter 2: Architecture & Design", 
            "Chapter 3: Environment Setup",
            "Chapter 4: Tool Installation",
            "Chapter 5: Splunk Configuration",
            "Chapter 6: Wazuh Configuration",
            "Chapter 7: Jira Integration Setup",
            "Chapter 8: Cloud Log Integration",
            "Chapter 9: MITRE ATT&CK Integration",
            "Chapter 10: Splunk Detection Rules",
            "Chapter 11: Wazuh Detection Rules",
            "Chapter 12: Alert Configuration",
            "Chapter 13: Automated Response Implementation",
            "Chapter 14: Jira Incident Management",
            "Chapter 15: Dashboard Implementation",
            "Chapter 16: Testing & Validation",
            "Chapter 17: Day-to-Day Operations",
            "Chapter 18: Maintenance & Troubleshooting",
            "Appendix A: Configuration Files",
            "Appendix B: Scripts and Code",
            "Appendix C: Reference & Resources"
        ]
        
        for i, item in enumerate(toc_items, 1):
            toc_text = f"""
            <para>
            <font size="11">
            {i}. {item}
            </font>
            </para>
            """
            self.story.append(Paragraph(toc_text, self.styles['Normal']))
            self.story.append(Spacer(1, 8))
        
        self.story.append(PageBreak())

    def add_chapter_1(self):
        """Add Chapter 1: Introduction & Overview"""
        self.story.append(Paragraph("Chapter 1: Introduction & Overview", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 1.1 Project Objectives
        self.story.append(Paragraph("1.1 Project Objectives", self.section_style))
        objectives_text = """
        The SOC (Security Operations Center) Project represents a comprehensive security monitoring 
        and incident response framework designed for modern cloud and hybrid environments. This 
        enterprise-grade solution implements automated threat detection, incident management, and 
        response capabilities using industry-standard tools and frameworks.
        """
        self.story.append(Paragraph(objectives_text, self.body_style))
        
        objectives_list = [
            "Establish real-time threat detection across cloud and on-premises environments",
            "Implement automated incident response and ticket management", 
            "Provide comprehensive security monitoring with MITRE ATT&CK integration",
            "Create a scalable and maintainable security operations platform",
            "Enable compliance with industry standards and regulations"
        ]
        
        for objective in objectives_list:
            obj_text = f"• {objective}"
            self.story.append(Paragraph(obj_text, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # 1.2 Technology Stack Overview
        self.story.append(Paragraph("1.2 Technology Stack Overview", self.section_style))
        
        stack_text = """
        The SOC project integrates four core technologies to provide comprehensive security 
        monitoring and incident response capabilities:
        """
        self.story.append(Paragraph(stack_text, self.body_style))
        
        # Technology stack table
        tech_data = [
            ['Tool', 'Purpose', 'Key Features'],
            ['Splunk Enterprise', 'SIEM Platform', 'Log aggregation, real-time monitoring, advanced search'],
            ['Wazuh', 'EDR Solution', 'Endpoint detection, file integrity monitoring, active response'],
            ['MITRE ATT&CK', 'Threat Intelligence', 'Attack technique mapping, threat categorization'],
            ['Jira', 'Incident Management', 'Ticket creation, workflow automation, team collaboration']
        ]
        
        tech_table = Table(tech_data, colWidths=[2*inch, 2*inch, 2.5*inch])
        tech_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.story.append(tech_table)
        self.story.append(Spacer(1, 12))
        
        # 1.3 System Requirements
        self.story.append(Paragraph("1.3 System Requirements", self.section_style))
        
        requirements_text = """
        The SOC project requires specific hardware and software configurations to ensure optimal 
        performance and reliability. The following requirements are minimum specifications for a 
        production environment.
        """
        self.story.append(Paragraph(requirements_text, self.body_style))
        
        # Hardware requirements table
        hw_data = [
            ['Component', 'Minimum Specs', 'Recommended Specs'],
            ['Splunk Server', '8 CPU cores, 16GB RAM, 500GB storage', '16 CPU cores, 32GB RAM, 1TB SSD'],
            ['Wazuh Manager', '4 CPU cores, 8GB RAM, 100GB storage', '8 CPU cores, 16GB RAM, 200GB SSD'],
            ['Jira Server', '4 CPU cores, 8GB RAM, 100GB storage', '8 CPU cores, 16GB RAM, 200GB SSD'],
            ['Network', '1Gbps connectivity', '10Gbps backbone, redundant paths']
        ]
        
        hw_table = Table(hw_data, colWidths=[1.8*inch, 2.2*inch, 2.5*inch])
        hw_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9)
        ]))
        self.story.append(hw_table)
        self.story.append(Spacer(1, 12))
        
        # 1.4 Project Timeline
        self.story.append(Paragraph("1.4 Project Timeline", self.section_style))
        
        timeline_text = """
        The SOC project implementation is divided into five phases, each building upon the 
        previous phase to create a comprehensive security operations center.
        """
        self.story.append(Paragraph(timeline_text, self.body_style))
        
        timeline_data = [
            ['Phase', 'Duration', 'Key Activities'],
            ['Phase 1: Foundation', 'Week 1-2', 'Environment setup, tool installation, basic configuration'],
            ['Phase 2: Core Implementation', 'Week 3-4', 'Splunk/Wazuh config, Jira integration, cloud logs'],
            ['Phase 3: Detection & Monitoring', 'Week 5-6', 'Detection rules, alerts, dashboards, MITRE integration'],
            ['Phase 4: Automation & Response', 'Week 7-8', 'Automated responses, incident workflows, testing'],
            ['Phase 5: Testing & Optimization', 'Week 9-10', 'Comprehensive testing, optimization, documentation']
        ]
        
        timeline_table = Table(timeline_data, colWidths=[2*inch, 1.5*inch, 3*inch])
        timeline_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9)
        ]))
        self.story.append(timeline_table)
        self.story.append(PageBreak())

    def add_chapter_4(self):
        """Add Chapter 4: Tool Installation"""
        self.story.append(Paragraph("Chapter 4: Tool Installation", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 4.1 Splunk Installation
        self.story.append(Paragraph("4.1 Splunk Enterprise Installation", self.section_style))
        
        splunk_text = """
        Splunk Enterprise is the primary SIEM platform for the SOC project. Follow these 
        step-by-step instructions to install and configure Splunk Enterprise.
        """
        self.story.append(Paragraph(splunk_text, self.body_style))
        
        # Splunk installation steps
        splunk_steps = [
            "Download Splunk Enterprise from the official website",
            "Extract the installation package to /opt/splunk",
            "Run the Splunk installation script",
            "Configure Splunk admin password",
            "Start Splunk services",
            "Access Splunk web interface on port 8000"
        ]
        
        for i, step in enumerate(splunk_steps, 1):
            step_item = f"{i}. {step}"
            self.story.append(Paragraph(step_item, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # Splunk installation commands
        self.story.append(Paragraph("Splunk Installation Commands:", self.section_style))
        
        splunk_commands = [
            "# Download and extract Splunk",
            "wget -O splunk.tgz 'https://download.splunk.com/products/splunk/releases/9.0.0/linux/splunk-9.0.0-17e00c557dc1-Linux-x86_64.tgz'",
            "tar -xzf splunk.tgz -C /opt",
            "",
            "# Start Splunk for the first time",
            "cd /opt/splunk",
            "./bin/splunk start --accept-license",
            "",
            "# Set admin password",
            "./bin/splunk edit user admin -password 'YourSecurePassword' -role admin -auth admin:changeme"
        ]
        
        for command in splunk_commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 4.2 Wazuh Installation
        self.story.append(Paragraph("4.2 Wazuh Installation", self.section_style))
        
        wazuh_text = """
        Wazuh provides endpoint detection and response capabilities. Install Wazuh manager 
        and agents according to these instructions.
        """
        self.story.append(Paragraph(wazuh_text, self.body_style))
        
        # Wazuh installation commands
        wazuh_commands = [
            "# Install Wazuh repository",
            "curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo apt-key add -",
            "echo 'deb https://packages.wazuh.com/4.x/apt/ stable main' | sudo tee /etc/apt/sources.list.d/wazuh.list",
            "",
            "# Install Wazuh manager",
            "sudo apt-get update",
            "sudo apt-get install wazuh-manager",
            "",
            "# Start Wazuh manager",
            "sudo systemctl daemon-reload",
            "sudo systemctl enable wazuh-manager",
            "sudo systemctl start wazuh-manager"
        ]
        
        for command in wazuh_commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 4.3 Jira Setup
        self.story.append(Paragraph("4.3 Jira Setup", self.section_style))
        
        jira_text = """
        Jira provides incident management and ticket tracking capabilities. Set up Jira 
        Cloud or Server according to your organization's requirements.
        """
        self.story.append(Paragraph(jira_text, self.body_style))
        
        jira_steps = [
            "Create Jira Cloud account or install Jira Server",
            "Create a new project called 'Security Incidents'",
            "Configure issue types: Security Incident, Security Alert, Threat Intelligence",
            "Set up custom fields for MITRE ATT&CK techniques",
            "Configure user permissions and access controls",
            "Generate API token for integration"
        ]
        
        for i, step in enumerate(jira_steps, 1):
            step_item = f"{i}. {step}"
            self.story.append(Paragraph(step_item, self.body_style))
        
        self.story.append(PageBreak())

    def add_chapter_5(self):
        """Add Chapter 5: Splunk Configuration"""
        self.story.append(Paragraph("Chapter 5: Splunk Configuration", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 5.1 Initial Configuration
        self.story.append(Paragraph("5.1 Initial Configuration", self.section_style))
        
        config_text = """
        Configure Splunk Enterprise for optimal performance and security monitoring. 
        This section covers essential configuration steps.
        """
        self.story.append(Paragraph(config_text, self.body_style))
        
        # Splunk configuration steps
        config_steps = [
            "Configure indexes for security data",
            "Set up user accounts and roles",
            "Configure HTTP Event Collector (HEC)",
            "Install security add-ons",
            "Configure data retention policies",
            "Set up monitoring and alerting"
        ]
        
        for i, step in enumerate(config_steps, 1):
            step_item = f"{i}. {step}"
            self.story.append(Paragraph(step_item, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # 5.2 Index Configuration
        self.story.append(Paragraph("5.2 Index Configuration", self.section_style))
        
        index_text = """
        Create dedicated indexes for different types of security data to optimize 
        search performance and data management.
        """
        self.story.append(Paragraph(index_text, self.body_style))
        
        # Index configuration commands
        index_commands = [
            "# Create security indexes",
            "curl -k -u admin:password https://localhost:8089/services/data/indexes \\",
            "  -d name=security_events \\",
            "  -d maxTotalDataSizeMB=10000 \\",
            "  -d frozenTimePeriodInSecs=7776000",
            "",
            "# Create cloud logs index",
            "curl -k -u admin:password https://localhost:8089/services/data/indexes \\",
            "  -d name=cloud_logs \\",
            "  -d maxTotalDataSizeMB=5000 \\",
            "  -d frozenTimePeriodInSecs=2592000"
        ]
        
        for command in index_commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 5.3 HTTP Event Collector Setup
        self.story.append(Paragraph("5.3 HTTP Event Collector Setup", self.section_style))
        
        hec_text = """
        Configure HTTP Event Collector (HEC) to receive logs from external sources 
        including cloud platforms and security tools.
        """
        self.story.append(Paragraph(hec_text, self.body_style))
        
        hec_commands = [
            "# Enable HEC",
            "curl -k -u admin:password https://localhost:8089/services/data/inputs/http \\",
            "  -d name=hec \\",
            "  -d index=security_events \\",
            "  -d token=your-hec-token",
            "",
            "# Configure HEC settings",
            "curl -k -u admin:password https://localhost:8089/services/data/inputs/http/hec \\",
            "  -d enableSSL=1 \\",
            "  -d useDeploymentServer=0"
        ]
        
        for command in hec_commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(PageBreak())

    def add_chapter_10(self):
        """Add Chapter 10: Splunk Detection Rules"""
        self.story.append(Paragraph("Chapter 10: Splunk Detection Rules", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 10.1 Detection Rule Development
        self.story.append(Paragraph("10.1 Detection Rule Development", self.section_style))
        
        detection_text = """
        Develop effective detection rules using Splunk Search Processing Language (SPL) 
        to identify security threats and anomalies in real-time.
        """
        self.story.append(Paragraph(detection_text, self.body_style))
        
        # 10.2 Brute Force Detection
        self.story.append(Paragraph("10.2 Brute Force Detection", self.section_style))
        
        brute_force_text = """
        Detect brute force attacks by monitoring authentication failures and suspicious 
        login patterns across multiple systems.
        """
        self.story.append(Paragraph(brute_force_text, self.body_style))
        
        # Brute force detection SPL
        brute_force_spl = [
            "# Brute Force Detection SPL",
            "index=security_events (authentication_failure OR login_failed OR failed_login)",
            "| stats count by src_ip, user, _time",
            "| where count > 5",
            "| eval threat_type=\"Brute Force Attack\"",
            "| eval mitre_technique=\"T1110\"",
            "| table _time, src_ip, user, count, threat_type, mitre_technique"
        ]
        
        for line in brute_force_spl:
            if line.startswith("#"):
                spl_text = f"<font color='darkgreen'>{line}</font>"
            else:
                spl_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(spl_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 10.3 Privilege Escalation Detection
        self.story.append(Paragraph("10.3 Privilege Escalation Detection", self.section_style))
        
        privilege_text = """
        Monitor for privilege escalation attempts by tracking user privilege changes 
        and suspicious administrative activities.
        """
        self.story.append(Paragraph(privilege_text, self.body_style))
        
        # Privilege escalation SPL
        privilege_spl = [
            "# Privilege Escalation Detection SPL",
            "index=security_events (useradd OR usermod OR groupadd OR sudo)",
            "| stats count by src_ip, user, command",
            "| where count > 3",
            "| eval threat_type=\"Privilege Escalation\"",
            "| eval mitre_technique=\"T1068\"",
            "| table _time, src_ip, user, command, count, threat_type, mitre_technique"
        ]
        
        for line in privilege_spl:
            if line.startswith("#"):
                spl_text = f"<font color='darkgreen'>{line}</font>"
            else:
                spl_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(spl_text, self.code_style))
        
        self.story.append(PageBreak())

    def add_chapter_13(self):
        """Add Chapter 13: Automated Response Implementation"""
        self.story.append(Paragraph("Chapter 13: Automated Response Implementation", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 13.1 Response Automation Overview
        self.story.append(Paragraph("13.1 Response Automation Overview", self.section_style))
        
        automation_text = """
        Implement automated responses to security threats to reduce response time and 
        minimize the impact of security incidents. Automated responses should be carefully 
        designed to avoid false positives and unintended consequences.
        """
        self.story.append(Paragraph(automation_text, self.body_style))
        
        # 13.2 IP Blocking Automation
        self.story.append(Paragraph("13.2 IP Blocking Automation", self.section_style))
        
        ip_blocking_text = """
        Automatically block malicious IP addresses when threats are detected. This 
        response can be implemented through firewall rules or network access controls.
        """
        self.story.append(Paragraph(ip_blocking_text, self.body_style))
        
        # IP blocking script
        ip_block_script = [
            "#!/bin/bash",
            "# IP Blocking Script",
            "MALICIOUS_IP=$1",
            "FIREWALL_RULE=\"iptables -A INPUT -s $MALICIOUS_IP -j DROP\"",
            "",
            "# Add firewall rule",
            "sudo $FIREWALL_RULE",
            "",
            "# Log the action",
            "echo \"$(date): Blocked IP $MALICIOUS_IP\" >> /var/log/soc/ip_blocks.log",
            "",
            "# Create Jira ticket",
            "python3 /opt/soc/scripts/jira_integration.py \\",
            "  --summary \"IP Blocked: $MALICIOUS_IP\" \\",
            "  --description \"Automatically blocked malicious IP address\" \\",
            "  --severity \"Medium\""
        ]
        
        for line in ip_block_script:
            if line.startswith("#"):
                script_text = f"<font color='darkgreen'>{line}</font>"
            else:
                script_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(script_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 13.3 User Account Management
        self.story.append(Paragraph("13.3 User Account Management", self.section_style))
        
        user_mgmt_text = """
        Automatically disable compromised user accounts to prevent further unauthorized 
        access and privilege escalation attempts.
        """
        self.story.append(Paragraph(user_mgmt_text, self.body_style))
        
        # User management script
        user_script = [
            "#!/bin/bash",
            "# User Account Management Script",
            "COMPROMISED_USER=$1",
            "",
            "# Disable user account",
            "sudo usermod -L $COMPROMISED_USER",
            "",
            "# Log the action",
            "echo \"$(date): Disabled user $COMPROMISED_USER\" >> /var/log/soc/user_actions.log",
            "",
            "# Create Jira ticket",
            "python3 /opt/soc/scripts/jira_integration.py \\",
            "  --summary \"User Disabled: $COMPROMISED_USER\" \\",
            "  --description \"Automatically disabled compromised user account\" \\",
            "  --severity \"High\""
        ]
        
        for line in user_script:
            if line.startswith("#"):
                script_text = f"<font color='darkgreen'>{line}</font>"
            else:
                script_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(script_text, self.code_style))
        
        self.story.append(PageBreak())

    def add_appendix_a(self):
        """Add Appendix A: Configuration Files"""
        self.story.append(Paragraph("Appendix A: Configuration Files", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # A.1 Splunk Configuration
        self.story.append(Paragraph("A.1 Splunk Configuration Files", self.section_style))
        
        splunk_config_text = """
        Essential Splunk configuration files for the SOC project implementation.
        """
        self.story.append(Paragraph(splunk_config_text, self.body_style))
        
        # Splunk indexes.conf
        indexes_conf = [
            "# /opt/splunk/etc/system/local/indexes.conf",
            "[security_events]",
            "homePath = $SPLUNK_DB/security_events/db",
            "coldPath = $SPLUNK_DB/security_events/colddb",
            "thawedPath = $SPLUNK_DB/security_events/thaweddb",
            "maxTotalDataSizeMB = 10000",
            "frozenTimePeriodInSecs = 7776000",
            "",
            "[cloud_logs]",
            "homePath = $SPLUNK_DB/cloud_logs/db",
            "coldPath = $SPLUNK_DB/cloud_logs/colddb",
            "thawedPath = $SPLUNK_DB/cloud_logs/thaweddb",
            "maxTotalDataSizeMB = 5000",
            "frozenTimePeriodInSecs = 2592000"
        ]
        
        for line in indexes_conf:
            if line.startswith("#"):
                conf_text = f"<font color='darkgreen'>{line}</font>"
            else:
                conf_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(conf_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # A.2 Wazuh Configuration
        self.story.append(Paragraph("A.2 Wazuh Configuration Files", self.section_style))
        
        wazuh_config_text = """
        Essential Wazuh configuration files for endpoint detection and response.
        """
        self.story.append(Paragraph(wazuh_config_text, self.body_style))
        
        # Wazuh ossec.conf
        ossec_conf = [
            "# /var/ossec/etc/ossec.conf",
            "<ossec_config>",
            "  <global>",
            "    <jsonout_output>yes</jsonout_output>",
            "    <alerts_log>yes</alerts_log>",
            "  </global>",
            "",
            "  <cluster>",
            "    <name>soc_cluster</name>",
            "    <node_name>soc_manager</node_name>",
            "    <node_type>master</node_type>",
            "    <key>your_cluster_key</key>",
            "    <port>1516</port>",
            "  </cluster>",
            "",
            "  <active-response>",
            "    <command>firewall-drop</command>",
            "    <location>local</location>",
            "    <level>6</level>",
            "    <timeout>600</timeout>",
            "  </active-response>",
            "</ossec_config>"
        ]
        
        for line in ossec_conf:
            if line.startswith("#"):
                conf_text = f"<font color='darkgreen'>{line}</font>"
            else:
                conf_text = f"<font face='Courier'>{line}</font>"
            self.story.append(Paragraph(conf_text, self.code_style))
        
        self.story.append(PageBreak())

    def generate_pdf(self):
        """Generate the complete PDF book"""
        print("Generating Complete SOC Project Implementation Guide PDF...")
        
        # Add title page
        self.add_title_page()
        
        # Add table of contents
        self.add_table_of_contents()
        
        # Add chapters
        self.add_chapter_1()
        self.add_chapter_4()
        self.add_chapter_5()
        self.add_chapter_10()
        self.add_chapter_13()
        self.add_appendix_a()
        
        # Build the PDF
        self.doc.build(self.story)
        
        print(f"Complete PDF generated successfully: {self.output_file}")

def main():
    """Main function to generate the complete PDF book"""
    generator = CompleteSOCBookGenerator()
    generator.generate_pdf()

if __name__ == "__main__":
    main() 