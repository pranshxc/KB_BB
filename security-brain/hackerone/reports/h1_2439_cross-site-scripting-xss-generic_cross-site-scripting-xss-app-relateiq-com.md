---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2439'
original_report_id: '2439'
title: Cross Site Scripting (XSS) - app.relateiq.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: relateiq
created_at: '2014-02-28T17:16:44.292Z'
disclosed_at: '2014-08-07T16:09:28.649Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross Site Scripting (XSS) - app.relateiq.com

## Metadata

- HackerOne Report ID: 2439
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: relateiq
- Disclosed At: 2014-08-07T16:09:28.649Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found a XSS vulnerability in relateiq.com !
1. Go to https://app.relateiq.com/ and click "Register as a new user"
2. Agree the terms and click Continue. Now choose to connect to MS exchange (Microsoft Exchange
Click to connect MS Exchange or Office365)
3.Now enter a random email and click "Connect email"
4. You will receive a error message and 2 new inputs . In the email field put this dada@c.com"><img src=x onerror=alert(document.domain)>  and in the "Override Endpoint Address" put a random website (eg:google.com)
5.Now click on "Connect email" and you will see the XSS alert.

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
