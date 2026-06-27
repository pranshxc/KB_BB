---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1187018'
original_report_id: '1187018'
title: wrong url in hackerone > goes to wix.com > unconnected
weakness: Misconfiguration
team_handle: sifchain
created_at: '2021-05-06T19:48:31.668Z'
disclosed_at: '2021-05-07T18:44:11.928Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# wrong url in hackerone > goes to wix.com > unconnected

## Metadata

- HackerOne Report ID: 1187018
- Weakness: Misconfiguration
- Program: sifchain
- Disclosed At: 2021-05-07T18:44:11.928Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi there, this is a very small issue out of scope. 
Your current domain name in your hackerone program is wrong: http://sifchain.finance and moves to wix.com

## Steps To Reproduce:
  1. Login as a researcher
  2. Open the program from sifchain: https://hackerone.com/sifchain?type=team
  3. click on the public url: http://sifchain.finance
4. you will be redirected to wix.com and see message "not connected"

## Supporting Material/References:
  * screen movie: F1291486

## Impact

I think there is no impact.

**But maybe** (Maybe - because i don't know how wix.com works):
An attacker can create a new website and give his wix-project the name "sifchain.finance" *or* can connect an external domain "sifchain.finance".
The attacker can create a copy/paste fake website.
Than all researchers who click here on hackerone.com on the link will come to a fake website.
The attacker maybe can steal sifchain login data from the researchers.

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
