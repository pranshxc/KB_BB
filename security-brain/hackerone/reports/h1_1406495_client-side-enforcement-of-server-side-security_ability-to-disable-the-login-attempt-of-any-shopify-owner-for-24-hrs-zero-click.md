---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1406495'
original_report_id: '1406495'
title: Ability to Disable the Login Attempt of any Shopify Owner for 24 hrs  (Zero_Click)
weakness: Client-Side Enforcement of Server-Side Security
team_handle: shopify
created_at: '2021-11-21T14:12:27.876Z'
disclosed_at: '2022-02-15T06:20:35.527Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- client-side-enforcement-of-server-side-security
---

# Ability to Disable the Login Attempt of any Shopify Owner for 24 hrs  (Zero_Click)

## Metadata

- HackerOne Report ID: 1406495
- Weakness: Client-Side Enforcement of Server-Side Security
- Program: shopify
- Disclosed At: 2022-02-15T06:20:35.527Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I Found a Bug in which Hacker Have Ability to Disable the Login Attempt of any Shopify Owner With (Zero_Click)

Summary:
----------


Proof of Concept;
-------------------

Credentials:
-------------
Victim = ███████.com (████████)

Hacker = █████████.com 

Victim Sceanrio:
-----------------
Step 1 : Victim Login to his Account (████.com)

Step 2 : For Better Security of his Account ---------> Victim Activate the 2 Factor Authentcation ( Via Mobile Phone Number)

Step 3 : 2 FA Activated Successfully -----------> Victim Logout

Attacker Scanario: (Incognito Tab)
------------------
Step 1 : Hacker Make a New Account  in shopify (███████.com)

Step 2 : Hacker Go to Manage Account -------> Choose to Activate 2 FA 

Step 3 : Hacker Enter his Mobile Number (█████████) --------> Capture the Request in Burpsuite

Step 4 : Hacker Change the Mobile Number (████) to (███████) --------> Forward the Request

Step 5 : Hacker Logout -------> Login again

Step 6 : Now Hacker Tap Multiple times in "RESEND CODE " --------> untill Server Reflect Stop
████████

Step 7 : Now Hacker Stop Finally


Victim Sceanrio: (Again)
------------------------

Step 1 : Victim Want to Login to his Shopify Account

Step 2 : Victim Enter Email and Password --------> Server Redirect to 2 FA page

Step 3 : Here Victim See So many OTP Code But Recent Code Still Not Arrive --------> Victim Click Resend But Server Block the Attempt

As a Result Victim not Allowed to Login to his Account

Zero_Click Vulnerbaility that Will Impact many Shopify Users Who Use Mobile Number as a method of 2 FA Verification


POC Video:
-----------
████


Please Let me Know if You have any doubt

Thank You

Regards~
saurabhsankhwar3

## Impact

1. In Real World Attacker Perform a BruteForce Attack on 2 FA page (infinite Time) --------> So that Server Not able to send correct OTP to Real Victim

2. There is Improper Security While Setting 2 FA via Mobile Phone

3. Hacker try to Disable Login Attempt of any Shopify owner just By Knowing Which Mobile Number He/She used For Enabling 2 FA in his Account

4 . Violation of Security Design Priciple

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
