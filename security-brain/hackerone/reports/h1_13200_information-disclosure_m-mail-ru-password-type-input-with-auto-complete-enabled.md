---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13200'
original_report_id: '13200'
title: (m.mail.ru)  Password type input with auto-complete enabled
weakness: Information Disclosure
team_handle: mailru
created_at: '2014-05-24T15:25:05.301Z'
disclosed_at: '2014-09-19T15:35:41.819Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# (m.mail.ru)  Password type input with auto-complete enabled

## Metadata

- HackerOne Report ID: 13200
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2014-09-19T15:35:41.819Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Password type input with auto complete enabled
Vulnerability description:
When a new name and password is entered in a form and the form is submitted, the browser asks if the password should be saved. Thereafter when the form is displayed, the name and password are filled in automatically or are completed as the name is entered. An attacker with local access could obtain the cleartext password from the browser cache.
This vulnerability affects     /cgi-bin/login. 

How to fix this vulnerability
The password auto-complete should be disabled in sensitive applications. 
To disable auto-complete, you may use a code similar to: 

<INPUT TYPE="password" AUTOCOMPLETE="off">

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
