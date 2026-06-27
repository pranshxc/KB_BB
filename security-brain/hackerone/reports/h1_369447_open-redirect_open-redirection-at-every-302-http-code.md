---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369447'
original_report_id: '369447'
title: OPEN REDIRECTION at every 302 HTTP CODE
weakness: Open Redirect
team_handle: brave
created_at: '2018-06-21T05:30:11.374Z'
disclosed_at: '2018-08-07T22:45:56.022Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: creators.basicattentiontoken.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# OPEN REDIRECTION at every 302 HTTP CODE

## Metadata

- HackerOne Report ID: 369447
- Weakness: Open Redirect
- Program: brave
- Disclosed At: 2018-08-07T22:45:56.022Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

#Summary
i guess every 302 HTTP CODE on 
>https://publishers.basicattentiontoken.org
possible to OpenRedirection

## Steps To Reproduce:

1. I edited the request when i got redirected from this request url

>https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca

587fb66a-9fdb-4419-9d05-f38ce41666ca = PUBLISHER_ID

>https://publishers.basicattentiontoken.org/publishers/587fb66a-9fdb-4419-9d05-f38ce41666ca

2. Add this header to the request and page willbe direct to injectedurl

>X-FORWARDED-HOST : injectedurl.com

Proof :
{F310965}

## Supporting Material/References:

  * BurpSuite
  * TextEditor

## Impact

A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.

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
