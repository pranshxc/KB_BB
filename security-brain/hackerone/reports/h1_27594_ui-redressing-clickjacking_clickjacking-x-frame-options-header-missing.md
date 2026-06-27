---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '27594'
original_report_id: '27594'
title: 'Clickjacking: X-Frame-Options header missing'
weakness: UI Redressing (Clickjacking)
team_handle: glasswire
created_at: '2014-09-09T15:55:01.653Z'
disclosed_at: '2014-10-12T12:57:34.695Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking: X-Frame-Options header missing

## Metadata

- HackerOne Report ID: 27594
- Weakness: UI Redressing (Clickjacking)
- Program: glasswire
- Disclosed At: 2014-10-12T12:57:34.695Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello. Typical simple bug.

Victim - www.glasswire.com

"It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.

Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.

An attacker may use this risk to invisibly load the target website into their own site and trick users into clicking on links which they never intended to. An "X-Frame-Options" header should be sent by the server to either deny framing of content, only allow it from the same origin or allow it from a trusted URIs." (c) https://hackerone.com/reports/17896

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
