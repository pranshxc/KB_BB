---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1547684'
original_report_id: '1547684'
title: Disconnecting an external login provider does not revoke session
weakness: Insufficient Session Expiration
team_handle: shopify
created_at: '2022-04-22T05:14:45.409Z'
disclosed_at: '2022-12-01T19:50:54.122Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Disconnecting an external login provider does not revoke session

## Metadata

- HackerOne Report ID: 1547684
- Weakness: Insufficient Session Expiration
- Program: shopify
- Disclosed At: 2022-12-01T19:50:54.122Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

Summary:
attacker could create a backdoor using google login function.if an attacker stole the  login password of victims throught any means. attacker could connect his/her google account and create a backdoor and attacker login with google  if the victim disconnect attacker session did  not expire and still get access beacuse of no session expire after disconnected with google account .attacker could still connect his google account again.

Steps To Reproduce:
  1. attacker stole the  login password of victims throught any means - https://accounts.shopify.com {{attacker prespective}}
  2.  attacker could connect his/her google account {{attacker prespective}}
 3. attacker login with google authentication {{attacker prespective}}
4. victim disconnect attacker session did  not expire and still get access beacuse of no session expire  in the attacker browser after disconnected with google account {{victims prespective}}
5. attacker could still connect his google account again. {{attacker prespective}}

POC video attached in this report

## Impact

no session expire after disconnected with google account an attacker can still logined to the victim account .thus an attacker could create a backdoor in victim account to login even if the victims changes the password attacker has a backdoor way to login to the account .

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
