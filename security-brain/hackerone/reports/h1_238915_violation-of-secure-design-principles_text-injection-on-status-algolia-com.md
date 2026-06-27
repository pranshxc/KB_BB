---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '238915'
original_report_id: '238915'
title: Text injection on status.algolia.com
weakness: Violation of Secure Design Principles
team_handle: algolia
created_at: '2017-06-11T06:55:15.028Z'
disclosed_at: '2017-08-25T10:17:57.962Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Text injection on status.algolia.com

## Metadata

- HackerOne Report ID: 238915
- Weakness: Violation of Secure Design Principles
- Program: algolia
- Disclosed At: 2017-08-25T10:17:57.962Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Algolia team!

I just found a text injection vulnerabilty in [status.algolia.com/clusters](https://status.algolia.com/clusters/) . Please follow the steps below.

**Vulnerable URL**
[status.algolia.com](https://status.algolia.com/clusters/)  

Steps to reproduce:
* Go to [Vulnerable URL](https://status.algolia.com/clusters/)
* Add anything you want after the Vulnerable Url.

**POC**
[LIVE POC](https://status.algolia.com/clusters/For%20more%20info%20go%20to%20www.evil.com)

F193293

Hope you fix it!

Thanks!
Sh3r1

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
