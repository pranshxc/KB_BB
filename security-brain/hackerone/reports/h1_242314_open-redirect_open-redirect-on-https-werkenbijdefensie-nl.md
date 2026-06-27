---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242314'
original_report_id: '242314'
title: Open redirect on https://werkenbijdefensie.nl/
weakness: Open Redirect
team_handle: radancy
created_at: '2017-06-22T10:57:31.443Z'
disclosed_at: '2017-07-27T08:14:12.420Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- open-redirect
---

# Open redirect on https://werkenbijdefensie.nl/

## Metadata

- HackerOne Report ID: 242314
- Weakness: Open Redirect
- Program: radancy
- Disclosed At: 2017-07-27T08:14:12.420Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
https://werkenbijdefensie.nl/ajax/contrast.php?contrast=1

**Description:** 
By adding "?contrast=1" after every url, it wil be redirect to the path after https://werkenbijdefensie.nl/
So I can redirect it to another website by adding one more slash 
████████
## Browsers Verified In:
Any browser

## Steps To Reproduce:
https://werkenbijdefensie.nl//codechoi.com/POC/Maximum/i.php?contrast=1

By visit this link you will be redirected to fake login.

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
