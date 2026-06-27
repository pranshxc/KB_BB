---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112025'
original_report_id: '112025'
title: Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: udemy
created_at: '2016-01-21T13:13:32.943Z'
disclosed_at: '2016-02-22T23:56:20.777Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS

## Metadata

- HackerOne Report ID: 112025
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: udemy
- Disclosed At: 2016-02-22T23:56:20.777Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

Bug: Stored XSS
Payload: "><img src=x onerror=prompt(document.domain);>
Browser Used: Google Chrome
OS: Windows 7

Steps to Reproduce:

1) Log in to your account
2) Click on My Courses
3) Choose any enrolled courses
4) Click on Add Discussion
5) Click on Link -> Insert Link
6) In URL use above Payload
7) In Text write anything
8) Click on Insert 
9) Now click on that Text
10) Javascript will get executed.

Please check the link of PoC video..
https://www.dropbox.com/s/i2l5v7av597frj8/Udemy%20XSS.avi?dl=0

Thanks,
Manish Agrawal.

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
