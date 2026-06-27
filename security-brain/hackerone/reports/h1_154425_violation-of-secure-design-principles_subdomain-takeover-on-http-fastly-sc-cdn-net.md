---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154425'
original_report_id: '154425'
title: Subdomain takeover on http://fastly.sc-cdn.net/
weakness: Violation of Secure Design Principles
team_handle: snapchat
created_at: '2016-07-27T18:52:56.828Z'
disclosed_at: '2016-08-22T19:46:06.530Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 110
tags:
- hackerone
- violation-of-secure-design-principles
---

# Subdomain takeover on http://fastly.sc-cdn.net/

## Metadata

- HackerOne Report ID: 154425
- Weakness: Violation of Secure Design Principles
- Program: snapchat
- Disclosed At: 2016-08-22T19:46:06.530Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey team,

I've found a snapchat cdn domain here which had a test instance of fastly setup but did not remove the dns record when the service was cancelled. This allowed me to create a Fastly instance to take it over. I've confirmed this is a snapchat property via Censys (https://censys.io/certificates/65ba2e172a1eb85eb1071c9fd7a4e8371ef12625409890507c89a54978305558) though the risk here seems minimal at best as this domain does not appear to be used anywhere on any snapchat properties.

Repro steps:

* Visit http://fastly.sc-cdn.net/takeover.html

Recommended fix:
Removal of this record is recommended.

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
