---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2058556'
original_report_id: '2058556'
title: Self XSS when sending HTML as a comment in the Deck app
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2023-07-09T13:22:14.905Z'
disclosed_at: '2024-01-18T10:33:42.483Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: nextcloud/deck
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS when sending HTML as a comment in the Deck app

## Metadata

- HackerOne Report ID: 2058556
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2024-01-18T10:33:42.483Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I hope you are doing well.

I found an XSS/HTML Injection Via Comments in Deck Cards.

Vulnerability Name :- XSS/HTML Injection Via Comments in Deck Cards

Vulnerability Description :- Hi Team , I found an XSS/HTML Injection Via Comments in Deck Cards, which leads to One time Malicious Script execution .
I performed my Testing on  Localhost Latest version of Nextcloud  27.0.0.8.

{F2481183}

Steps to Reproduce :- 1. Setup the Nextcloud Instance Locally.
2. After setting up locally --> login.
3. After that Go to Deck --> Create Cards --> Click on that card --> Go to comments.
4. Enter this payload in comments :- <a href=http://██████/dangling_markup/name.html><font size=100 color=red>You must click me</font></a><base target="
5. You can also use this --> <a href=http://███████/dangling_markup/name.html><font size=100 color=blue>You Hacked by BhaRat</font></a><base target="
6. Put this script in comments and click and send and Boom! you see the one time execution.
7. Attacker can easily found a way to make it persistent or execute their malicious script once.

## Impact

1. Malicious Script Execution.
2. If attacker can able to make it persistent --> it leads to cookie stealing and account takeover.

POC Attached

If you need further info I am here to help you.

Thanks and Regards,
BhaRat

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
