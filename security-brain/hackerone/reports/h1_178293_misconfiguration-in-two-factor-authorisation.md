---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178293'
original_report_id: '178293'
title: Misconfiguration in Two Factor Authorisation
team_handle: shopify
created_at: '2016-10-26T21:12:21.852Z'
disclosed_at: '2016-12-17T02:49:54.815Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
---

# Misconfiguration in Two Factor Authorisation

## Metadata

- HackerOne Report ID: 178293
- Weakness: 
- Program: shopify
- Disclosed At: 2016-12-17T02:49:54.815Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey

There seems to be a weird misconfiguration which leads to bypass of two factor authorisation

#### Scenario

1. Let's assume you have setup Two Factor Authorisation with Google Authenticator

2. You now activate `Google Apps` from `Login services` at https://shop-1.myshopify.com/admin/settings/account

3. Now your try to "Sign In with Google" `https://shop-1.myshopify.com/admin/auth/login?google_apps=1`

What's weird is no two factor code is required and you directly land in Admin Panel

#### Issue

Issue here is Two Factor Authorisation is disabled as soon as you "Sign In with Google" and now you cannot even enable it because you can't see any Two Factor Authenticator Tab in Accounts

And now when you try to simple login with correct credentials you can access Admin Panel without Two Factor Code from Google Authenticator at `https://shop-1.myshopify.com/admin/auth/login`

Also there is no indication to via mail or notification that Two Factor Authorisation has been disabled when Two Factor Authorisation is disabled
While it shouldn't be disabled in the first place

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
