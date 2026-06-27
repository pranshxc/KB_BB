---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7862'
original_report_id: '7862'
title: ClickJacking
weakness: UI Redressing (Clickjacking)
team_handle: localize
created_at: '2014-04-17T18:17:04.166Z'
disclosed_at: '2014-05-17T22:33:19.766Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# ClickJacking

## Metadata

- HackerOne Report ID: 7862
- Weakness: UI Redressing (Clickjacking)
- Program: localize
- Disclosed At: 2014-05-17T22:33:19.766Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.

Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.

An attacker may use this risk to invisibly load the target website into their own site and trick users into clicking on links which they never intended to. An "X-Frame-Options" header should be sent by the server to either deny framing of content, only allow it from the same origin or allow it from a trusted URIs.

Attacked PoC .

Daksh

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
