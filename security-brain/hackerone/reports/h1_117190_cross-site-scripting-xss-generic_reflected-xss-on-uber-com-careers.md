---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117190'
original_report_id: '117190'
title: Reflected XSS on Uber.com careers
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-02-18T18:49:41.711Z'
disclosed_at: '2016-04-06T20:55:49.377Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on Uber.com careers

## Metadata

- HackerOne Report ID: 117190
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-04-06T20:55:49.377Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Location
www.uber.com/careers/

###Description:
It is possible for an attacker to inject an arbitrary javascript into city GET parameter. This leads to phishing, defacing from URL, stealing credentials by using a fake login page and many other client side risks.

###POC:
- Logon to [uber.com/careers/list/?city=...](https://www.uber.com/careers/list/?city=allicg<%2fscript><script>alert('xss by pavanw3b')<%2fscript>fupaiiz&country=all&keywords=&subteam=all&team=all) on firefox.
- Note the alert *xss by pavanw3b* as the screenshot attached.

Tested on latest firefox: 4.0.2

Please let me know if you need further explanation or details.​

Cheers,
Pavan
www.pavanw3b.com | fb/pavanw3b | @pavanw3b

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
