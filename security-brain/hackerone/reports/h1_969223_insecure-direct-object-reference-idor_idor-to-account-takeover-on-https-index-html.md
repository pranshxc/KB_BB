---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '969223'
original_report_id: '969223'
title: IDOR to Account Takeover on https://████/index.html
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2020-08-27T19:24:05.440Z'
disclosed_at: '2020-09-29T20:30:56.276Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR to Account Takeover on https://████/index.html

## Metadata

- HackerOne Report ID: 969223
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2020-09-29T20:30:56.276Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team!

**Summary:**

I found when you wish to update your profile on https://███████/ after your login through https://██████████/signIn/signIn.html website due to an IDOR.

This IDOR gives you the opportunity to change the origin email for the registered account by changing the ID parameter on the following request, i assume that if i would do it on the id=1 i would takeover the admin account, this is due to not requiring the OLD password to make an email change, aswell as no restriction to make POST actions on different account IDS.


**Description:**

IDOR chained to full Account Takeover on ██████ domain.

Account
## Step-by-step Reproduction Instructions

1. Register an account at https://█████████/signIn/CreateAccount.html (Attacker)
2. Login to your account and go the https://███████/signIn/account page
3. Click on the "update" button located at thetop middle, and capture the request on BURP
4. Now change the ID parameter on the request to the victims, change the email, and you successfully have managed to switch his email.

Request:

███


Video PoC:

█████

## Suggested Mitigation/Remediation Actions

1. Implementing email request change based on OLD password input
2. Returning 403/401 when user account attempts to change another user ID settings.

## Disclaimer

as you might notice the domain is https://██████/signIn/signIn.html when you sign in (.mil site), and it redirects you afterwards to https://██████████/ with the Compromised account, therefore i considered this In Scope.

Best Regards,
Nagli

## Impact

Issuing the malicious request on the victim account ID will lead to account takeover by replacing the email of the victim with the email of the attacker, and requesting a new password using the Forgot password option.

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
