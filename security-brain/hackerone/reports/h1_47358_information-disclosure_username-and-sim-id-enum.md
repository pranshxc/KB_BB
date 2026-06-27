---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47358'
original_report_id: '47358'
title: Username and sim id enum
weakness: Information Disclosure
team_handle: mobilevikings
created_at: '2015-02-10T21:19:41.716Z'
disclosed_at: '2015-03-04T14:19:19.181Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Username and sim id enum

## Metadata

- HackerOne Report ID: 47358
- Weakness: Information Disclosure
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:19:19.181Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Look at this url (GET request)
https://mobilevikings.be/en/sims/authorization/remove/admin/1036358/ - looks good - admin user detected 
https://mobilevikings.be/en/sims/authorization/remove/lloyd/1036358/ - looks good - lloyd user detected
https://mobilevikings.be/en/sims/authorization/remove/lloydxxx/1036358/ - there is no lloydxxx user
Sim card id (exist username should be used - lloyd in this case):
https://mobilevikings.be/en/sims/authorization/remove/lloyd/1036358/ - sim card id 1036358 detected
https://mobilevikings.be/en/sims/authorization/remove/lloyd/1036359/ - sim card id 1036359 detected
https://mobilevikings.be/en/sims/authorization/remove/lloyd/1036351/ - there is no sim card id 1036351

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
