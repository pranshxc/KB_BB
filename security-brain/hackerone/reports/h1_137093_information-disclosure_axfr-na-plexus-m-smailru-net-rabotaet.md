---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137093'
original_report_id: '137093'
title: AXFR на plexus.m.smailru.net работает
weakness: Information Disclosure
team_handle: mailru
created_at: '2016-05-08T09:05:24.334Z'
disclosed_at: '2016-06-15T14:32:24.048Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# AXFR на plexus.m.smailru.net работает

## Metadata

- HackerOne Report ID: 137093
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2016-06-15T14:32:24.048Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

MacBook-Pro:subbrute isox$ dig @217.69.129.107 plexus.m.smailru.net axfr

; <<>> DiG 9.8.3-P1 <<>> @217.69.129.107 plexus.m.smailru.net axfr
; (1 server found)
;; global options: +cmd
plexus.m.smailru.net.	600	IN	SOA	ns1.mail.ru. hostmaster.mail.ru. 2300425875 900 900 1209600 300
plexus.m.smailru.net.	600	IN	NS	plexus.m.smailru.net.
plexus.m.smailru.net.	600	IN	A	217.69.129.107
mail-115.plexus.m.smailru.net. 600 IN	A	192.0.2.10
plexus.m.smailru.net.	600	IN	SOA	ns1.mail.ru. hostmaster.mail.ru. 2300425875 900 900 1209600 300
;; Query time: 143 msec
;; SERVER: 217.69.129.107#53(217.69.129.107)
;; WHEN: Sun May  8 12:04:30 2016
;; XFR size: 5 records (messages 1, bytes 187)

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
