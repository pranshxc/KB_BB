---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17540'
original_report_id: '17540'
title: Reflected XSS in Pastebin-view
weakness: Cross-site Scripting (XSS) - Generic
team_handle: irccloud
created_at: '2014-06-26T01:59:19.878Z'
disclosed_at: '2014-06-28T13:48:03.078Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in Pastebin-view

## Metadata

- HackerOne Report ID: 17540
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: irccloud
- Disclosed At: 2014-06-28T13:48:03.078Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The paste ID passed in via the URL in the Pastebin-view is inserted between `<script>` tags unsanitised. This leads to reflected XSS that bypasses all major XSS protection software (Chrome, IE...).

Normal request: https://www.irccloud.com/pastebin/nhm4f6pB
Proof-of-concept: https://www.irccloud.com/pastebin/";alert(0);%2F%2F

I've never used **HackerOne** before so please let me know if my report is missing something important!

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
