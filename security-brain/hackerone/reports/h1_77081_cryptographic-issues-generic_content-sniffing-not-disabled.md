---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77081'
original_report_id: '77081'
title: Content Sniffing not disabled
weakness: Cryptographic Issues - Generic
team_handle: keybase
created_at: '2015-07-20T20:48:50.106Z'
disclosed_at: '2015-08-05T01:28:42.527Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cryptographic-issues-generic
---

# Content Sniffing not disabled

## Metadata

- HackerOne Report ID: 77081
- Weakness: Cryptographic Issues - Generic
- Program: keybase
- Disclosed At: 2015-08-05T01:28:42.527Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Issue description :-
There was no "X-Content-Type-Options" HTTP header with the value nosniff set in the response. The lack of this header causes that certain browsers, try to determine the content type and encoding of the response even when these properties are defined correctly. This can make the web application vulnerable against Cross-Site Scripting (XSS) attacks. E.g. the Internet Explorer and Safari treat responses with the content type text/plain as HTML, if they contain HTML tags.

Issue remediation :-
Set the following HTTP header at least in all responses which contain user input:
X-Content-Type-Options: nosniff

Request:
OPTIONS / HTTP/1.1
Cookie: guest=lgHZIDA2MzM4NmU5ZWQ1ZTU3NWIwNjI1NTBiNTBmMjBmYTA4zlWtXXXOAAFRgMDEIPoFWhfui0zP639i8xFbEpow%2Flv4DLBOwb9VZrNNhfWg
Host: keybase.io
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*


Response:
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Mon, 20 Jul 2015 20:43:44 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3
Connection: keep-alive
X-Powered-By: Express
Allow: GET
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload

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
