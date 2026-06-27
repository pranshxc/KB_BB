---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220150'
original_report_id: '220150'
title: 200 http code in 403 forbidden directories on main Ubnt.com domain
weakness: Forced Browsing
team_handle: ui
created_at: '2017-04-11T08:00:19.664Z'
disclosed_at: '2017-04-19T14:08:00.177Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- forced-browsing
---

# 200 http code in 403 forbidden directories on main Ubnt.com domain

## Metadata

- HackerOne Report ID: 220150
- Weakness: Forced Browsing
- Program: ui
- Disclosed At: 2017-04-19T14:08:00.177Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

My investigations revealed that we have accesible directory in forbidden directory:

http://www.ubnt.com/static/ - forbidden
http://www.ubnt.com/static/cm/ - forbidden
Here we have http://www.ubnt.com/static/cm/mode/ accesible and then /xm/l and /django/ foders

POC:
http://www.ubnt.com/static/cm/mode/ - 200 http code (accesible)
http://www.ubnt.com/static/cm/mode/xml/ - 200 http code (accesible)
http://www.ubnt.com/static/cm/mode/django/ - 200 http code (accesible)

Now, i didn't looked up very close to this pages content, but for sure we are not supposed to acces them. Thank you.

Kind Regards.

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
