---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36986'
original_report_id: '36986'
title: '[Stored XSS] vine.co - profile page'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-11-21T13:39:29.380Z'
disclosed_at: '2015-03-26T22:34:57.111Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [Stored XSS] vine.co - profile page

## Metadata

- HackerOne Report ID: 36986
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-03-26T22:34:57.111Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Stored XSS via API request:
While creating new account in Windows mobile app, i noticed this request:

    PUT /users/1147563919679037440 HTTP/1.1

    avatarUrl=https%3A%2F%2Fvines.s3.amazonaws.com%2Favatars_trellis%2F2014%2F11%2F21%2F0B2EAE2EB81147563929149554688_1.3.4.jpg&username=

it seems that the variable username is not properly filtered, just set username to e.g. <svg/onload=alert()> and see result on your profile in vine web site. 

"demo":
https://vine.co/u/1147563919679037440

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
