---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '334253'
original_report_id: '334253'
title: CSRF at [Apply to this program] that lead to submit your request automatic
  with out any validations
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2018-04-06T14:21:28.785Z'
disclosed_at: '2018-07-05T23:09:23.824Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSRF at [Apply to this program] that lead to submit your request automatic with out any validations

## Metadata

- HackerOne Report ID: 334253
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2018-07-05T23:09:23.824Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , 
the behavior found in some of programs that need to `Apply to this program` like @hackthedts this program need to your submit Application before start found/send bug to them .
this button have no any validations/check protect for CSRF bug , that can lead to auto apply to program by used this link `https://hackerone.com/hackthedts?apply=true`

#POC 
this CSRF work fine with user that have a tax confirm or had an bounty get before .
1- open this link https://hackerone.com/hackthedts?apply=true
2- if you login-in you will see that your apply has been send successfully , if not login you will redirect to login page then the apply will take a place automatic 
 


### Optional: Your Environment (Browser version, Device, etc)

 * any

this should be an step to confirm the apply or an additional step to be sure what the user/research will do .

## Impact

this can be used to send massive apply with only open link

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
