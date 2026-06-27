---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9256'
original_report_id: '9256'
title: Full Path Disclosure (FPD) in www.localize.im
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-23T01:46:29.208Z'
disclosed_at: '2014-04-23T04:56:23.261Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure (FPD) in www.localize.im

## Metadata

- HackerOne Report ID: 9256
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-23T04:56:23.261Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found an information disclosure vulnerability/Full Path Disclosure on your application.

Proof of Concept
-------------------------
GET  : https://www.localize.im/projects/[projiect ID/languages/[Language ID]
POST CONTENT: 
`CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&####LotsOfPhrases######&updatePhrases[secret]=[SecredCodes]&updatePhrases[translatorID]=[ID]`

Just Add "[]" after any of those *updatePhrases[previous][ID][0]*

### The information from page:
> **Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191**

I Also Added a Screenshot of that FPD as attachment..
Hope You'll fix this one..
Thanks

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
