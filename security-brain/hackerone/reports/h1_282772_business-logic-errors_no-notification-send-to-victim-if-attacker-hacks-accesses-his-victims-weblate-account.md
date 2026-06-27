---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282772'
original_report_id: '282772'
title: no notification send to victim if attacker hacks/accesses his victims WebLate
  account.
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-10-25T09:43:42.673Z'
disclosed_at: '2018-09-26T09:23:09.718Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# no notification send to victim if attacker hacks/accesses his victims WebLate account.

## Metadata

- HackerOne Report ID: 282772
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2018-09-26T09:23:09.718Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello team,

when a hacker hacks into his victims WebLate account, the victim does not get any notifications. (via email for example) this means that the victim therefore won't take action to change his password for example in order to secure his account.


Risk:

very, very dangerous a hacker can now do whatever he wants, WITHOUT letting the victim know about his account takeover. (the victim knows nothing about the account takeover, so he also won't take action to change his password, etc, etc.) because of this vuln.


Migitation:

send a notification email for example if someone elses account here is compromised. companies such as Google are already doing this. so in this case your application will become MUCH more SECURE (if you fix this of course.) this is a best-practice feature that MOST big companies apply in their applications.


Note:

the attacker can do whatever he wants, WITHOUT letting his victims know a thing! (of course the victim will see the damage, BUT then it is already too late as the attacker already did whatever he wanted against his victims)

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
