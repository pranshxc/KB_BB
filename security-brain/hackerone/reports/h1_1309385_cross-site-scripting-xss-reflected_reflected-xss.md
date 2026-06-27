---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1309385'
original_report_id: '1309385'
title: Reflected XSS [██████]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-08-18T04:05:42.404Z'
disclosed_at: '2022-04-29T14:06:38.791Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS [██████]

## Metadata

- HackerOne Report ID: 1309385
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-29T14:06:38.791Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Reflected cross-site scripting (XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way. An attacker can execute JavaScript arbitrary code on the victim's session.
Steps To Reproduce

 Go to this URL:
https://█████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Impact

- Perform any action within the application that the user can perform.
- View any information that the user is able to view.
- Modify any information that the user is able to modify.
- Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.
- Steal user's cookie.

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
