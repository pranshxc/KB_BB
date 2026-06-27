---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2434904'
original_report_id: '2434904'
title: Reflected Cross-site Scripting via search query on ██████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2024-03-26T16:32:56.994Z'
disclosed_at: '2024-05-03T18:06:55.779Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross-site Scripting via search query on ██████

## Metadata

- HackerOne Report ID: 2434904
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2024-05-03T18:06:55.779Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team

I found a reflected xss via search query on ████████ that allows an attacker to execute Javascript code into victim's browser.

## PoC

1- Doing subdomain enumeration of ██████████, i found the following one: ████████
2- On the search query i saw that is injecting inside an h6 html tag:

██████████

3- So to html escape, i used the following payload to trigger the XSS: `</h6><image/src/onerror=alert(document.cookie)>`

████

## Impact

An incorrect sanitization of search query parameter allows an attacker to execute JS code into victim's browser.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Proof-of-concept above on the description.

## Suggested Mitigation/Remediation Actions
Sanitize input data from the user to avoid html/XSS injections.

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
