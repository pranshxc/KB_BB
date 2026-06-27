---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '218680'
original_report_id: '218680'
title: '[buy.coinbase.com]Content Injection'
team_handle: coinbase
created_at: '2017-04-05T06:36:34.082Z'
disclosed_at: '2017-05-25T23:45:32.629Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
---

# [buy.coinbase.com]Content Injection

## Metadata

- HackerOne Report ID: 218680
- Weakness: 
- Program: coinbase
- Disclosed At: 2017-05-25T23:45:32.629Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Hello Coinbase

### Details

I'm not sure if this issue will count, i just want to make sure that is why i submit it. The parameter `code` is Vulnerable in Content Injection allowing me to inject any Text.

### Proof Of Concept

Here is my PoC:
{F173393}

and this which the text overlaps on the modal.
{F173394}

### PoC Link
`https://buy.coinbase.com/widget?code=<Content Injection here>&address=1234567890&crypto_currency=BTC`

Best Regards,
@phspade

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
