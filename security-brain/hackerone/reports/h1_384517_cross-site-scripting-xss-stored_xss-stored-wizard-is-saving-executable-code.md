---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384517'
original_report_id: '384517'
title: XSS (stored) Wizard is saving executable code
weakness: Cross-site Scripting (XSS) - Stored
team_handle: rocket_chat
created_at: '2018-07-20T11:20:42.267Z'
disclosed_at: '2018-09-27T12:46:09.463Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS (stored) Wizard is saving executable code

## Metadata

- HackerOne Report ID: 384517
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: rocket_chat
- Disclosed At: 2018-09-27T12:46:09.463Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

issue: xss(stored)
Stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. The stored input is not correctly filtered. As a consequence, the malicious data will appear to be part of the web site and run within the user’s browser under the privileges of the web application.

poc:
url: https://imgsrcxonerrorprompt2.rocket.chat

## Impact

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

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
