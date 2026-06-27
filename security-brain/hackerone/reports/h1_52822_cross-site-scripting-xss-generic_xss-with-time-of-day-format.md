---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '52822'
original_report_id: '52822'
title: XSS with Time-of-Day Format
weakness: Cross-site Scripting (XSS) - Generic
team_handle: phabricator
created_at: '2015-03-20T21:32:08.402Z'
disclosed_at: '2015-04-19T21:58:26.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS with Time-of-Day Format

## Metadata

- HackerOne Report ID: 52822
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: phabricator
- Disclosed At: 2015-04-19T21:58:26.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

- Go to your user preferences
- Put the following into Time-of-Day Format (with the quote): 
 `'<\i\m\g \s\r\c=x \o\n\e\r\r\o\r=\a\l\e\r\t(\'X\S\S\')\>' `
- Open a repository (diffusion) -> XSS-Popup

The repository file-overview is the only place where I could see the XSS so far.

Because it's a user own preference, it is not easy to actually do something malicious in a real-world scenario. But it's definitely possible if you think hard enough about it :)

Cheers,
David

mongoose

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
