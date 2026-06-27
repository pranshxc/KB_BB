---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176159'
original_report_id: '176159'
title: '[iOS] URI Obfuscation in iOS application'
weakness: HTTP Response Splitting
team_handle: brave
created_at: '2016-10-16T16:57:32.254Z'
disclosed_at: '2016-10-17T18:19:29.735Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- http-response-splitting
---

# [iOS] URI Obfuscation in iOS application

## Metadata

- HackerOne Report ID: 176159
- Weakness: HTTP Response Splitting
- Program: brave
- Disclosed At: 2016-10-17T18:19:29.735Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

you must trick someone into viewing a website they did not want to view by tempting them with something they are familiar with.

## Products affected: 

 Brave iOS application 

https://itunes.apple.com/in/app/brave-web-browser/id1052879175?mt=8  

this application is vulnerable to the URI obfuscation 

## Steps To Reproduce:

 * open browser into ios device 
* type www.brave.com@fb.com 
* it will open fb.com without any pop ups 

## Supporting Material/References:

  *PoC is under attached 

https://www.youtube.com/watch?v=51RPPwSEXvU

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
