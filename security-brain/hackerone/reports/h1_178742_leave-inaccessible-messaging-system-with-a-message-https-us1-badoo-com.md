---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178742'
original_report_id: '178742'
title: Leave inaccessible messaging system with a message (https://us1.badoo.com)
team_handle: bumble
created_at: '2016-10-29T05:08:24.542Z'
disclosed_at: '2017-01-19T19:16:51.906Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
---

# Leave inaccessible messaging system with a message (https://us1.badoo.com)

## Metadata

- HackerOne Report ID: 178742
- Weakness: 
- Program: bumble
- Disclosed At: 2017-01-19T19:16:51.906Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, to test the messaging system I found a vulnerability that allows Inaccessible leave mensajaria system to another user (only required to send a message).

The vulnerability is in the system as the mobile version smiles and app do not have that system is only vulnerable version desktop

VULNERABLE https://us1.badoo.com
NOT VULNERABLE Version mobile (https://m.badoo.com/) App

Reproduction steps

1 .- Visit https://badoo.com/ and access your account
2 .- Selecione a user and send the message http: //www.ab99
3 .- The user who received the message could not read or write messages.

Exploitability

This is an easy mui vulnerability to exploit only requires sending a simple message, an attacker could selecionar massively users and leave them unable to read messages on your platform.

Technical details

This problem is in the system that generates smiles, which transforms :) to its corresponding image, to be more specific is in BuildLink of SmileViewController https://badoocdn.com//v2/en-us/-/js/ hon_v3 / page.messenger.1101.j

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
