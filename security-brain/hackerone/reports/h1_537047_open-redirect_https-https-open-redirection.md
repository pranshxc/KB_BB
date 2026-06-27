---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '537047'
original_report_id: '537047'
title: '[https://█████████/]&&[https://█████████/] Open Redirection'
weakness: Open Redirect
team_handle: lyst
created_at: '2019-04-12T22:30:05.170Z'
disclosed_at: '2022-03-22T11:53:42.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- open-redirect
---

# [https://█████████/]&&[https://█████████/] Open Redirection

## Metadata

- HackerOne Report ID: 537047
- Weakness: Open Redirect
- Program: lyst
- Disclosed At: 2022-03-22T11:53:42.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

***Summary***

Hi Team,

An attacker can redirect vicitm on an external website using ``https://████/account/login``  endpoint because ``next`` parameter is not being validated properly.

***Affected URL***

`https://███/account/login/?next=///////////////////////////evil.com`

***Steps to Reproduce***

1) Go https://████/account/login/?next=%2Fapp%2F .
2) Add this payload `////////////////////////////evil.com` to the `?next=` parameter .
3) Registeran account in the normal way .
4) You will be redirected to evil.com website .

***POC***
{F467696}

***References***

* https://hackerone.com/reports/347645
* https://hackerone.com/reports/125003
* https://hackerone.com/reports/411723

## Impact

* Open redirects allow a malicious attacker to redirect people unknowingly to a malicious
website .
* Simplifies phishing attacks .

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
