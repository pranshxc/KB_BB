---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265528'
original_report_id: '265528'
title: Reflected XSS on the data.gov (WAF bypass+ Chrome XSS Auditor bypass+ works
  in all browsers)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: gsa_bbp
created_at: '2017-09-02T18:21:43.165Z'
disclosed_at: '2017-09-15T13:39:04.674Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on the data.gov (WAF bypass+ Chrome XSS Auditor bypass+ works in all browsers)

## Metadata

- HackerOne Report ID: 265528
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: gsa_bbp
- Disclosed At: 2017-09-15T13:39:04.674Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered Cross-Site scripting issue on the https://www.data.gov/local/ endpoint.
The issue can be site-wide, and exploitable in any place, where pagination exist.

##The Impact and Severity
I assigned the High severity, because unlike the last #263226 report (that XSS was exploitable in the Firefox only), this XSS works in all browsers (Chrome/IE/Firefox).
But, considering that this case requires user interaction (hovering the mouse to the Page 2), the severity can be lowered to the Medium, if you consider so.

##POC (Reflected XSS)
Use this link in the Mozilla Firefox, Chrome or IE
https://www.data.gov/local/?&q&zzz%27onmou%3Cseover=1&ale%3Crt(%27xsp%27%3C)%3C;1;%20//

and hover the mouse to the page 2.
{F217930}

##Suggested fix
Sanitize the URLs in the `<div class="pagination">` block.

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
