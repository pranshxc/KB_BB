---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198218'
original_report_id: '198218'
title: HTML Injection on ████
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2017-01-13T19:48:13.428Z'
disclosed_at: '2019-12-02T18:34:30.450Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection on ████

## Metadata

- HackerOne Report ID: 198218
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:34:30.450Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
HTML Injection vulnerabilities on █████████ Air Base Site.

**Description:**
Search value are output without being escaped.

HTML Injection via ```Category``` parameter
http://█████████/News/Commentaries?Search=security&Category=%22%3E%3Cimage/src=%22//███████/sealift/2011/July/images/Gumbyleaning2.jpg

Response HTML
```
<div class="dig_pager">

<a class="dig_pager_button dig_pager_current" href="http://█████████/News/Commentaries/Search/security?Category="><image/src="//████████/sealift/2011/July/images/Gumbyleaning2.jpg"><span>1</span></a>
```


## Impact
- By setting inappropriate contents, the impression of the organization deteriorates.
For example, short URLs that set porn images and graphic images are shared by SNS.

- GET request can be generated from the victim's browser.
For example, there are cases where it is possible to log out a Web service used by the victim.
>This discussion is helpful.
>http://security.stackexchange.com/a/135548


## Suggested Remediation Actions
Escape HTML before inserting untrusted data into element content.

Because WAF is running on this site, I could not do XSS.
However, since WAF may be bypassed, I recommend HTML escaping.

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
