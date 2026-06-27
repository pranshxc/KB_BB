---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198673'
original_report_id: '198673'
title: HTTP-Basic Authentication on logs.nextcloud.com
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2017-01-16T05:58:51.131Z'
disclosed_at: '2017-01-17T10:05:57.294Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTP-Basic Authentication on logs.nextcloud.com

## Metadata

- HackerOne Report ID: 198673
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2017-01-17T10:05:57.294Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings,

While visiting https://logs.nextcloud.com/ , I noticed that this server use HTTP-Basic Authentication.

{F152730}

POC :
------

    GET https://logs.nextcloud.com/ HTTP/1.1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: br
    DNT: 1
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    Authorization: Basic cmJjYWZlOnJiY2FmZQ==
    Host: logs.nextcloud.com

Result : 
------

cmJjYWZlOnJiY2FmZQ== is the base64 of rbcafe:rbcafe and it's transmitted plaintext

Risk : 
------

- Vulnerable to client side attacks.
- Vulnerable to MITM attack.
- Vulenrable to Eavesdropping attack.
- Vulnerable to Brute force attacks.

Possible fix :
------

HTTP-Basic Authentication should be changed for HTTP-Digest Authentication.

Best regards
@rbcafe

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
