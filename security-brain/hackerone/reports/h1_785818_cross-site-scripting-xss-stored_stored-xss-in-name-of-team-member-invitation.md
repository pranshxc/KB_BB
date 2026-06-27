---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '785818'
original_report_id: '785818'
title: Stored XSS in Name of Team Member Invitation
weakness: Cross-site Scripting (XSS) - Stored
team_handle: localizejs
created_at: '2020-01-30T16:09:30.436Z'
disclosed_at: '2020-02-06T20:56:52.353Z'
has_bounty: true
visibility: full
substate: duplicate
vote_count: 14
asset_identifier: localizestaging.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Name of Team Member Invitation

## Metadata

- HackerOne Report ID: 785818
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: localizejs
- Disclosed At: 2020-02-06T20:56:52.353Z
- Has Bounty: Yes
- Visibility: full
- Substate: duplicate

## Original Report

hello team
i have found an stored in add team member
##Step to reproduce
1. Go to  https://localizestaging.com/organization/team?filter=all
2. click on add team member
3. On the name, enter payload:  </script><svg onload=alert(document.domain)>    
4. and in the email  add  your victim email
4. when he join the team the xss  will trigger.
{F701271}

now  victim , can't logout, he can't do anything in his account

best regards
@moodiabdoul3

## Impact

the victim can nothing in his account

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
