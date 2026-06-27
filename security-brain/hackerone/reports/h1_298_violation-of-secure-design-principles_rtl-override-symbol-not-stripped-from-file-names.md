---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '298'
original_report_id: '298'
title: RTL override symbol not stripped from file names
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2013-11-07T19:12:41.742Z'
disclosed_at: '2015-05-28T04:49:32.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# RTL override symbol not stripped from file names

## Metadata

- HackerOne Report ID: 298
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-28T04:49:32.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Any [U+202E RIGHT-TO-LEFT OVERRIDE](http://codepoints.net/U+202E) (and similar) symbols in file names of uploaded files are not stripped from the file name, causing potentially malicious executables to look like harmless images, for example. This might trick HackerOne panel members into accidentally opening _evil h4x0r filez_.

I’ve attached two files:

* one is named [`insane_in_the_cort[RLO]3pm.exe`](http://mothereff.in/js-escapes#1insane%5fin%5fthe%5fcort%5Cu202E3pm.exe), which gets rendered as `insane_in_the_cortexe.mp3`, making it look like a harmless mp3 file of a well-known Cypress Hill song.
* another is named [`po[RLO]gnp.app`](http://mothereff.in/js-escapes#1po%5Cu202Egnp.app), which gets rendered as `poppa.png`, as if it was just a PNG image.

I’ve also attached a screenshot showing what it looks like after uploading the files.

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
