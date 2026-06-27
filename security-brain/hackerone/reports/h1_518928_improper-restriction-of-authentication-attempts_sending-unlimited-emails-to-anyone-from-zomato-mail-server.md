---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '518928'
original_report_id: '518928'
title: Sending Unlimited Emails to anyone from zomato mail server.
weakness: Improper Restriction of Authentication Attempts
team_handle: zomato
created_at: '2019-03-30T05:10:48.992Z'
disclosed_at: '2019-04-16T15:39:04.413Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Sending Unlimited Emails to anyone from zomato mail server.

## Metadata

- HackerOne Report ID: 518928
- Weakness: Improper Restriction of Authentication Attempts
- Program: zomato
- Disclosed At: 2019-04-16T15:39:04.413Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:** Zomoto provides developers to get the rich data of restaurant from their API.
https://developers.zomato.com/api
But here there is a security issue that can we exploited against zomato's Simple Email Server on Aws. 

**Description:**When  we request the api_key from zomato they ask us for our email address and if the registration is successful then the developer would receive the confirmation email and they would get the api key. But there is no limit on number of times we can request the api_key. Although we get the same api_key every time but every time a email is sent to the specified email (This can we email of anyone).
**Platform(s) Affected:** Website


## Steps To Reproduce:

1. Go to this url https://developers.zomato.com/api and click on the generate api key button.

>Note:- This button is only shown to the users those who have not generated the api_key before.


2 . Intercept the request in proxy you would get a post request

``` 
POST /php/developer HTTP/1.1
Host: www.zomato.com
Connection: close
Content-Length: 223
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://developers.zomato.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36
DNT: 1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://developers.zomato.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fr;q=0.8,hi;q=0.7,ru;q=0.6
Cookie: PHPSESSID=f735ebfd3e11e47782417af48ab7ee23700ba818; 

context=api&action=generate_api_key&plan=premium&token=c8bb20d4e575cf91aa8028ac9802a050&name=VIPIN+BIHARI&email=<ANY_EMAIL>&phone=8127411000&company=XYZ.com&country=1
```
F454847: Screenshot from 2019-03-30 10-31-02.png

3 . Now Attacker can Brute force the same request ( as above ) any numbers of times and the attacker would be able to send api_key email to anyone many times.

## Impact

1. The attacker can send api_key email to anyone ( It will be a spam mail for anyone ) any number of times and there making there mailbox out of storage.
2. It cost money to send emails to anyone and here the company may have the financial loss (If attacker tries to send thousands of mail ).

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
