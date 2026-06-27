---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115296'
original_report_id: '115296'
title: Your Application Have Cacheable SSL Pages
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-02-08T01:25:52.766Z'
disclosed_at: '2017-10-16T05:52:14.105Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Your Application Have Cacheable SSL Pages

## Metadata

- HackerOne Report ID: 115296
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2017-10-16T05:52:14.105Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

You Have All Cacheable SSL Pages in Domain .

It is possible to gather sensitive information about the web application such as usernames, passwords, Contact information , comments or any machine name and/or sensitive file locations.

Sensitive information might have been cached by your browser

Most web browsers are configured by default to cache the user's pages during use. This means that SSL pages are cached as well. 

It is not recommended to enable the web browser to save any SSL information, since this information might be compromised when a vulnerability exists.

Response :-

HTTP/1.1 200 OK
Server: cloudflare-nginx
Date: Mon, 08 Feb 2016 01:21:25 GMT
Content-Type: text/html;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache

Disable caching on all SSL pages or all pages that contain sensitive data.

This can be achieved by using "Cache-Control: no-store" and either "Pragma: no-cache" or "Cache-Control: no-cache" response directives in your SSL page headers.

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
