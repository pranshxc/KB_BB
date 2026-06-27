---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45428'
original_report_id: '45428'
title: CSRF bypass
weakness: Cross-Site Request Forgery (CSRF)
team_handle: vimeo
created_at: '2015-01-27T19:22:38.392Z'
disclosed_at: '2015-01-30T18:18:49.473Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF bypass

## Metadata

- HackerOne Report ID: 45428
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: vimeo
- Disclosed At: 2015-01-30T18:18:49.473Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Team,

Once again i'm here.
During research of vimeo.com I found that you are using anti-csrf token against csrf attack. but it's not going to validate on server side.

let's see

Step 1: go to https://vimeo.com/forgot_password
Step 2: write your email and click on **help me**.
Step 3: Now before posting make sure **Burp Suite's Interceptor is turned on** to capture the request.

Click on "help me" now, you will see below kind of request in Burp suite:

```
POST /forgot_password HTTP/1.1
Host: vimeo.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://vimeo.com/forgot_password
Cookie: vuid=471411067.232973627; __utma=18302654.785580395.1421186258.1421859718.1422384189.4; __utmz=18302654.1421186258.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=18302654.|2=user_type=basic=1^3=ms=0=1^7=video_count=0=1; site_settings=%7B%22sticky_page%22%3Anull%7D; has_logged_in=1; __gads=ID=3eb5153d2e8ef474:T=1421187886:S=ALNI_MZ62UIUIjNjSl4kp3auNxfRHSXdnQ; stats_start_date=2015%2F01%2F10; stats_end_date=2015%2F01%2F14; __utmb=18302654.4.10.1422384189; __utmc=18302654; __utmli=forgot_form; xsrft=e9b0179d3dd45669bd6d44a2484fb0f5.0
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 79

email=shubhamgupta109.1995%40gmail.com&token=e9b0179d3dd45669bd6d44a2484fb0f5.0
```

now you can see you are using **anti-csrf token** there but it's not going to validate. attacker can flood user account with too many mails for password reset request.

I'ave attached POC of the same.
Let me know if you needed more info.

Best Regard
Shubham

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
