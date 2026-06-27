---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '368119'
original_report_id: '368119'
title: '[engineering.udemy.com] - Subdomain Takeover (ghost.io)'
weakness: Improper Access Control - Generic
team_handle: udemy
created_at: '2018-06-18T12:08:08.453Z'
disclosed_at: '2018-06-27T22:03:46.205Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- improper-access-control-generic
---

# [engineering.udemy.com] - Subdomain Takeover (ghost.io)

## Metadata

- HackerOne Report ID: 368119
- Weakness: Improper Access Control - Generic
- Program: udemy
- Disclosed At: 2018-06-27T22:03:46.205Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

Found that DNS record of `engineering.udemy.com` domain was pointing to inactive ghost.io instance. So when we visit https://engineering.udemy.com we will be notified that site doesn't exist.

{F310092}

```
$ host engineering.udemy.com
engineering.udemy.com is an alias for udemy-engineering-blog.ghost.io.
udemy-engineering-blog.ghost.io has address 141.101.114.35
udemy-engineering-blog.ghost.io has address 141.101.115.35
udemy-engineering-blog.ghost.io has address 190.93.244.35
udemy-engineering-blog.ghost.io has address 190.93.245.35
udemy-engineering-blog.ghost.io has address 190.93.246.35
```

So I've registered PRO account for 20$/month on ghost.org and created publication with the name `udemy-engineering-blog`, as a next step I configured custom DNS record for my publication.

{F310093}

CNAME record was already configured, so I could successfully pass validation and even have valid SSL certificate and now can serve content on behalf of `engineering.udemy.com`

https://engineering.udemy.com/

{F310094}

## Impact

Attacker is able to serve any content on behalf of `engineering.udemy.com` domain

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
