---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1088966'
original_report_id: '1088966'
title: Ability to invite a new member on Sandbox Program
weakness: Business Logic Errors
team_handle: security
created_at: '2021-01-27T20:32:07.106Z'
disclosed_at: '2021-04-05T21:13:40.858Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Ability to invite a new member on Sandbox Program

## Metadata

- HackerOne Report ID: 1088966
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2021-04-05T21:13:40.858Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In the description 
> HackerOne offers a sandbox for hackers to help them test program functionality for security vulnerabilities. To create a program, go here. You can select any product edition, giving you access to almost all features HackerOne offers. Hackers can create up to 30 programs in the sandbox. It is currently **not** possible to invite program members to new programs in the sandbox.

However in the Sandbox program the owner allows to invite a new Security member after estabilishing the program

## Steps to produce

1. Create a new sandbox program

2.  Go to [https://hackerone.com/{YOUR-PROGRAM}/team_members](https://hackerone.com/{YOUR-PROGRAM}}/team_members)

3. Invite any user

██████

4. As you can see you can invite a user even though in the description it says 

> It is currently **not** possible to invite program members to new programs in the sandbox.

███

██████████

## Impact

Allows the attacker to invite a ``team_member`` to the sandbox program even though its not permitted.

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
