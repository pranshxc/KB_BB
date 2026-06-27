---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229825'
original_report_id: '229825'
title: Rate Limit Issue on hosted.weblate.org
weakness: Improper Restriction of Authentication Attempts
team_handle: weblate
created_at: '2017-05-19T09:48:37.059Z'
disclosed_at: '2017-07-02T09:52:58.501Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Rate Limit Issue on hosted.weblate.org

## Metadata

- HackerOne Report ID: 229825
- Weakness: Improper Restriction of Authentication Attempts
- Program: weblate
- Disclosed At: 2017-07-02T09:52:58.501Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

Rate limit issue exist in hosted.weblate.org. An attacker can able to send as many email as he want to the victim mail. The attacker can successfully bruteforce on any users mail account even when the rate limiting is enabled.

Step to reproduce :

1. sign up and login to a [hosted.weblate.org](https://hosted.weblate.org)
2. Go to [Password reset](https://hosted.weblate.org/accounts/reset/) option
3. Enter an email address. 
4. Set up a proxy server (i used burp)
5. Configure your browser(firefox in my case) to work with the proxy server
6. Click on "Reset my password" button
7. Intercept the request
8. Send to Intruder
9. set position as your given email
10. set payload as many time you want to send mail
11. click on start attack

The victim will get mail as the number of payload you added. In my case i added upto 300 time and it hit into my mail box upto 300 time.

##Request
```
POST /accounts/reset/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 135
Referer: https://hosted.weblate.org/
Cookie: csrftoken=csrftoken_here
Connection: keep-alive
Upgrade-Insecure-Requests: 1

csrfmiddlewaretoken=csrfmiddlewaretoken_here&email=email@here.com&content=&captcha=captcha_here
```

{F186001}

{F186002}

Thanks

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
