---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '34188'
original_report_id: '34188'
title: Various Low level Vulnerabilities
weakness: Cross-site Scripting (XSS) - Generic
team_handle: blockio
created_at: '2014-11-06T10:29:19.264Z'
disclosed_at: '2015-05-03T02:23:48.608Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Various Low level Vulnerabilities

## Metadata

- HackerOne Report ID: 34188
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: blockio
- Disclosed At: 2015-05-03T02:23:48.608Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1.XSS protection Not Enabled:
Example URL: https://block.io/js/secure/secrets.js?mtime=1412493238

Web Browser XSS Protection is not enabled, or is disabled by the configuration of the 'X-XSS-Protection' HTTP response header on the web server

The X-XSS-Protection HTTP response header allows the web server to enable or disable the web browser's XSS protection mechanism. The following values would attempt to enable it: 
X-XSS-Protection: 1; mode=block
X-XSS-Protection: 1; report=http://www.example.com/xss
The following values would disable it:
X-XSS-Protection: 0
The X-XSS-Protection HTTP response header is currently supported on Internet Explorer, Chrome and Safari (WebKit).
Note that this alert is only raised if the response body could potentially contain an XSS payload (with a text-based content type, with a non-zero length).

Ensure that the web browser's XSS filter is enabled, by setting the X-XSS-Protection HTTP response header to '1'.


2.Cookie set Without HTTPonly flag
Example URL: https://block.io/users/sign_in

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.Ensure that the HttpOnly flag is set for all cookies.


3.Cookie set without secure flag
Example URL: https://block.io/users/password/new

A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted tunnel. Ensure that the secure flag is set for cookies containing such sensitive information.

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
