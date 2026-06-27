---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152584'
original_report_id: '152584'
title: S3 bucket takeover due to proxy.harvestfiles.com
weakness: Improper Authentication - Generic
team_handle: harvest
created_at: '2016-07-20T15:58:50.077Z'
disclosed_at: '2016-09-10T22:00:01.258Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- improper-authentication-generic
---

# S3 bucket takeover due to proxy.harvestfiles.com

## Metadata

- HackerOne Report ID: 152584
- Weakness: Improper Authentication - Generic
- Program: harvest
- Disclosed At: 2016-09-10T22:00:01.258Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
---------

I can takeover your `███` S3 bucket. You are using https://proxy.harvestfiles.com to proxy requests to this bucket. The proxy automatically signs the requests and adds the required authorization headers for your S3 user.

However, an attacker can then simply impersonate the user and create arbitrary requests which will be signed and forwarded to the S3 bucket. 

Proof of Concept
-----------

As a proof of concept I have created a file on the bucket: █████████

This was done by issuing the following request:

```
PUT ███████ HTTP/1.1
Host: proxy.harvestfiles.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

arbitrary-write
```

Impact
--------

Of course, instead of just writing one file, I can change the access control policy and add my own account as the owner. If you check the acl: ████ 
you will see the user ██████████ has full control over the bucket and with your proxy he basically acts on our behalf.

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
