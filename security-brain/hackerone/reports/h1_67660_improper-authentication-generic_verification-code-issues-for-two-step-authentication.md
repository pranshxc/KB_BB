---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67660'
original_report_id: '67660'
title: Verification code issues for Two-Step Authentication
weakness: Improper Authentication - Generic
team_handle: automattic
created_at: '2015-06-12T20:58:31.999Z'
disclosed_at: '2015-09-20T16:05:47.316Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Verification code issues for Two-Step Authentication

## Metadata

- HackerOne Report ID: 67660
- Weakness: Improper Authentication - Generic
- Program: automattic
- Disclosed At: 2015-09-20T16:05:47.316Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I noticed two issues regarding the verification code that is sent to the phone as Two-Step Authentication for Wordpress accounts. I found out that verification code sent as SMS while enabling Two-Step Authentication can be reused infinitely for login. 

Issue#1 The application does not correctly verifies the verification code for login

Steps to reproduce:
1. Log into your Wordpress account
2. Navigate to Security under Profile
3. Enable Two-Step Authentication
4. Select verify via SMS 
5. Note down the verification code (MagicCode)
6. Complete the process by selecting I am finished printing
7. Sign out from the application 
8. Log into the application by providing email/username and password
9. When application will prompt you to provide verification code, use the code(MagicCode) initially provided while enabling the 2-FA
10. Notice that you are allowed to logged in using obsolete verification code. 
11. Try it multiple times by logging out and log in by providing same MagicCode all time during 2-FA verification.

It simply kills the purpose of having second factor when you are not verifying it correctly. An attacker can use it for account take over.

Issue#2 The application does not correctly verifies the verification code for disabling Two-Step Authentication

Steps to reproduce:
1. Follow steps 1 through 6 from the Issue#1
2. After sometime, again navigate to Security and click on Two-Step Authentication
3. Click on "Disable Two-Step Authentication"
4. It will prompt for verification code that is sent to your mobile phone (note : A code has been sent to your device via SMS. You may request another code after one minute.)
5. Instead of typing the new code, use the old code(MagicCode) that was received as the first SMS during enabling 2-FA.
6. Notice that you are able to Disable Two-Step by using past verification code 

This is a weird behavior of the MagicCode. Its not time based as well. I have tried it after waiting sufficient time. There are other codes as well received during the test like the code for disabling 2-FA but they behave differently.

Currently I am trying to build attack scenario where an attacker can take advantage of this behavior but nevertheless it does not stop you from delving into the matter and fixing the issue.

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
