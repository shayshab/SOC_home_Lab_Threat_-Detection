#!/usr/bin/env python3
"""
SOC Project: Complete Implementation Guide
PDF Book Generator
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

class SOCBookGenerator:
    def __init__(self, output_file="SOC_Project_Implementation_Guide.pdf"):
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
        
        # 1.4 Prerequisites
        self.story.append(Paragraph("1.4 Prerequisites", self.section_style))
        
        prereq_text = """
        Before beginning the SOC project implementation, ensure all prerequisites are met:
        """
        self.story.append(Paragraph(prereq_text, self.body_style))
        
        prereq_list = [
            "Administrative access to all servers and network infrastructure",
            "Valid licenses for Splunk Enterprise and Jira",
            "Cloud platform accounts with API access (AWS, Azure, GCP)",
            "Network diagrams and IP addressing scheme",
            "Security policies and compliance requirements documentation",
            "Team contact information and escalation procedures"
        ]
        
        for prereq in prereq_list:
            prereq_item = f"• {prereq}"
            self.story.append(Paragraph(prereq_item, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # 1.5 Project Timeline
        self.story.append(Paragraph("1.5 Project Timeline", self.section_style))
        
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
        self.story.append(Spacer(1, 12))
        
        # 1.6 Success Metrics
        self.story.append(Paragraph("1.6 Success Metrics", self.section_style))
        
        metrics_text = """
        The success of the SOC project implementation is measured through specific metrics 
        across detection performance, response efficiency, and operational excellence.
        """
        self.story.append(Paragraph(metrics_text, self.body_style))
        
        metrics_data = [
            ['Category', 'Metric', 'Target'],
            ['Detection Performance', 'Time to Detection (TTD)', '< 5 minutes'],
            ['Detection Performance', 'False Positive Rate', '< 10%'],
            ['Detection Performance', 'MITRE ATT&CK Coverage', '> 80%'],
            ['Response Efficiency', 'Time to Response (TTR)', '< 15 minutes'],
            ['Response Efficiency', 'Automated Response Success', '> 95%'],
            ['Operational Excellence', 'System Uptime', '> 99.5%'],
            ['Operational Excellence', 'Dashboard Response Time', '< 3 seconds']
        ]
        
        metrics_table = Table(metrics_data, colWidths=[2*inch, 2.5*inch, 1.5*inch])
        metrics_table.setStyle(TableStyle([
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
        self.story.append(metrics_table)
        self.story.append(Spacer(1, 12))
        
        # 1.7 Key Takeaways
        self.story.append(Paragraph("1.7 Key Takeaways", self.section_style))
        
        takeaways_list = [
            "The SOC project provides comprehensive security monitoring and incident response capabilities",
            "Four core tools work together: Splunk (SIEM), Wazuh (EDR), MITRE ATT&CK (intelligence), Jira (management)",
            "Proper planning and preparation are essential for successful implementation",
            "Security and compliance considerations must be addressed throughout the project",
            "Success metrics should be established and monitored throughout the implementation"
        ]
        
        for takeaway in takeaways_list:
            takeaway_item = f"• {takeaway}"
            self.story.append(Paragraph(takeaway_item, self.body_style))
        
        self.story.append(PageBreak())

    def add_chapter_2(self):
        """Add Chapter 2: Architecture & Design"""
        self.story.append(Paragraph("Chapter 2: Architecture & Design", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 2.1 SOC Architecture Overview
        self.story.append(Paragraph("2.1 SOC Architecture Overview", self.section_style))
        
        arch_text = """
        The SOC architecture is designed as a layered, modular system that provides comprehensive 
        security monitoring and incident response capabilities. The architecture follows security 
        best practices and enables scalability, maintainability, and operational efficiency.
        """
        self.story.append(Paragraph(arch_text, self.body_style))
        
        # Architecture principles
        self.story.append(Paragraph("Architecture Principles:", self.section_style))
        principles_list = [
            "Defense in Depth: Multiple layers of security controls",
            "Zero Trust: Verify every access attempt",
            "Modular Design: Independent component operation",
            "Scalability: Support for growth and expansion",
            "Security First: Built-in security controls"
        ]
        
        for principle in principles_list:
            principle_item = f"• {principle}"
            self.story.append(Paragraph(principle_item, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # 2.2 Data Flow Architecture
        self.story.append(Paragraph("2.2 Data Flow Architecture", self.section_style))
        
        dataflow_text = """
        The SOC data flow follows a structured pipeline from data collection through incident 
        response. Each component plays a specific role in the security monitoring ecosystem.
        """
        self.story.append(Paragraph(dataflow_text, self.body_style))
        
        # Data flow table
        flow_data = [
            ['Stage', 'Component', 'Function'],
            ['Data Collection', 'Cloud APIs, Log Sources', 'Gather security events and logs'],
            ['Data Processing', 'Splunk Indexers', 'Parse, index, and enrich data'],
            ['Analysis', 'Splunk Search Heads', 'Correlate and analyze security events'],
            ['Detection', 'Detection Rules', 'Identify security threats and anomalies'],
            ['Response', 'Wazuh Active Response', 'Automated threat response actions'],
            ['Management', 'Jira Integration', 'Incident tracking and workflow']
        ]
        
        flow_table = Table(flow_data, colWidths=[1.5*inch, 2*inch, 3*inch])
        flow_table.setStyle(TableStyle([
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
        self.story.append(flow_table)
        self.story.append(Spacer(1, 12))
        
        # 2.3 Network Architecture
        self.story.append(Paragraph("2.3 Network Architecture", self.section_style))
        
        network_text = """
        The network architecture provides secure communication between SOC components while 
        maintaining proper segmentation and access controls.
        """
        self.story.append(Paragraph(network_text, self.body_style))
        
        network_components = [
            "Security VLAN (VLAN 100): Dedicated network for SOC tools",
            "Management VLAN (VLAN 200): Administrative access to tools",
            "Data VLAN (VLAN 300): Data collection and processing",
            "DMZ: External-facing components with restricted access"
        ]
        
        for component in network_components:
            comp_item = f"• {component}"
            self.story.append(Paragraph(comp_item, self.body_style))
        
        self.story.append(PageBreak())

    def add_chapter_3(self):
        """Add Chapter 3: Environment Setup"""
        self.story.append(Paragraph("Chapter 3: Environment Setup", self.chapter_style))
        self.story.append(Spacer(1, 12))
        
        # 3.1 Server Preparation
        self.story.append(Paragraph("3.1 Server Preparation", self.section_style))
        
        prep_text = """
        Proper server preparation is essential for successful SOC implementation. This section 
        covers the step-by-step process for preparing your environment.
        """
        self.story.append(Paragraph(prep_text, self.body_style))
        
        # Step-by-step instructions
        steps = [
            "Update system packages and apply security patches",
            "Configure network interfaces and IP addressing",
            "Set up firewall rules and security groups",
            "Create dedicated user accounts for SOC tools",
            "Configure DNS resolution and time synchronization",
            "Install required system dependencies"
        ]
        
        for i, step in enumerate(steps, 1):
            step_item = f"{i}. {step}"
            self.story.append(Paragraph(step_item, self.body_style))
        
        self.story.append(Spacer(1, 12))
        
        # 3.2 Network Configuration
        self.story.append(Paragraph("3.2 Network Configuration", self.section_style))
        
        network_config_text = """
        Configure network settings to ensure proper communication between SOC components 
        and external data sources.
        """
        self.story.append(Paragraph(network_config_text, self.body_style))
        
        # Network configuration commands
        self.story.append(Paragraph("Network Configuration Commands:", self.section_style))
        
        commands = [
            "# Configure network interfaces",
            "sudo ip addr add 192.168.100.10/24 dev eth0",
            "sudo ip route add default via 192.168.100.1",
            "",
            "# Configure firewall rules",
            "sudo ufw allow 22/tcp",
            "sudo ufw allow 8000/tcp",
            "sudo ufw allow 1514/tcp",
            "sudo ufw enable"
        ]
        
        for command in commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(Spacer(1, 12))
        
        # 3.3 User Account Setup
        self.story.append(Paragraph("3.3 User Account Setup", self.section_style))
        
        user_text = """
        Create dedicated user accounts for SOC tools with appropriate permissions and 
        security controls.
        """
        self.story.append(Paragraph(user_text, self.body_style))
        
        user_commands = [
            "# Create SOC user account",
            "sudo useradd -m -s /bin/bash socadmin",
            "sudo usermod -aG sudo socadmin",
            "",
            "# Set up SSH key authentication",
            "sudo mkdir -p /home/socadmin/.ssh",
            "sudo chmod 700 /home/socadmin/.ssh",
            "sudo chown socadmin:socadmin /home/socadmin/.ssh"
        ]
        
        for command in user_commands:
            if command.startswith("#"):
                cmd_text = f"<font color='darkgreen'>{command}</font>"
            else:
                cmd_text = f"<font face='Courier'>{command}</font>"
            self.story.append(Paragraph(cmd_text, self.code_style))
        
        self.story.append(PageBreak())

    def generate_pdf(self):
        """Generate the complete PDF book"""
        print("Generating SOC Project Implementation Guide PDF...")
        
        # Add title page
        self.add_title_page()
        
        # Add table of contents
        self.add_table_of_contents()
        
        # Add chapters
        self.add_chapter_1()
        self.add_chapter_2()
        self.add_chapter_3()
        
        # Build the PDF
        self.doc.build(self.story)
        
        print(f"PDF generated successfully: {self.output_file}")

def main():
    """Main function to generate the PDF book"""
    generator = SOCBookGenerator()
    generator.generate_pdf()

if __name__ == "__main__":
    main() 