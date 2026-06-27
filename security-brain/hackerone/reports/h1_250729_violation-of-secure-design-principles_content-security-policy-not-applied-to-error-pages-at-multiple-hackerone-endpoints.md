---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '250729'
original_report_id: '250729'
title: Content Security Policy not applied to error pages at multiple HackerOne endpoints
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-07-18T04:22:35.920Z'
disclosed_at: '2017-12-12T01:05:38.090Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Security Policy not applied to error pages at multiple HackerOne endpoints

## Metadata

- HackerOne Report ID: 250729
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2017-12-12T01:05:38.090Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HackerOne CSP "script-src" includes "unsafe-inline" bypass via % and %"
-----


**Summary & Description**

>We utilize a strict Content Security Policy and a safe-by-default templating language to effectively neutralize Cross-Site Scripting (XSS).

>We encrypt all network communications with SSL/TLS accompanied with Perfect Forward Secrecy and HTTP Strict Transport Security (HSTS), including being HSTS preloaded in most major browsers.

base in my finding i found that there was a missing or not included `Content Security Policy` in your website. i bypass a simple `%` or `%"` to reproduce a XSS. like what you said `We utilize a strict Content Security Policy and a safe-by-default templating language to effectively neutralize Cross-Site Scripting (XSS).` and `We encrypt all network communications with SSL/TLS accompanied with Perfect Forward Secrecy and HTTP Strict Transport Security (HSTS), including being HSTS preloaded in most major browsers.` but in this case i can bypass via inspect element.

why am i getting this error or a blank page ? with a simple `%` or `%"` at the and point of a url ? i can bypass your `Content Security Policy`


### Steps To Reproduce

at first if you `Inspect element` and `Edit a HTML` at any line you will getting this error

>Refused to execute inline event handler because it violates the following Content Security Policy directive: "script-src 'self' www.google-analytics.com". Either the 'unsafe-inline' keyword, a hash ('sha256-...'), or a nonce ('nonce-...') is required to enable inline execution.

which is good, but in my case, i can bypass your `Content Security Policy` with `%` or `%"` at the end point of a any url


1. Go to any HackerOne Subdomains
2. add `%` or `%"` at the end point
3. Inspect element and `Edit as HTML` at any line
4. paste the payload, `<img src=x onerror=alert('Hacker1')>`
5. now i can bypass your `Content Security Policy`

Proof of Concept Video
https://www.youtube.com/watch?v=zMjTgpm-dLE

**Tested Websites**
	
>https://hackerone-attachments.s3.amazonaws.com
https://api.hackerone.com
https://hackerone.com
https://www.hackerone.com
https://profile-photos.hackerone-user-content.com



**Reference**
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src
https://www.websec.be/blog/cspreporting/



**Platforms and Tested Browser**

Tested in Windows 7 and 10
Google Chrome latest Version
Microsoft Edge 40.15063.0.0

**Regards:**
WH-PH

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
