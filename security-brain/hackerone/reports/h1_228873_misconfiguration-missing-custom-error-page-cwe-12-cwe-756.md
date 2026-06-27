---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228873'
original_report_id: '228873'
title: 'Misconfiguration: Missing Custom Error Page (CWE-12 & CWE-756)'
team_handle: portswigger
created_at: '2017-05-16T17:29:14.060Z'
disclosed_at: '2017-05-16T19:09:58.965Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
---

# Misconfiguration: Missing Custom Error Page (CWE-12 & CWE-756)

## Metadata

- HackerOne Report ID: 228873
- Weakness: 
- Program: portswigger
- Disclosed At: 2017-05-16T19:09:58.965Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi 
I found that custom errors for ```` http://portswigger.net ```` application framework `are not configured.,
so application vulnerable to CWE-756 & CWE-12
https://cwe.mitre.org/data/definitions/12.html
https://cwe.mitre.org/data/definitions/756.html
- Impact:

Default error pages gives detailed information about the error that occurred, and should not be used in production environments.

Attackers can leverage the additional information provided by a default error page to mount attacks targeted on the framework, database, or other resources used by the application.


- POC:

````   http://portswigger.net/%5c.../file  ````
{F185140}

thanks

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
