---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27511'
original_report_id: '27511'
title: ads.twitter.com xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-09-09T02:32:00.993Z'
disclosed_at: '2014-11-17T14:30:51.415Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# ads.twitter.com xss

## Metadata

- HackerOne Report ID: 27511
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-11-17T14:30:51.415Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Cross-Site Scripting vulnerability exists in card[name] parameter when creating/cloning a card via script https://ads.twitter.com/accounts/18ce53wrkma/cards/new?card_type=7. 
Here is the simple test vector: </title><script>alert(document.cookie)</script><title>
After the card is created XSS becomes persistent and can be triggered via https://ads.twitter.com/accounts/18ce53wrkma/cards/show?url_id=42qj.

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
