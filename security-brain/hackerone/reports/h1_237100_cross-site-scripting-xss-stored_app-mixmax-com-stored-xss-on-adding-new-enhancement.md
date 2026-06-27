---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '237100'
original_report_id: '237100'
title: '[app.mixmax.com] Stored XSS on Adding new enhancement.'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mixmax
created_at: '2017-06-06T03:29:54.853Z'
disclosed_at: '2017-06-13T05:30:36.822Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [app.mixmax.com] Stored XSS on Adding new enhancement.

## Metadata

- HackerOne Report ID: 237100
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mixmax
- Disclosed At: 2017-06-13T05:30:36.822Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Mixmax team,

Today I just found a Stored XSS on app.mixmax.com by adding a new enhancement. Just follow the steps below to reproduce this bug.

**Vulnerable URL**
[APP MIXMAX - Settings - Integrations & API](https://app.mixmax.com/dashboard/settings/integrations)

**Payload**
"><img src=x onerror=alert(document.domain)>


**Steps to reproduce**
- Go to the [Vulnerable URL](https://app.mixmax.com/dashboard/settings/integrations).
- Click Integrations & API then click Add Enhancement.
- In the **Name Field** just add the **Payload** into it. add what ever you want in to the other fields then click **Add Enhancement**

- after you  add the new enhancement. the prompt will show like this: F191647

- and then we can share this New Enhancement to the other users or a team by clicking the share icon beside to our newly added enhancement. F191648

- add a user or a team to share this enhancement. F191655 

- after you share this to the use users, the users will recieve an email regarding to the enhance that you have been shared to them.  F191656
  
 when the users or the the victim accept the enhancement, it will redirect to the **Vulnerable URL** and showing that our payload are working.

XSSED!
F191663


Regards,
Sh3r1

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
