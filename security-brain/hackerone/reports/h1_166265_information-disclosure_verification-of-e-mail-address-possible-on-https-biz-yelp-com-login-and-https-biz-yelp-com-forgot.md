---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166265'
original_report_id: '166265'
title: Verification of E-Mail address possible on https://biz.yelp.com/login and https://biz.yelp.com/forgot
weakness: Information Disclosure
team_handle: yelp
created_at: '2016-09-06T20:29:41.312Z'
disclosed_at: '2016-10-27T17:39:43.075Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- information-disclosure
---

# Verification of E-Mail address possible on https://biz.yelp.com/login and https://biz.yelp.com/forgot

## Metadata

- HackerOne Report ID: 166265
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2016-10-27T17:39:43.075Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

On pages https://biz.yelp.com/login and https://biz.yelp.com/forgot a malicious user can verify if a particular E-mail address is registered on biz.yelp.com.

Steps to reproduce for https://biz.yelp.com/login:
1. Open https://biz.yelp.com/login
2. Enter non existing E-Mail Address
3. Enter any password
4. Submit form
5. Result: The error message discloses, that the submitted E-Mail address is not known. 

Steps to reproduce for https://biz.yelp.com/forgot:
1. Open https://biz.yelp.com/forgot
2. Enter non existing E-Mail Address
4. Submit form
5. Result: The error message discloses, that the submitted E-Mail address is not known. 

An attacker can try different E-Mail addresses and can test if they are registered or not, helping him in a brute-force attack.

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
