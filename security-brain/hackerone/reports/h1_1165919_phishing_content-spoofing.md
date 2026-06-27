---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165919'
original_report_id: '1165919'
title: Content Spoofing
weakness: Phishing
team_handle: reddit
created_at: '2021-04-15T17:33:22.741Z'
disclosed_at: '2021-10-21T19:49:17.133Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: s.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- phishing
---

# Content Spoofing

## Metadata

- HackerOne Report ID: 1165919
- Weakness: Phishing
- Program: reddit
- Disclosed At: 2021-10-21T19:49:17.133Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Vulnerability:
Content Spoofing or Text Injection
Description:
This vulnerability will reflect text on to the web page which is used to scam a victim to visit or send information to a malicious website. Because it is inside the domain and trusted web page, there is chances of scam. Open the Url and you will see it.
URL:   ==https://ads-api.reddit.com///ohhhhhhhhhhh%20we%20are%20facing%20a%20heavy%20traffic,%20please%20visit%20our%20following%20website%20https://www.attacker.com%20to%20learn%20more==
attachments :::
{F1266927}

Reference:
https://owasp.org/www-community/attacks/Content_Spoofing
Screenshot is attached as a POC.

similar reports ::

1-  https://hackerone.com/reports/841630
2- https://hackerone.com/reports/498562
3- https://hackerone.com/reports/327671

## Impact

It is used to scam victim and result will be dangerous.

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
