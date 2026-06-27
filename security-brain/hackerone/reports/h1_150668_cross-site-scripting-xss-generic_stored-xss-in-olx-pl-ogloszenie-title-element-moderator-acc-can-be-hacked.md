---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150668'
original_report_id: '150668'
title: stored XSS in olx.pl - ogloszenie TITLE element - moderator acc can be hacked
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-11T16:40:45.432Z'
disclosed_at: '2016-12-11T14:15:09.971Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# stored XSS in olx.pl - ogloszenie TITLE element - moderator acc can be hacked

## Metadata

- HackerOne Report ID: 150668
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-12-11T14:15:09.971Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

The OLX.PL is vulnerable to stored XSS attack.
When adding new advertisement, it is possible to put a payload in its title (here I used Title<script>alert(1)</script>

I see ads are being pre-moderated, however it can remain uncaught also the length limit in title field is enough to insert into it e.g. a BeEF hook so it will invisible hack moderator's browser. 
Assuming there are unsolved session fixation issues this may lead to takeover of moderator's cookie and impersonating him

This input should be validated properly, e.g. a whitelist of chracters that can be used - aplhanum + some chars like .,!? but no html 

Please see screenshots as a PoC

Cheers
Lukasz

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
