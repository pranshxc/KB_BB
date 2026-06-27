---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '503283'
original_report_id: '503283'
title: Real Time Error Logs Through Debug Information
weakness: Information Exposure Through Debug Information
team_handle: slack
created_at: '2019-02-28T11:01:26.220Z'
disclosed_at: '2019-04-11T09:15:29.815Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 95
asset_identifier: slack.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# Real Time Error Logs Through Debug Information

## Metadata

- HackerOne Report ID: 503283
- Weakness: Information Exposure Through Debug Information
- Program: slack
- Disclosed At: 2019-04-11T09:15:29.815Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**: During the assessment, I have found the debug URL on slackb.com which is disclosing the World Wide real time error logs of Slack users.

The information leaked includes the following:
1. User Device Information
2. Redacted Token
3. Client IP Address
4. Description
5. Session ID
6. Team ID
7. User ID
8. User Agent
9. Server Response
10. Timestamp
11. api_call
12. x-amz-cf-id
13. x-amz-id-2

And other user sensitive information.

**Steps to Reproduce**

Open below URL in browser and refresh it to see real time logs.

https://slackb.com/debug

The vulnerable domain here is slackb.com. I have confirmed this with Slack to report this on Hackerone and mention the vulnerable domain.

## Impact

By exploiting this vulnerabiliti​y, an attacker can dump the real-time logs and information gained through this is critical which includes the team ID, user ID and redacted token which allows attackers to gather information which can be used later in the attack lifecycle, in order to achieve more than they could if they didn’t get access to such information.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
