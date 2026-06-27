---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '276747'
original_report_id: '276747'
title: CSS injection in avito.ru via IE11
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: avito
created_at: '2017-10-12T20:42:23.571Z'
disclosed_at: '2019-12-12T09:33:57.878Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# CSS injection in avito.ru via IE11

## Metadata

- HackerOne Report ID: 276747
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: avito
- Disclosed At: 2019-12-12T09:33:57.878Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team Security @avito

I discovered [CSS Injection](https://portswigger.net/knowledgebase/issues/details/00501300_cssinjectionreflected) on [avito.ru](https://avito.ru) in `form search` via IE11

####Description

`CSS injection` vulnerabilities arise when an application imports a style sheet from a **user-supplied URL**, or embeds user input in CSS blocks without adequate escaping. They are closely related to cross-site scripting (XSS) vulnerabilities but often trickier to exploit.

Being able to inject arbitrary CSS into the victim's browser may enable various attacks, including :

- Executing arbitrary JavaScript using IE's expression() function.
- Using CSS selectors to read parts of the HTML source, which may include sensitive data such as anti-CSRF tokens.
- Capturing any sensitive data within the URL query string by making a further style sheet import to a URL on the attacker's domain, and monitoring the incoming Referer header. 

**Affected URL**
~~~
https://www.avito.ru/rossiya/nedvizhimost?s='><b/style=position:fixed;top:0;left:0;font-size:200px>XSS<!--
~~~

####Proof of Concept 

{F228726}


####Remediation

Ensure that user input is adequately escaped before embedding it in CSS blocks, and consider using a whitelist to prevent loading of arbitrary style sheets.

####References

[Malicious CSS](http://mksben.l0.cm/2015/10/css-based-attack-abusing-unicode-range.html)

**Best Regards**
Hussain Adnan

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
