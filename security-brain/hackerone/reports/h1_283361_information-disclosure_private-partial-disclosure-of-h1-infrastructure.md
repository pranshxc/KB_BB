---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283361'
original_report_id: '283361'
title: Private partial disclosure of h1 infrastructure
weakness: Information Disclosure
team_handle: security
created_at: '2017-10-26T22:17:15.436Z'
disclosed_at: '2017-11-03T00:29:44.632Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private partial disclosure of h1 infrastructure

## Metadata

- HackerOne Report ID: 283361
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2017-11-03T00:29:44.632Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description**
I've found that following servers & services can be potentially interesting when attacking h1-infrastructure:
* Payments Admin ██████
* API Docs ██████████
* API █████████
* MailCatcher ██████████
* Story Book ███
* Karma ████████
* Core Test Server █████████
* Core Staging ████
* Core Production https://hackerone.com/
* Support Staging ███████
* Support Production █████████
* Payments Staging ███████
* Payments Production █████

At least ███ are enabled via Internet.
For example ████ is using Basic Authentication without any throtlling.
I've write JMeter script that performs bruteforcing by dictionary (nothing was found by 10K attempts but I've stopped bruteforcing as I do not understant possible impact on your staging service).

In my practice Staging servers often use forks of production data with some obfuscation of very sensitive data. But, any way real sensitive data can be still found in such instances and used against production.

**Steps to reproduce**
* login to the application and go to /bugs page
* find that███████.███████.js is downloaded by browser (perhaps for other user the hash-value can be different)
* look inside the *.js file - you will find uppermentioned links

**p.s.**
No such reports are registered currently in your Hacktivity thread.
brutforcing-jmeter script can be provided to you if necessary.

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
