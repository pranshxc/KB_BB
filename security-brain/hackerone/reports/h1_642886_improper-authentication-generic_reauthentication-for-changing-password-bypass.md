---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '642886'
original_report_id: '642886'
title: Reauthentication for changing password bypass
weakness: Improper Authentication - Generic
team_handle: liberapay
created_at: '2019-07-14T11:55:54.888Z'
disclosed_at: '2020-12-23T10:16:00.179Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Reauthentication for changing password bypass

## Metadata

- HackerOne Report ID: 642886
- Weakness: Improper Authentication - Generic
- Program: liberapay
- Disclosed At: 2020-12-23T10:16:00.179Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello There
So Libra Pay has this security system because of which if a malicious user tries to change the password of a logged in account, whether by session hijack or anything else he will be asked to re-enter the password before he can change it. 
But this loop hole I found in the system using which he/she can change it without even knowing the old password. How? 
Here is the reproduction steps:

Step 1. Go to accounts settings. 
Step 2. Add an email address to the email which we have access to(Remember adding an email doesn't require you to re-enter password but changing password does) 
Step 3. Confirm the email address. 
Step 4. Make it primary email. (Even this doesn't require you to re-enter password)
Step 5. Now we can change the password by reseting it through the new ema

I have checked for this in several other platforms as well but most of them were smart enough to ask me for entering password before I could change or add email address. May be you can implement the same.

Thank you.
Baibhav Anand Jha.
Security Researcher.

## Impact

A malicious user will be able to change the password without knowing the old password.

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
