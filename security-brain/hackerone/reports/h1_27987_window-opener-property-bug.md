---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27987'
original_report_id: '27987'
title: Window Opener Property Bug
team_handle: security
created_at: '2014-09-13T17:14:26.342Z'
disclosed_at: '2014-10-28T23:18:36.550Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Window Opener Property Bug

## Metadata

- HackerOne Report ID: 27987
- Weakness: 
- Program: security
- Disclosed At: 2014-10-28T23:18:36.550Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The bug mentioned in #23386 is not yet correctly patched I believe.

See, if a user sets his/her profile's website link to a similar page as mentioned in #23386. I mean a page that can manipulate the window.opener property would be able to accomplish similar results as in #23386

**Proof-of-Concept**:

1. Login to HackerOne
2. Navigate to https://hackerone.com/settings/profile/edit
3. Set *Website* to https://demo.prakharprasad.com/ga.html
4. Once someone visits this link from a profile page  (eg. https://hackerone.com/<username->), his opener HackerOne window will be hijacked.

Let me know if you have any questions.

Thanks,
Prakhar Prasad

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
