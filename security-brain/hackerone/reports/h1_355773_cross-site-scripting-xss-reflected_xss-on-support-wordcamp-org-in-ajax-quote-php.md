---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '355773'
original_report_id: '355773'
title: XSS on support.wordcamp.org in ajax-quote.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: wordpress
created_at: '2018-05-21T23:10:18.324Z'
disclosed_at: '2018-07-23T15:06:06.875Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.wordcamp.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on support.wordcamp.org in ajax-quote.php

## Metadata

- HackerOne Report ID: 355773
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: wordpress
- Disclosed At: 2018-07-23T15:06:06.875Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
There is an XSS vulnerability in ajax-quote.php on http://support.wordcamp.org. It can be demonstrated with the attached POC - this needs to be run in Firefox to execute, as it's super basic and XSS Auditor will catch it (but with multiple parameters, even with one of them filtered, it's likely that one could be crafted that would work in Chrome, too).

I would quite like to check out that SupportPress application in more detail, but it's quite hard to install :( Seems to not work out of the box for me - so for now, just an XSS.

## Impact

An attacker who could trick an authenticated user into visiting their webpage/link could perform any action on behalf of that user. Cookie theft seems unlikely as, from a brief scan of the code (I can't login) I think it uses httponly on the important cookies.

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
