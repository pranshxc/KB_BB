---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167107'
original_report_id: '167107'
title: XSS and Open Redirect on https://jobs.dubizzle.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-09-09T13:16:26.643Z'
disclosed_at: '2016-10-20T14:24:19.522Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS and Open Redirect on https://jobs.dubizzle.com/

## Metadata

- HackerOne Report ID: 167107
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-20T14:24:19.522Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found an interesting vulnerability.With this one we can redirect someone to a malicious site,or we can trigger XSS.

STEPS TO REPRODUCE
---------------------

1-Go to that link https://jobs.dubizzle.com/en/pricing/?return=javascript:prompt(31)
2-Click  the "Continue placing your ad" button.
3-XSS will execute.

For Open Redirect,we can use these link  https://jobs.dubizzle.com/en/pricing/?return=http://example.com

TESTING
---------------------
Tested and confirmed Chrome's and Firefox's latest versions.

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
