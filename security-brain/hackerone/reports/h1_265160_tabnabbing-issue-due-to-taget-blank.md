---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265160'
original_report_id: '265160'
title: TabNabbing issue (due to taget=_blank)
team_handle: monero
created_at: '2017-09-01T07:01:43.664Z'
disclosed_at: '2018-04-25T05:50:20.331Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
---

# TabNabbing issue (due to taget=_blank)

## Metadata

- HackerOne Report ID: 265160
- Weakness: 
- Program: monero
- Disclosed At: 2018-04-25T05:50:20.331Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

i get to know in this particular url 
https://getmonero.org/get-started/what-is-monero/ and i found one 3rd party url.

Issue lies Here :

<a href="https://www.openhub.net/p/monero" target="_blank">

Here i can see you are using target=_blank and no more rel tag.
Here , target=_blank means it will open in another new tab. but due to tabnabbing it can change parent tab as well .
so as per security principal , don't trust much on 3rd party. and be at your safe sight,

i can recommend you to add rel="noreferer, ,noopener" to avoid this issue.

So final tag for that particular anchor tag will be:

<a href="https://www.openhub.net/p/monero" target="_blank rel="norefere,noopener" type="link">

Thanks,

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
