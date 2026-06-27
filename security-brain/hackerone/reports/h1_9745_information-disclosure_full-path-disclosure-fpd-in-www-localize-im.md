---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9745'
original_report_id: '9745'
title: Full Path Disclosure (FPD) in www.localize.im
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-25T14:14:56.830Z'
disclosed_at: '2014-07-08T01:53:41.804Z'
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

- HackerOne Report ID: 9745
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-07-08T01:53:41.804Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
found another information disclosure vulnerability/Full Path Disclosure on your application.

Proof of Concept
-------------------------
GET  : https://www.localize.im/projects/[projiect ID/languages/[Language ID]
POST CONTENT: 
`CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yy4][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&####LotsOfPhrases######&updatePhrases[secret]=[SecredCodes]&updatePhrases[translatorID]=[ID]`

Just Add "[]" after any of those *updatePhrases[edit][ID][0]* parameter.

Note: look like my last FPD Vulnerability report. doesn't it?
but last one was at *updatePhrases[previous][ID][0]* that is fixed as you rolled out a fix for that..
i just went to check that the bug is fixed or not and found there is another parameter that is still vulnerable.

### The information from page:
> **Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 192**

I Also Added a Screenshot of that FPD as attachment..
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
