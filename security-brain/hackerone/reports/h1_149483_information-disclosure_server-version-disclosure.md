---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149483'
original_report_id: '149483'
title: Server version disclosure
weakness: Information Disclosure
team_handle: uber
created_at: '2016-07-06T04:17:07.946Z'
disclosed_at: '2016-07-07T23:01:36.205Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 12
tags:
- hackerone
- information-disclosure
---

# Server version disclosure

## Metadata

- HackerOne Report ID: 149483
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-07-07T23:01:36.205Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi uber, maybe this is a low risk but i want to report that the __nginx__ and __openresty__ server version are being disclosed.

__For openresty:__ Accessing this url: https://chef.uberinternal.com/ will give you an error "502 Bad Gateway" but you can see on the page that the server version was disclose (openresty/1.9.3.1). See screenshot (openresty.JPG).

__For Nginx:__ When you go to this URL: __http://it-tools.uberinternal.com/__ , it will redirect to JetBrains but you will see in the response header that the __nginx/1.8.0__ version was disclosed. See screen shots (nginx_1.JPG and nginx_2.JPG)

It is important to keep secret of server versions. Similar reports here: #141125

Cheers
Japz

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
