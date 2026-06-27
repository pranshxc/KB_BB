---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146093'
original_report_id: '146093'
title: 'WordPress Vulnerabilities: User Enumeration, Vulnerable Akismet Plugin, XML-RPC
  Interface available'
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-06-20T19:16:23.593Z'
disclosed_at: '2016-06-22T07:36:19.241Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# WordPress Vulnerabilities: User Enumeration, Vulnerable Akismet Plugin, XML-RPC Interface available

## Metadata

- HackerOne Report ID: 146093
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-06-22T07:36:19.241Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

1. User Enumeration:
It is possible to enumerate four  WordPress usernames (jancborchardt, jos, lukasreschke, frank). An attacker can use these username to carry out brute-force attack in order to forcefully authenticate.

2. Akismet Plugin(2.5.0-3.1.4) vulnerable to unauthenticated Stored Cross Site Scripting:
This vulnerability allows an attacker to post a comment on a WordPress site which will execute javascript in the WordPress admin console. This is a typical XSS vulnerability pattern and one of the attacks it enables would allow an attacker to steal a WordPress administrator’s cookies and gain administrative access to a WordPress website.

3. XML-RPC Interface available: The presence of xmlrpc.php can cause brute force amplification attack.
https://nextcloud.com/xmlrpc.php

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
