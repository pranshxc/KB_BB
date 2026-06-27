---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140377'
original_report_id: '140377'
title: don't store CSRF tokens in cookies
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-05-22T21:17:47.463Z'
disclosed_at: '2016-06-16T15:25:14.224Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# don't store CSRF tokens in cookies

## Metadata

- HackerOne Report ID: 140377
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-06-16T15:25:14.224Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Your web application generates CSRF token values inside cookies
which is not a best practice for web applications as revelation of cookies can reveal CSRF Tokens as well.
Authenticity tokens should be kept separate from cookies and should be isolated to change operations in the account only.

More description:
This report tells that the CSRF tokens are present inside of the cookies value which is not a best practice and if the cookie is intercepted and compromised than the CSRF token will also be vulnerable.

This is the Captured request of edit Statement HTTP ,In this request you can see CSRF token is generating in cookies named as csrf_token

POST /~[MY USER ID]/statement.json HTTP/1.1
Host: gratipay.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CSRF-Token: y44PyqG67bRQljEA5mLK1bez4hgZ8XSD
X-Requested-With: XMLHttpRequest
Referer: https://gratipay.com/~ameerassadi4/
Content-Length: 24
Cookie: csrf_token=y44PyqG67bRQljEA5mLK1bez4hgZ8XSD; suppress-welcome=; session=aa5c93be733b4aae8370af6a3fae2be3
Connection: close

lang=en&content=sssssssd

i have also added a PoC picture in attachments,

Cheers,
Ameer Assadi
www.Ameeras.me / www.Geekurity.com

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
