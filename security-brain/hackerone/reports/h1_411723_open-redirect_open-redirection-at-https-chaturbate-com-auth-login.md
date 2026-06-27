---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411723'
original_report_id: '411723'
title: Open redirection at https://chaturbate.com/auth/login/
weakness: Open Redirect
team_handle: chaturbate
created_at: '2018-09-20T10:33:20.219Z'
disclosed_at: '2018-10-22T01:50:43.336Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirection at https://chaturbate.com/auth/login/

## Metadata

- HackerOne Report ID: 411723
- Weakness: Open Redirect
- Program: chaturbate
- Disclosed At: 2018-10-22T01:50:43.336Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

##Summary##
An attacker can redirect vicitm on an external website using https://chaturbate.com/auth/login/ endpoint because `next` parameter is not being validated properly. There is a protection existed but it's weak and can be bypassed.

`http` keyword is detected and protection works if payload contains `http` at beginning but that check can be bypassed using `Http` keyword. Though, only numeric is allowed after `Http:` so we can use decimal form of external domain/IP-address. In PoC, `3627732462` is decimal form of IP address of google.com.

## Steps To Reproduce:

  1. Open https://chaturbate.com/auth/login/?next=Http:3627732462
  1. Get logged in
  1. You will be redirected on https://google.com instead of a chaturbate website
  1. Done

###Suggested Fix:
Use more strong regular expression at this endpoint.

## Impact

- Simplifies phishing attacks
- Reflected File Download

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
