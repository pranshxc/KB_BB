---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '133744'
original_report_id: '133744'
title: XSS in Asset name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-04-22T09:13:39.342Z'
disclosed_at: '2016-05-13T18:30:31.949Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Asset name

## Metadata

- HackerOne Report ID: 133744
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-05-13T18:30:31.949Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Found one XSS iin asset name

**Steps To Reproduce**

1. Create Any member at `https://sandbox.veris.in/portal/members/`

2. Add that member in any group at `https://sandbox.veris.in/portal/groups/`

3. Create an `Asset` named `<script>alert(1);</script>` at `https://sandbox.veris.in/portal/assets/`

4. Now go back to members  `https://sandbox.veris.in/portal/members/` and click on the symbol shown in screen shot for any of the member
{F88735}

you should see an XSS popup!

Regards
Ashish

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
