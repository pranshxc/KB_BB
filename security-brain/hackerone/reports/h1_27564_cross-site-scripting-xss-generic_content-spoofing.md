---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27564'
original_report_id: '27564'
title: Content spoofing
weakness: Cross-site Scripting (XSS) - Generic
team_handle: phabricator
created_at: '2014-09-09T12:39:52.759Z'
disclosed_at: '2014-09-11T12:26:36.844Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Content spoofing

## Metadata

- HackerOne Report ID: 27564
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: phabricator
- Disclosed At: 2014-09-11T12:26:36.844Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I'm Dheeraj and I have found a content spoofing vulnerability in your system.


**Description :** 

Using the following link : https://secure.phabricator.com/auth/login/facebook:facebook.com/?error=<Spoofed Content>
Attacker can perform phishing attack.

**Attack Example :** 

https://secure.phabricator.com/auth/login/facebook:facebook.com/?error=We%20are%20having%20trouble%20accessing%20your%20account,%20kindly%20send%20your%20account%20details%20here%20attacker@site.com.%20Sorry%20for%20the%20inconvenience%20caused.


Regards
Dheeraj
@dheerajhere

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
