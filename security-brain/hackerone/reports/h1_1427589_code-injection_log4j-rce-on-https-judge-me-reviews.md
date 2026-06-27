---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1427589'
original_report_id: '1427589'
title: Log4j RCE on https://judge.me/reviews
weakness: Code Injection
team_handle: judgeme
created_at: '2021-12-15T10:30:12.893Z'
disclosed_at: '2021-12-21T08:57:29.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: https://judge.me/reviews
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# Log4j RCE on https://judge.me/reviews

## Metadata

- HackerOne Report ID: 1427589
- Weakness: Code Injection
- Program: judgeme
- Disclosed At: 2021-12-21T08:57:29.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:
CVE-2021-44228, also named Log4Shell or LogJam, is a Remote Code Execution (RCE) class vulnerability. If attackers manage to exploit it on one of the servers, they gain the ability to execute arbitrary code and potentially take full control of the system.
What makes CVE-2021-44228 especially dangerous is the ease of exploitation: even an inexperienced hacker can successfully execute an attack using this vulnerability. According to the researchers, attackers only need to force the application to write just one string to the log, and after that they are able to upload their own code into the application due to the message lookup substitution function.

Supporting Material/References:
Picture and Logs was Uploaded as a proof.

https://www.tenable.com/blog/cve-2021-44228-proof-of-concept-for-critical-apache-log4j-remote-code-execution-vulnerability

Remediation:
Update the log4j jar to 2.15 or 2.16

## Impact

Successful attack leads Arbitary Code Execution on the application

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
