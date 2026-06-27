---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '271533'
original_report_id: '271533'
title: Bruteforcing password reset tokens, could lead to account takeover
weakness: Improper Restriction of Authentication Attempts
team_handle: instacart
created_at: '2017-09-25T14:43:49.014Z'
disclosed_at: '2017-11-06T22:34:36.314Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Bruteforcing password reset tokens, could lead to account takeover

## Metadata

- HackerOne Report ID: 271533
- Weakness: Improper Restriction of Authentication Attempts
- Program: instacart
- Disclosed At: 2017-11-06T22:34:36.314Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey Instacart security team,

###Description
When resetting a new password on https://shoppers.instacart.com/password you will receive an email with a reset link.
when clicking on this link. you go to this page: https://shoppers.instacart.com/password/edit?reset_password_token=Your_Token

when entering a new password in the 2 input boxes on the page and clicking on "change my password" a post will be send to https://shoppers.instacart.com/password.
if the token is correct, the password will be changed. but if the token is incorrect, the response will contain "Reset password token is invalid".

Because there is no rate limit in place, this token can easily be brute forced.

###poc
this is the request that is used: 

POST /password HTTP/1.1
Host: shoppers.instacart.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 274
Referer: https://shoppers.instacart.com/password/edit?reset_password_token=The_Reset_Token
Cookie: My_cookies
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

utf8=%E2%9C%93&_method=put&authenticity_token=fSk65PV8vJ0RddbWWQsRP5VrbNIVqHjT%2Fgx6b8BlrOKIQirOlPSZ%2BnnbPUtPR8dB3hkMTLcky0J0P01qoysScQ%3D%3D&driver%5Breset_password_token%5D=The_Reset_Token&driver%5Bpassword%5D=New_password&driver%5Bpassword_confirmation%5D=New_password&commit=Change+my+password

###fix
to fix this issue, you could implement an timeout after a number of requests in a period of time.
just like it is implemented here: https://www.instacart.com/accounts/password
this returns "429 Too Many Requests" when making multiple requests in a short period of time.

also making the token more random by giving it a random number of characters instead of 20 characters will also help.
there is also an option to include the email as parameter. 

If you have questions, please don't hesitate to ask them. i will be happy to answer them ;)

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
