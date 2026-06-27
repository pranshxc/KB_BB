---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1295497'
original_report_id: '1295497'
title: EC2 Takeover at turn.shopify.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2021-08-09T08:45:17.516Z'
disclosed_at: '2022-03-28T14:21:28.665Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# EC2 Takeover at turn.shopify.com

## Metadata

- HackerOne Report ID: 1295497
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2022-03-28T14:21:28.665Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**
Hi team,
It seems that the domain **turn.shopify.com** pointed to an EC2 instance that was terminated and the DNS record wasn't updated. We managed to register a new EC2 instance with the IP that **turn.shopify.com** points to:

**Command**
```
dig turn.shopify.com
; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> turn.shopify.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5523
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;turn.shopify.com.		IN	A

;; ANSWER SECTION:
turn.shopify.com.	3600	IN	A	54.90.1.144

;; Query time: 17 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Mon Aug 09 10:41:14 CEST 2021
;; MSG SIZE  rcvd: 61
```

**URL**
``http://turn.shopify.com/0xd0m7``

**POC**
{F1404895}

Saved at:
``https://archive.ph/4ro3x``

## Impact

An EC2 takeover has the same impact as a subdomain takeover, instead of having a dangling CNAME there is a dangling A record. With it we are able to:
Serve phishing pages which are bound to be trusted, since there is no way of finding out that we are the owners. Besides, we could also get an SSL certificate to serve the content via HTTPS. For demonstration purposes we have only opened port 80.
Stored XSS and DoS, as shown in the PoC.
Privilege escalation: we will be checking upon submission of the report, it could be possible to use an XSS to exfiltrate personal information or take over accounts. A comment will be added if this is the case.
SSH sniffing: it'd be possible to open ports and install different services on the machine, amongst them an ssh or ftp server to capture credentials.
Malware distribution.
And many more, basically everything since we now have control over one of your domains.

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
