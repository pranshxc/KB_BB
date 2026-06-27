---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116621'
original_report_id: '116621'
title: server calendar and server status available to public
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-02-15T18:52:40.186Z'
disclosed_at: '2016-02-20T12:12:30.378Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- information-disclosure
---

# server calendar and server status available to public

## Metadata

- HackerOne Report ID: 116621
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-02-20T12:12:30.378Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

It was found that a calendar containing information about various tasks to be performed by the server admin can be viewed by any user.

link: http://inside.gratipay.com/appendices/calendar

it reveals stuff link data of expiration of ssl certificate, lastpass accounts, etc

further important entries that might entered in the future may contain critical data and hence access to this link should only be to concerned personnel

Server status - server load, bandwidth, database connections, etc revealed via public link

link: http://inside.gratipay.com/appendices/health

This link reveals important information about the server load and other information and can aid an attacker for other atacks

These links belong to the inside.fratiplay.com which says that t is for the internal employees only yet the domain is accessible publically.

Access to this domain should be restricted to the internal employees only.

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
