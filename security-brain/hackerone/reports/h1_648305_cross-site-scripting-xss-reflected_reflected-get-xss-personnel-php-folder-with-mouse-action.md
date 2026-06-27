---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '648305'
original_report_id: '648305'
title: '[██████] Reflected GET XSS (/personnel.php?..&folder=*) with mouse action'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2019-07-17T19:06:16.559Z'
disclosed_at: '2019-12-02T19:17:06.197Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [██████] Reflected GET XSS (/personnel.php?..&folder=*) with mouse action

## Metadata

- HackerOne Report ID: 648305
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:17:06.197Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I will combine this vulnerability with this vulnerability (described in this report #648222). If you have not read this report, I recommend reading that report first, and then studying this report.

##### I want to note that this report cannot be closed as a duplicate to the above described report. why? because this vulnerability exists for authorized users. Using the bypass authorization bug I just had the opportunity to explore the internal structure of the site.

If you study the last report, as well as the reports that you described there, you can understand that the developers have already tried to fix some vulnerabilities by simply restricting access to the site. It was not effective. It is strongly recommended to fix each vulnerability separately.

### Steps to reproduce

1) Turn on Live Interception in burp (Proxy-Intercept) Go to this link
> https://██████████/personnel.php?content=training&folder=FA_CERT%27%20onmouseover=alert(1)%20%27%22&item=FA05.01.01&rcnum=rc22752

2) Intercept request. Press right mouse button-> Do intercept -> Response this request
███████

3) Delete this redirection
█████

Answer:
████████

4) Then you need move the mouse cursor under the selected text block ("Mass-Sign")
████

Result:
████████

## Impact

JavaScript can still be dangerous if misused as part of malicious content:

-  Malicious JavaScript has access to all the objects that the rest of the web page has access to. This includes access to the user’s cookies. Cookies are often used to store session tokens. If an attacker can obtain a user’s session cookie, they can impersonate that user, perform actions on behalf of the user, and gain access to the user’s sensitive data.
- JavaScript can read the browser DOM and make arbitrary modifications to it. Luckily, this is only possible within the page where JavaScript is running.
- JavaScript can use the XMLHttpRequest object to send HTTP requests with arbitrary content to arbitrary destinations.
- JavaScript in modern browsers can use HTML5 APIs. For example, it can gain access to the user’s geolocation, webcam, microphone, and even specific files from the user’s file system. Most of these APIs require user opt-in, but the attacker can use social engineering to go around that limitation.

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
