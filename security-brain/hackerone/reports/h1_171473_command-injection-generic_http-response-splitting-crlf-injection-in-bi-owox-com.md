---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '171473'
original_report_id: '171473'
title: HTTP Response Splitting(CRLF injection) in bi.owox.com
weakness: Command Injection - Generic
team_handle: owox
created_at: '2016-09-23T15:19:39.122Z'
disclosed_at: '2016-12-20T20:35:20.542Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- command-injection-generic
---

# HTTP Response Splitting(CRLF injection) in bi.owox.com

## Metadata

- HackerOne Report ID: 171473
- Weakness: Command Injection - Generic
- Program: owox
- Disclosed At: 2016-12-20T20:35:20.542Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found a CRLF injection vulnerability in bi.owox.com
> More about HTTP response splitting https://www.owasp.org/index.php/Testing_for_HTTP_Splitting/Smuggling_(OTG-INPVAL-016)

**POC (Burp)** > Adding a new header with ```%0d%0a```

{F122461}


Regards,
 Florin

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
