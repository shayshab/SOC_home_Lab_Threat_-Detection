# SOC Project

This project sets up an Automated Threat Detection and Incident Response Framework using Splunk, Wazuh, and MITRE ATT&CK for cloud and hybrid environments.

## Structure
- docs/setup_guide.md: Step-by-step setup and learning guide
- scripts/cloud_log_forwarding.sh: Example script for forwarding cloud logs
- splunk/detection_rules.conf: Example Splunk detection rules
- wazuh/mitre_rules.xml: Example Wazuh MITRE ATT&CK mapping rules
- dashboards/: Example dashboard configs for Splunk and Wazuh

## How to Use
1. Follow `docs/setup_guide.md` to set up Splunk, Wazuh, and cloud log integration
2. Use `scripts/cloud_log_forwarding.sh` to forward logs from AWS CloudTrail to Splunk
3. Import detection rules and dashboards into Splunk and Wazuh
4. Test with simulated attacks and review dashboards

## Resources
- Splunk: https://www.splunk.com/en_us/download.html
- Wazuh: https://documentation.wazuh.com/current/index.html
- MITRE ATT&CK: https://attack.mitre.org/
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
# SOC_home_Lab_Threat_-Detection
