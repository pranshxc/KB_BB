---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '85615'
original_report_id: '85615'
title: Reflected XSS on vimeo.com/musicstore
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-08-30T03:49:15.449Z'
disclosed_at: '2017-08-31T10:29:49.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on vimeo.com/musicstore

## Metadata

- HackerOne Report ID: 85615
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2017-08-31T10:29:49.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

The value of the parameter _section_ is reflected in the Javascript function `MusicStoreCommon.initialize()` without escaping, which allows to insert Javascript code.

__Proof of concept__
1. Go to https://vimeo.com/musicstore?section=%27-alert(document.domain)-%27.
2. `alert(document.domain)` is executed.

This reflected XSS is reproducible on Chrome, Safari and Firefox.

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
