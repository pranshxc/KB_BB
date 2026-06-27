---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13628'
original_report_id: '13628'
title: Password type input with auto-complete enabled
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-05-27T12:43:34.208Z'
disclosed_at: '2014-11-17T14:30:46.935Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password type input with auto-complete enabled

## Metadata

- HackerOne Report ID: 13628
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-11-17T14:30:46.935Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Vulnerability description :

When a new name and password is entered in a form and the form is submitted, the browser asks if the password should be saved. Thereafter when the form is displayed, the name and password are filled in automatically or are completed as the name is entered. An attacker with local access could obtain the cleartext password from the browser cache.

URL : https://www.irccloud.com/

Fixing this vulnerability :

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
