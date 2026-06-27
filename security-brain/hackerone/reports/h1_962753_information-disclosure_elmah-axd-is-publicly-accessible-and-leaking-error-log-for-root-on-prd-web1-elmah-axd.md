---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '962753'
original_report_id: '962753'
title: Elmah.axd is publicly accessible and leaking  Error Log for ROOT on █████_PRD_WEB1
  █████████elmah.axd
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-08-19T19:58:18.726Z'
disclosed_at: '2020-09-03T17:22:07.322Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# Elmah.axd is publicly accessible and leaking  Error Log for ROOT on █████_PRD_WEB1 █████████elmah.axd

## Metadata

- HackerOne Report ID: 962753
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2020-09-03T17:22:07.322Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hello,
Security team, hope you are doing well. I found out that elmah.axd is publicly accessible on ████████ which is leaking error log which contain cookies and server code etc.

## Step-by-step Reproduction Instructions
1. Go to ██████elmah.axd and you will see the error logs.
2. Same issue on█████████/elmah.axd 

## Suggested Mitigation/Remediation Action:
Implement proper authentication on elmah.axd or forbidden access . For reference -
https://blog.elmah.io/elmah-security-and-allowremoteaccess-explained/
https://elmah.github.io/a/securing-error-log-pages/

## Impact

Attacker can get access to any employee account using the cookies which he found in error log and also he can dump for endpoints.

Please find an attachment of poc and  if  you need more information please let me know 
Best Regards,
Rudra16

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
