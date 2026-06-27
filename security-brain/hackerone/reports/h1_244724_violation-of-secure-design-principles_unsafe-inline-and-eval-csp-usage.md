---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244724'
original_report_id: '244724'
title: Unsafe Inline and Eval CSP Usage
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-06-30T11:51:04.742Z'
disclosed_at: '2017-07-24T15:23:12.178Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unsafe Inline and Eval CSP Usage

## Metadata

- HackerOne Report ID: 244724
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-24T15:23:12.178Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team, The HTTP header of the wakatime.com website includes an unsafe CSP parameter for "script-src".

#Impact:
However, the "script-src" parameter is set to "unsafe-inline" or "unsafe-eval", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks. As a best practice, this value should not be included as a "script-src" parameter, if possible.

#PoC:
```
HTTP/1.1 200 OK
Server: nginx
Date: Fri, 30 Jun 2017 11:48:48 GMT
Content-Type: application/json
Content-Length: 2242
Connection: close
Set-Cookie: csrftoken=7032d6127e4e2a5fd4f74e2abbed3301403b0034; Expires=Fri, 07-Jul-2017 11:48:48 GMT; Max-Age=604800; Secure; Path=/
Vary: Cookie
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' data: https://*.stripe.com https://*.braintreegateway.com https://api.github.com https://*.olark.com https://wakatime.disqus.com https://*.disquscdn.com https://analytics.twitter.com https://platform.twitter.com https://static.ads-twitter.com/ https://www.google-analytics.com https://heapanalytics.com https://*.heapanalytics.com https://connect.facebook.net https://load.sumome.com https://sumome-140a.kxcdn.com; img-src 'self' data: https://ssl.google-analytics.com https://s-static.ak.facebook.com https://syndication.twitter.com https://sumome.com https://sumome-140a.kxcdn.com https://checkout.paypal.com https://bitbucket.org https://avatar-cdn.atlassian.com assets-cdn.github.com www.google-analytics.com https://*.braintreegateway.com heapanalytics.com https://analytics.twitter.com t.co *.twimg.com *.facebook.com *.olark.com *.disqus.com *.disquscdn.com *.githubusercontent.com *.gravatar.com *.wp.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://*.olark.com https://sumome-140a.kxcdn.com *.disquscdn.com; media-src https://*.olark.com https://*.amazonaws.com; font-src 'self' https://fonts.gstatic.com; frame-src 'self' https://*.stripe.com https://www.facebook.com https://s-static.ak.facebook.com https://staticxx.facebook.com https://*.twitter.com https://*.olark.com https://disqus.com www.youtube.com player.vimeo.com checkout.paypal.com; object-src 'self'; connect-src 'self' api.github.com www.google-analytics.com heapanalytics.com https://sumome.com *.olark.com https://avatar-cdn.atlassian.com https://secure.gravatar.com *.disqus.com;
```

As can be seen, "unsafe-inline" and "unsafe-eval" is included in in the list of "script-src" parameters. 
This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Let me know if any further info is required.

Regards,
Mr.R3boot.

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
