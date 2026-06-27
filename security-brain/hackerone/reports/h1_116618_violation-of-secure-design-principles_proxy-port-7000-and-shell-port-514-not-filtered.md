---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116618'
original_report_id: '116618'
title: proxy port 7000 and shell port 514 not filtered
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-02-15T18:38:29.446Z'
disclosed_at: '2016-02-20T12:12:01.196Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# proxy port 7000 and shell port 514 not filtered

## Metadata

- HackerOne Report ID: 116618
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-02-20T12:12:01.196Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

port 7000 on assets.gratipay.com was found to be open to the public. The port seems to be working on a proxy module of nginx and i was able to connect to ot by configuring my browser to use it as a proxy.

also port 514 is also found to be open and connection to it via rlogin succeeds although no substantial data is revealed.

These ports may reveal internal architecture of application and can be use to communicate to internal d=network of the server, hence should be filtered from direct interation

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
