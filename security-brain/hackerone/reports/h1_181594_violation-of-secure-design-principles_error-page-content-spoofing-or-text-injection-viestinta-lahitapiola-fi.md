---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181594'
original_report_id: '181594'
title: Error Page Content Spoofing or Text Injection (viestinta.lahitapiola.fi)
weakness: Violation of Secure Design Principles
team_handle: localtapiola
created_at: '2016-11-11T16:51:16.140Z'
disclosed_at: '2017-01-09T09:12:30.677Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- violation-of-secure-design-principles
---

# Error Page Content Spoofing or Text Injection (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181594
- Weakness: Violation of Secure Design Principles
- Program: localtapiola
- Disclosed At: 2017-01-09T09:12:30.677Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team!

I want to report a context spoofing or text injection at the new scope added [ viestinta.lahitapiola.fi ] 

#### Vulnerability Description: The new scope  allows users to inject any content on the 404 not found webpage

#### Vulnerable Location:
http://viestinta.lahitapiola.fi/!!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20
{F134122}


#### Fix & Mitigation:

Fix 404 error page to a new who not allow text content injection

Please let me know if more info needed,

Best Regards,
@ak1t4

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
