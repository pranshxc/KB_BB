---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1272478'
original_report_id: '1272478'
title: IDOR Leads To Account Takeover Without User Interaction
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mtn_group
created_at: '2021-07-21T18:40:29.114Z'
disclosed_at: '2022-09-04T13:23:03.840Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: mtnbusiness.com.ng
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR Leads To Account Takeover Without User Interaction

## Metadata

- HackerOne Report ID: 1272478
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mtn_group
- Disclosed At: 2022-09-04T13:23:03.840Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team,
There's IDOR Bug on this subdomain `mtnmobad.mtnbusiness.com.ng` leads to account takeover, More details check the Poc. 

## Steps To Reproduce:

  1. Create two accounts on `mtnmobad.mtnbusiness.com.ng` and both accounts verify the emails from your email inbox
  2. Login to attacker account on Browser A Go to update Profile Try to update the address for example and Capture the Request with burp send it to `Repeater`
{F1384484}
3. Login to Victim account on browser B do the same to get the victim `ID` you can Grab his ID without sending this request to `Repeater`
4. Go to the Attacker Request You sent to `Repeater` Change `/ID` with the Victim's `ID` you Grabbed From Step 3 Then change `Email` with different email, you need to change the `username` parameter not the `email` see this screenshot, Leave the email as your attacker email. the `username` Value is email and just update that one.

{F1384509} 
5.  Go Reset the Password (act like you don't know the Pass XD), login and successfully account Takeover without User Interaction

## Supporting Material/References:
--Check this Video :
{F1384553}

## Impact

Full account Takeover without user interaction

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
