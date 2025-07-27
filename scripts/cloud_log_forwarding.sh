#!/bin/bash
# cloud_log_forwarding.sh
# Example script to forward AWS CloudTrail logs to Splunk via HEC (HTTP Event Collector)

# Set these variables
SPLUNK_HEC_URL="https://<splunk-server>:8088"
SPLUNK_HEC_TOKEN="<your-splunk-hec-token>"
AWS_REGION="us-east-1"

# Install AWS CLI if not present
if ! command -v aws &> /dev/null; then
    echo "AWS CLI not found. Installing..."
    pip install awscli
fi

# Download CloudTrail logs (example)
aws cloudtrail lookup-events --region $AWS_REGION > cloudtrail_events.json

# Send logs to Splunk
curl -k $SPLUNK_HEC_URL/services/collector/event \
    -H "Authorization: Splunk $SPLUNK_HEC_TOKEN" \
    -d @cloudtrail_events.json

echo "Logs forwarded to Splunk."
