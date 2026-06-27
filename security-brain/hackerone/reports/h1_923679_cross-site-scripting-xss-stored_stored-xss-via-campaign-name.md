---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '923679'
original_report_id: '923679'
title: stored xss via Campaign Name.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: lemlist
created_at: '2020-07-14T17:29:59.163Z'
disclosed_at: '2020-07-21T14:46:35.025Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored xss via Campaign Name.

## Metadata

- HackerOne Report ID: 923679
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: lemlist
- Disclosed At: 2020-07-21T14:46:35.025Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi,
I found a stored  xss https://app.lemlist.com

## Steps To Reproduce:
1. go to https://app.lemlist.com/.
2. create or edit campaigns.
3. set the payload `/><svg src=x onload=confirm(document.domain);>` in the **Campaign Name**.
4. visit Buddies-to-Be tab .
5. click Add one on the right Top . or click on one of the list of  **Contact**
6. you will see pop-up.

## Poc
{F907302}

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
