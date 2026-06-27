---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1208453'
original_report_id: '1208453'
title: Account takeover through multistage CSRF at https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer
  and ../AutoChoice/changePwOktaAnswer
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gsa_vdp
created_at: '2021-05-25T12:08:45.244Z'
disclosed_at: '2021-07-23T02:07:47.706Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
asset_identifier: autochoice.fas.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Account takeover through multistage CSRF at https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer and ../AutoChoice/changePwOktaAnswer

## Metadata

- HackerOne Report ID: 1208453
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gsa_vdp
- Disclosed At: 2021-07-23T02:07:47.706Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Account takeover is possible through CSRF vulnerability at 'Change Security Question/Answer'  & ' Change Password'.
The endpoints - https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer & https://autochoice.fas.gsa.gov/AutoChoice/changePwOktaAnswer both are vulnerable to CSRF attack .==The CSRF token/or its presence is not validated at server side.==

Since, the password update functionality requires 'Secret Answer' Value & 'New Password'. Therefore, in multistage CSRF Secret Answer was updated first & then using that new secret answer, new password was set for the account using second stage.

Both CSRF request are performed through the same html POC. Upon execution of POC html, changes will  be reflected after few seconds as timeout is set for the first request to complete.  Also, there is no need to know the security question either, which itself is updated in the first stage.

POC Video - {F1314428}

CSRF Html file -  {F1314439}

@Triage Team - Since, this report involves two CSRFs for different functionalities, should I have filed two different  reports ?  as I would be losing rep. points.

## Impact

Account takeover through CSRF

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
