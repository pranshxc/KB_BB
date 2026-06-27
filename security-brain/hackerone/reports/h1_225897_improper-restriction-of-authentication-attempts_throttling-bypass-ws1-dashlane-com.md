---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225897'
original_report_id: '225897'
title: Throttling Bypass - ws1.dashlane.com
weakness: Improper Restriction of Authentication Attempts
team_handle: dashlane
created_at: '2017-05-03T18:09:34.753Z'
disclosed_at: '2017-07-30T03:27:44.525Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Throttling Bypass - ws1.dashlane.com

## Metadata

- HackerOne Report ID: 225897
- Weakness: Improper Restriction of Authentication Attempts
- Program: dashlane
- Disclosed At: 2017-07-30T03:27:44.525Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description
The host at ws1.dashlane.com throttles requests based on the IP address of the user after a certain amount of repeated requests.
By adding the `X-Forwarded-For` header, an attacker can bypass the throttling completely, rendering the security measure ineffective against DOS attacks. 

# Proof of concept
1. Send a large amount of requests like the following until a `{"error":{"code":-32600,"message":"Throttled."}}` message is received.
2. Send another request with an added `X-Forwarded-For` header : 
3. The web server will respond with a successful message instead of a throttled response.

I have attached two screenshots demonstrating the proof of concept.

Thank you,

Ian

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
