---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '919859'
original_report_id: '919859'
title: stored xss in app.lemlist.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: lemlist
created_at: '2020-07-09T17:29:33.440Z'
disclosed_at: '2020-07-21T14:08:47.344Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored xss in app.lemlist.com

## Metadata

- HackerOne Report ID: 919859
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: lemlist
- Disclosed At: 2020-07-21T14:08:47.344Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I found a stored xss [app.lemlist.com](https://app.lemlist.com/).

## Steps To Reproduce:

  1. go to https://app.lemlist.com/.
  1. create or edit **campaigns**.
  1. visit tab **Buddies-to-Be**.
  1. click **Add one** on the right Top.
  1. Fill in the input 
  1. add `/><svg src=x onload=confirm(document.domain);>` ** Icebreaker** and **companyName**
  1. click create .
              
## POC
{F901411}

## Impact

Stealing cookies

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
