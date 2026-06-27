---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157465'
original_report_id: '157465'
title: Host Header Injection/Redirection Attack
weakness: Command Injection - Generic
team_handle: gratipay
created_at: '2016-08-07T19:03:20.003Z'
disclosed_at: '2016-08-07T23:06:12.949Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 7
tags:
- hackerone
- command-injection-generic
---

# Host Header Injection/Redirection Attack

## Metadata

- HackerOne Report ID: 157465
- Weakness: Command Injection - Generic
- Program: gratipay
- Disclosed At: 2016-08-07T23:06:12.949Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello,

__I'm sorry for adding this, please allow me to close if you do not accept the risk involved.__

Gratipay is vulnerable to host header injection because the host header can be changed to something outside the target domain (ie. gratipay.com and grtp.co) and cause it to redirect to to that domain instead.

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.

__PoC:__
{F110430}

Regards,
Shuaib Oladigbolu

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
