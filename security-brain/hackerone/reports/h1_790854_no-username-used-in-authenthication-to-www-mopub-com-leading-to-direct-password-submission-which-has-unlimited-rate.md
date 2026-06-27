---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '790854'
original_report_id: '790854'
title: NO username used in authenthication to www.mopub.com leading to direct password
  submission which  has unlimited submission rate.
team_handle: x
created_at: '2020-02-07T19:51:26.608Z'
disclosed_at: '2020-02-28T00:00:48.060Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
asset_identifier: mopub.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# NO username used in authenthication to www.mopub.com leading to direct password submission which  has unlimited submission rate.

## Metadata

- HackerOne Report ID: 790854
- Weakness: 
- Program: x
- Disclosed At: 2020-02-28T00:00:48.060Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**user name is  not used in authentication leading to direct password submission

**Description:** user name not used in authentication in https://www.mopub.com/login/?next=/dsp-portfolio/       (this page is labelled as SITE ADMIN: refer POC) can lead to direct submitting of password and this password has  unlimited submission rate

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. go to https://www.mopub.com/login/?next=/dsp-portfolio/
  2. we get a text box input only for password submission.
  3. this password submission has unlimited rate for submitting leading to bruteforce attacks.

POC screenshots attached.

## Impact:This page is labelled as site admin (look in poc)and thus direct entry of password only which has no rate for submission can lead to attacker getting logged in.

## Supporting Material/References:

  * screenshots of POC attached.)

## Impact

attaker can login to page which is listed as SITE ADMIN in mopub.com

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
