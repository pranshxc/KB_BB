---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1698006'
original_report_id: '1698006'
title: IDOR  [mtnmobad.mtnbusiness.com.ng]
team_handle: mtn_group
created_at: '2022-09-12T13:25:43.101Z'
disclosed_at: '2022-10-13T07:18:08.412Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
---

# IDOR  [mtnmobad.mtnbusiness.com.ng]

## Metadata

- HackerOne Report ID: 1698006
- Weakness: 
- Program: mtn_group
- Disclosed At: 2022-10-13T07:18:08.412Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

  1.  Go to https://mtnmobad.mtnbusiness.com.ng/#/dashboard/home with burp proxy
  1. Intercept a POST request to /app/dashboardData and review its response you will see emails and ids 
  1. Go to https://mtnmobad.mtnbusiness.com.ng/#/userProfile
  1. change name, mobile, address etc. and intercept with burp proxy
  1. change the id and the email with victim's and forward the request
  1. The changes will be saved in the victim's account


# Note:

If you already know account's email and id you can skip step 1 and 2

## Supporting Material/References:

  {F1922714}

## Impact

An attacker can change every user's account information

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
