---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '797685'
original_report_id: '797685'
title: IDOR in marketing calendar tool
weakness: Insecure Direct Object Reference (IDOR)
team_handle: semrush
created_at: '2020-02-16T17:18:34.404Z'
disclosed_at: '2020-04-02T09:35:56.290Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in marketing calendar tool

## Metadata

- HackerOne Report ID: 797685
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: semrush
- Disclosed At: 2020-04-02T09:35:56.290Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#INTRODUCTION

##_I used two accounts to search for this vulnerability:_
**Id:** █████ **Email:** ██████
**Id:** ███ **Email:** ███

##_IP used:_
**78.194.169.36**

##_Endpoint URL:_
https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=CALENDAR_ID

#EXPLOITATION

##_Description of Security Issue:_
When a marketing calendar is loaded in the browser, the site sends a request such as this: {F718449}.
This request returns information such as if the owner has connected a google analytic account and the owner's user id associated with the calendar with the id pass in parameter. The problem comes from the fact that it is not verified that the user making the request has the calendar or that the person is invited to consult it.

#RESOLUTION
Check that the user making the request has the calendar or that the person is invited to consult the calendar.

## Impact

##_Exploit scenario for this vulnerability:_

 - A user such as a concurrent service could by bruteforcing the "calendar_id" parameter establish a list of all calendars and the number of unique users who have created calendars. It will also know the number of users who have connected their google analytic account on it. This represents bussiness data.

 - A user who knows someone's user_id (because he was invited to a calendar owned by the victim for example) can by bruteforcing the parameter "calendar_id" establish the number of calendar owned by the victim and the number of calendar being linked to a google analytic account.

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
