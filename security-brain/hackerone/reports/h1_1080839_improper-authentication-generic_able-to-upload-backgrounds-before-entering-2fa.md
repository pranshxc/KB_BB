---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1080839'
original_report_id: '1080839'
title: Able to upload backgrounds before entering 2FA
weakness: Improper Authentication - Generic
team_handle: cs_money
created_at: '2021-01-18T14:02:39.245Z'
disclosed_at: '2021-02-03T14:37:30.631Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: 3d.cs.money
asset_type: URL
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# Able to upload backgrounds before entering 2FA

## Metadata

- HackerOne Report ID: 1080839
- Weakness: Improper Authentication - Generic
- Program: cs_money
- Disclosed At: 2021-02-03T14:37:30.631Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi Team, 
I am able to see and use uploaded backgrounds and able to upload new ones without proper authentication of 2FA. I hope you remember this report #993786.

## Steps To Reproduce:

  1. Login with a steam account and enable 2FA.
  1. Now logout your account. Clear all the cookies.
  1. Now again login into your account now don't enter the 2FA code.
  1. Go to the 3d.cs.money
  1. If you are a Prime subscriber you are able to upload the custom backgrounds by pressing the "ctrl+v" combination. If you have already uploaded some backgrounds you are able to see those too.

## Supporting Material/References:
Please check the attachment F1162263.

## Impact

Able to access subdomain without proper authentication.
It should be accessible after the proper authentication.
Thanks

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
