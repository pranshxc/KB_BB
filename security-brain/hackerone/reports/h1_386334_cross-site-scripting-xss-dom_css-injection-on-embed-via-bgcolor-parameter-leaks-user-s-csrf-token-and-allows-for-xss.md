---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386334'
original_report_id: '386334'
title: CSS Injection on /embed/ via bgcolor parameter leaks user's CSRF token and
  allows for XSS
weakness: Cross-site Scripting (XSS) - DOM
team_handle: chaturbate
created_at: '2018-07-24T18:02:24.808Z'
disclosed_at: '2018-09-19T23:37:20.507Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# CSS Injection on /embed/ via bgcolor parameter leaks user's CSRF token and allows for XSS

## Metadata

- HackerOne Report ID: 386334
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: chaturbate
- Disclosed At: 2018-09-19T23:37:20.507Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

There's a CSS injection here: https://chaturbate.com/embed/admin/?bgcolor=%7D*%7Bbackground:red&tour=nvfS&disable_sound=0&campaign=iNSGX 

```
  body, div#main, div.content, div.block, div.section {margin: 0px; padding: 0px;}
  body {min-width:800px;}
  div.content {width: 100%;}
  
  body {background: }*{background:red;}

```

This allows an attacker to enumerate the CSRF token. Once the CSRF token is enumerated, we can 

#POC 
1. Go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR/reset`
2. Now go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR` and let it do it's magic :) 

{F324052}

There are numerous endpoints like `POST /choose_broadcaster_chat_color` where it returns `Content-Type: text/html; charset=utf-8` that could potentially allow a hacker to combine the two for XSS (I haven't gotten that far yet)


 **Do you mind asking your HackerOne contact to allow collaboration on your program, so I can invite another researcher that helped me exploit this fully?**

Thanks,
Ben

## Impact

#

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
