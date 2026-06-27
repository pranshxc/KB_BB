---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '377264'
original_report_id: '377264'
title: █████ - DOM-based XSS
weakness: Cross-site Scripting (XSS) - DOM
team_handle: deptofdefense
created_at: '2018-07-04T21:32:33.041Z'
disclosed_at: '2019-12-02T19:09:19.671Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# █████ - DOM-based XSS

## Metadata

- HackerOne Report ID: 377264
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:09:19.671Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings, 

I've discovered a DOM-based XSS at **███**

**_Proof of concept:_**

**1.** Go to https://████/█████████/home/troubleshoot.html?lang=en
**2.** In the username field, add the following code:

```
--><button/autofocus/onfocus=Function("confirm`1`")();//name="XSS
```

**3.** The javascript code is correctly executed:

██████

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

Thanks for your attention and let me know if you need anything.
Regards, Yumi

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
