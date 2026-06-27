---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1321407'
original_report_id: '1321407'
title: Stored XSS in Document Title
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localizejs
created_at: '2021-08-27T14:00:58.288Z'
disclosed_at: '2021-09-27T14:00:01.507Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 120
asset_identifier: app.localizestaging.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Document Title

## Metadata

- HackerOne Report ID: 1321407
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localizejs
- Disclosed At: 2021-09-27T14:00:01.507Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary :

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS.

Vulnerable URL : https://app.localizestaging.com/documents

Payload XSS : 
"><img src=x onerror=alert(document.domain)> 

Step to Reproduces :
1. Login to your account
2. Create Project
3. What are you translating? (select documents)
4. Upload Document
5. Input XSS payload in Document Title = "><img src=x onerror=alert(document.domain)> 
6. Save it
7. XSS triggered

## Impact

Can steal Cookie, Can run javascript code, and get information sensitive

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
