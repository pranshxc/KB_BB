---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9148'
original_report_id: '9148'
title: XSS Reflected - https://www.stopthehacker.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: stopthehacker
created_at: '2014-04-22T16:57:52.359Z'
disclosed_at: '2014-08-08T18:06:03.181Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS Reflected - https://www.stopthehacker.com/

## Metadata

- HackerOne Report ID: 9148
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: stopthehacker
- Disclosed At: 2014-08-08T18:06:03.181Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi.

I want to report a Reflected xss vulnerability that I found in www.stopthehacker website and which can affect the safety of your users. This vulnerability allows an attacker to inject in web pages javascript content for sending malicious scripts to an unsuspecting user. This flaw can access any cookies, session tokens, or other sensitive information retained by victim's browser and used with that site. This flaw works only in IE browser.

Link: http://www.stopthehacker.com/?"><script>alert(document.cookie)</script>
Steps for reproduce this vulnerability: Open the link above in IE and you can see that my javascript function alert() was executed.

Regards,
Coltuneac Alexandru

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
