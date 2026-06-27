---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '371980'
original_report_id: '371980'
title: Bypass CSP  frame-ancestors at olx.co.za, olx.com.gh
weakness: UI Redressing (Clickjacking)
team_handle: olx
created_at: '2018-06-28T09:34:25.299Z'
disclosed_at: '2018-09-23T10:02:27.867Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- ui-redressing-clickjacking
---

# Bypass CSP  frame-ancestors at olx.co.za, olx.com.gh

## Metadata

- HackerOne Report ID: 371980
- Weakness: UI Redressing (Clickjacking)
- Program: olx
- Disclosed At: 2018-09-23T10:02:27.867Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

[olx.co.za](https://www.olx.co.za/) and [olx.com.gh](https://www.olx.com.gh/) both of them restrict framing by using this CSP rule:

```
content-security-policy: frame-ancestors 'self' https://*.mod-tools.com:*
```
olx.co.za:

{F313178}

olx.com.gh:

{F313179}

If we take a look at `mod-tools.com` we can see that the domain is not claimed:
```
$ dig mod-tools.com 

; <<>> DiG 9.10.3-P4-Ubuntu <<>> mod-tools.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 11998
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;mod-tools.com.			IN	A

;; Query time: 1 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Thu Jun 28 10:34:33 CEST 2018
;; MSG SIZE  rcvd: 31

```
Or an image as a POC:
{F313189}

## Impact

An attacker could claim [mod-tools.com](https://mod-tools.com/)  and from there he/she could perform clickjacking attack against `olx.co.za`, `olx.com.gh`.

{F313177}

Best,
Taha Ibrahim DRAIDIA

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
