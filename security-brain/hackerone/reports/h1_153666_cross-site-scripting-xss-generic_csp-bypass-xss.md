---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153666'
original_report_id: '153666'
title: csp bypass + xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2016-07-25T11:37:10.338Z'
disclosed_at: '2017-07-05T23:53:00.642Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# csp bypass + xss

## Metadata

- HackerOne Report ID: 153666
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2017-07-05T23:53:00.642Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

On my previous report (number 126464) I've mentioned that 
analytics.twitter.com has a CSP bypass which I couldn't exploit that time.

Now, I've found a reflected XSS on careers.twitter.com which again I couldn't exploit by itself. Because you have CSP, and I've combined two of them to successfully trigger XSS.

If you visit the url:
https://careers.twitter.com/en/jobs-search.html?location=1%22%3E%3Cscript%20src=//analytics.twitter.com/tpm?tpm_cb=alert%28document.domain%29%3E//

you will see xss triggered. 

Regards.

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
