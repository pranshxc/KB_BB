---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411075'
original_report_id: '411075'
title: Abusing "Report as abuse" functionality to delete any user's post.
weakness: Business Logic Errors
team_handle: vanilla
created_at: '2018-09-18T13:14:58.687Z'
disclosed_at: '2020-01-18T15:05:43.433Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 160
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Abusing "Report as abuse" functionality to delete any user's post.

## Metadata

- HackerOne Report ID: 411075
- Weakness: Business Logic Errors
- Program: vanilla
- Disclosed At: 2020-01-18T15:05:43.433Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
Greetings!!

**Description:**
I would like to report a vulnerability that can be used to delete any user’s post by abusing “Report an abuse” function within application. After specific number of reports submitted to server, it automatically deletes that post of user.
Application has functionality where one user can report for abusive post or content of another user. An attacker can send multiple abuse report for the victim’s post from one account to delete user’s post. 
 
## Steps to reproduce:

1. Login with attacker's credentials in browser and victim’s credentials in incognito mode of browser 
2. Post some text or other content through victim’s account on his own wall.
3. Now open attacker’s account and goto victim’s wall or profile. You will see the content posted by victim. 
4. Set up any proxy intercepting tool with the browser (I’m using Burp Suite) and start intercepting requests
7. Click on “Flag” of victim’s post and select “Abuse”. Capture this request in Burpsuite and send to Intruder tab
8. Goto “Position” tab and select “clear”
9. Now goto Payload tab and select “Payload type” as “Null Payloads”
10. Under the payload options select “Continue indefinably”
11. Now goto “Options” tab and set number of threads “100”
12. Click on start attack. After 900 requests reload the page.
13. If post is still exist, wait for more payloads to be executed.
14. After specific number of successful payloads post will get deleted. 
15. You can verify with attacker’s as well as victim’s account also
 

Mitigations:
Application should also verify source of "Abusive flags". If requests are being submitted from one account, block the requests.

## Impact

An attacker can use this vulnerability to delete any user’s post by sending multiple abuse flags to server. Server is not verifying report’s source as it only verifying report’s quantity, so attacker can send multiple reports from one account and get victim’s post deleted. 
Attacker can delete multiple posts by abusing this vulnerability in reputed forums and posts which have got high attention or number of likes, LOLs and comments.

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
