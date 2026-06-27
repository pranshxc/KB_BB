---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '854793'
original_report_id: '854793'
title: No rate limiting for confirmation email lead to email flooding and leads to
  enumeration of emails in publishers.basicattentiontoken.org
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2020-04-21T06:13:15.394Z'
disclosed_at: '2020-11-09T20:30:54.417Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: creators.basicattentiontoken.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limiting for confirmation email lead to email flooding and leads to enumeration of emails in publishers.basicattentiontoken.org

## Metadata

- HackerOne Report ID: 854793
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2020-11-09T20:30:54.417Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is no bruteforce protection here https://publishers.basicattentiontoken.org/publishers when i try to changes email's contact account.
Also the actual thing is when I put an existing email in the above url's "publisher[pending_email]" parameter I get an error response status (400 Bad Request)
But if i put non-existing email, i get "200 OK" status. As this do not have any bruteforce protection an attacker may get all the emails of the publishers.basicattentiontoken.org.

####How to reproduce
1.Use Burp Suite and capture below request upon navigation to https://publishers.basicattentiontoken.org/publishers/settings?locale=en# at changes emails contact
2.Click on Save button after entering email address
{code}
POST /publishers HTTP/1.1
Host: publishers.basicattentiontoken.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://publishers.basicattentiontoken.org/publishers/settings
X-CSRF-Token: K3ImpMdB22SFYupK9nbc9IEubpRgmVTYVKQ/HnPFcbglcbkSKBb5wdJ4GCx436E1TuPddMUZR0u5Nh0f9r6pJQ==
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------115523927333677217472699996749
Origin: https://publishers.basicattentiontoken.org
Content-Length: 466
DNT: 1
Connection: close
Cookie: _publishers_session=ed2071cd116ba7c96b346bb91a89720e; __cfduid=d906d4d29ca3e5455a66f2a903dea07071587447187; _pk_testcookie..undefined=1; _pk_testcookie.6.8f93=1; _pk_id.6.8f93=2ad1aec69df84899.1587447189.1.1587447535.1587447189.; _pk_ses.6.8f93=1

-----------------------------115523927333677217472699996749
Content-Disposition: form-data; name="publisher[name]"

Victim User
-----------------------------115523927333677217472699996749
Content-Disposition: form-data; name="publisher[pending_email]"

victimuser280@gmail.com
-----------------------------115523927333677217472699996749
Content-Disposition: form-data; name="_method"

patch
-----------------------------115523927333677217472699996749--

{code}
3.Send the captured request to Intruder and repeat the request in loop
3.Set the payload position into email address parameter with list of any random email address (option to enumerate email exist/non-exist)
4.Victim will get email flooding as much as payload has generated in his/her mailbox

####Remediation:
Rate limiting should be implemented

####References:
https://hackerone.com/reports/297359
https://hackerone.com/reports/39486
https://hackerone.com/reports/751604
https://hackerone.com/reports/774050
https://hackerone.com/reports/245147

## Impact

Email flooding and bruteforcing

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
