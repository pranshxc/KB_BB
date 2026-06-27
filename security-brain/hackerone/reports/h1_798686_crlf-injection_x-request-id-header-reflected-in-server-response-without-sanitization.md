---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '798686'
original_report_id: '798686'
title: x-request-id header reflected in server response without sanitization
weakness: CRLF Injection
team_handle: radancy
created_at: '2020-02-18T08:39:04.231Z'
disclosed_at: '2020-02-22T16:58:29.872Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: '*.maximum.nl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# x-request-id header reflected in server response without sanitization

## Metadata

- HackerOne Report ID: 798686
- Weakness: CRLF Injection
- Program: radancy
- Disclosed At: 2020-02-22T16:58:29.872Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
maximum.nl

**Summary:** 
When issuing a GET request to maximum.nl, its possible to set the x-request-id header which is then reflected in the server response without any sanitization. 

**Description:**
An attacker can use this vulnerability to escalate to more advanced attacks such as CRLF injection/Web Cache poisoning, or defeat XSS defences since they are able to inject arbitrary values in server responses

## Steps To Reproduce:

Run this command in the terminal and observe the response

curl -v https://www.maximum.nl/ -H 'x-request-id: 450%0d%0a%0d%0aTest=test' | grep 'x-request-id'

## Known steps to resolve:
Sanitize the x-request-id header when setting it in header responses. Better still, set this value server side instead of using the value set in the request headers

## Impact

CRLF injection

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
