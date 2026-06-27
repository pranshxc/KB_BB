---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145458'
original_report_id: '145458'
title: 'nextcloud.com: Mail Bombing ( No Rate Limiting On Sending Emails On Contact
  us Page)'
weakness: Memory Corruption - Generic
team_handle: nextcloud
created_at: '2016-06-17T16:13:45.160Z'
disclosed_at: '2016-07-17T16:28:25.156Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- memory-corruption-generic
---

# nextcloud.com: Mail Bombing ( No Rate Limiting On Sending Emails On Contact us Page)

## Metadata

- HackerOne Report ID: 145458
- Weakness: Memory Corruption - Generic
- Program: nextcloud
- Disclosed At: 2016-07-17T16:28:25.156Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

We can bomb (spam) any email by using your website.

Please Check attack success poc image in attached file you will understand :)

POC :
1.go to. Link :- &#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;
2. in details fill , all things in email option enter victim email. 
4.replay the same request many time , the victim's email will be spammed with nextcloud messages.

Impact :- i got 10000 Mail so it may leads to really hard bombing as well as its make your mailing servers busy...

Request :-

POST /contact/contactsubmit/ HTTP/1.1
Host: nextcloud.com
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:48.0) Gecko/20100101 Firefox/48.§0§
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://nextcloud.com/contact/
Cookie: _pk_id.1.efcb=b3f46f0726fd1fc9.1466166605.2.1466179534.1466179523.; _pk_ref.1.efcb=%5B%22%22%2C%22%22%2C1466179523%2C%22https%3A%2F%2Fhackerone.com%2Fnextcloud%22%5D; _pk_ses.1.efcb=*
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 113

yourname=fddgdfg&email=jyd4q4d01uar16s8%40my10minutemail.com&organization=dfsdfds&phone=00121212&comments=ytryrty


Cheers !

Ashish pathak

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
