---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2033005'
original_report_id: '2033005'
title: Bypassing the block of Security Domain Restriction and normally invite blocked
  domains with special characters “İ”
weakness: Business Logic Errors
team_handle: frontegg
created_at: '2023-06-21T08:19:03.857Z'
disclosed_at: '2024-03-20T13:13:35.928Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: portal.frontegg.com
asset_type: URL
max_severity: none
tags:
- hackerone
- business-logic-errors
---

# Bypassing the block of Security Domain Restriction and normally invite blocked domains with special characters “İ”

## Metadata

- HackerOne Report ID: 2033005
- Weakness: Business Logic Errors
- Program: frontegg
- Disclosed At: 2024-03-20T13:13:35.928Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hey sub, Hope you are doing well today inshallah <3

I found a bug that allows the users to invite someone with a blocked domain in the project ..

If the owner for example made a rule that no one can invite emails of `yopmail.com` I would be able to invite them normally and break his rules with special charachters ..

We gonna use “İ” instead of “I” or “i”

## Steps to reproduce:

1. There sould be a rule at first blocking the domain for example `yopmail.com`,  add it from: **Settings ⇒ Security ⇒ Domain Restrictions ⇒ Deny Only ⇒ and add** `yopmail.com`
2. Go into your inviting dashboard from: **Settings ⇒ Users ⇒ Invite Users**
3. If we tried to invite someone now with the blocked domain, We gonna get error saying:
    
    {F2432936}
    
4. Now Let’s Invite “email@yopmaİl.com” instead of “email@yopmail.com”
5. Here we go, It’s invited successfully:
    
    {F2432937}
    
6. and I receive a message of inviation on the email normally:
    
    {F2432938}
    
7. Thank You <3

## Note:

- You can use this backup for more special chars: https://0xacb.com/normalization_table

## Impact

- Breaking the owner’s rules and inviting a blocked domain to the project
- rules violation

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
