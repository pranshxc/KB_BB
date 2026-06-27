---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44217'
original_report_id: '44217'
title: Application XSS filter function Bypass may allow Multiple stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-01-18T10:18:23.387Z'
disclosed_at: '2015-06-28T15:50:24.029Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Application XSS filter function Bypass may allow Multiple stored XSS

## Metadata

- HackerOne Report ID: 44217
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2015-06-28T15:50:24.029Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

As i analysed the application behavior and the security structure, i found out that the application is using "Greedy XSS Regex filter" against XSS and removes any the whole string from '<' to '>'. So i tried some basic bypass which allowed me to insert tags and other characters into the string.

Here is the the payload:
<%0crameset%20src=''> 

Now if we see the whole application is using same filter against XSS which makes this bypass to be universally working on nearly all the input fields, which means we can say an attacker can successfully bypass and enter XSS payload in database but when the string prints in the frontend there is another filter, which encode all html entities before printing.

Nice but now enough as many of the inputs could in the below condition will end up with a successful XSS exploitation.
1. Input under javascript.
2. Any string not properly encoded before printing.
3. JSON output with HTML headers.

I have already reported some issues in vimeo where input injected directly into javascript and do not need any html characters, another issue of JSON output with HTML headers. 

Below you can see both reports:
https://hackerone.com/reports/43934
https://hackerone.com/reports/44215

In the first screenshot you can see profile update request where i updates my profile and injected those HTML characters, in second screenshot you can see it injected in the response as stored XSS.

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
