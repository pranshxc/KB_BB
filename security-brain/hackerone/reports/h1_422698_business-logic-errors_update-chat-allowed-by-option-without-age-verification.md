---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '422698'
original_report_id: '422698'
title: Update Chat Allowed By Option ( without age verification )
weakness: Business Logic Errors
team_handle: chaturbate
created_at: '2018-10-11T18:57:01.553Z'
disclosed_at: '2018-10-18T12:34:39.056Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Update Chat Allowed By Option ( without age verification )

## Metadata

- HackerOne Report ID: 422698
- Weakness: Business Logic Errors
- Program: chaturbate
- Disclosed At: 2018-10-18T12:34:39.056Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary##
Hi Team,
I am here again with one interesting issue.
This issue deals with the fact that according to the policies of chaturbate, a broadcaster cannot modify the option - Chat Allowed By - until and unless he/she has verified his/her age (default choice is set to all).
This thing could be bypassed and any broadcaster who doesn't have his/her age verified could update this option.

## Steps To Reproduce:

1. First of all, start broadcasting.
2. Click on the gear icon in the chat options to open broadcaster settings.
3. Edit any option and intercept the request in Burp Suite.
4. Now in that request, replace the value of the parameter allowed_chat with any of the following 
   1. all
   2. tip_recent
   3. tip_anytime
   4. tokens
5. The value would get updated even though the age has not been verified.

## Impact

Any user who doesn't have his/her age verified can update settings which have been blocked for them.

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
