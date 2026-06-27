---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '950881'
original_report_id: '950881'
title: IDOR when editing email leads to Account Takeover on Atavist
weakness: Insecure Direct Object Reference (IDOR)
team_handle: automattic
created_at: '2020-08-04T14:08:41.810Z'
disclosed_at: '2020-11-18T14:21:14.912Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR when editing email leads to Account Takeover on Atavist

## Metadata

- HackerOne Report ID: 950881
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: automattic
- Disclosed At: 2020-11-18T14:21:14.912Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
I created an account on Atavist and checked my settings page.
I can change my email at https://magazine.atavist.com/cms/reader/account with this request :

{F936117}

And as you can see, there is a `id` parameter on request data. It's our user ID, and it's vulnerable for IDOR. So we can change any user's email address.

Also user IDs are sequential so an attacker can change all accounts' email.

## Steps To Reproduce:

  1.Go to https://magazine.atavist.com/login and Login to your account
  1. Go to https://magazine.atavist.com/cms/reader/account and open your proxy program 
  1. Change the email and click `Save`
  1. In request, change the ID to your test account's ID
  1. Forward the request
  1. Now you can reset victim's password via https://magazine.atavist.com/forgot

## Impact

Account Takeover without user interaction

Thanks,
Bugra

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
