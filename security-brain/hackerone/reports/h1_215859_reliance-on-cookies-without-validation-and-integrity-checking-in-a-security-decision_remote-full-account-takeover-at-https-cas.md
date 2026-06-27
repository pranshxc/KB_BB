---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215859'
original_report_id: '215859'
title: '[REMOTE] Full Account Takeover At https://██████████████/CAS/'
weakness: Reliance on Cookies without Validation and Integrity Checking in a Security
  Decision
team_handle: deptofdefense
created_at: '2017-03-24T14:49:40.993Z'
disclosed_at: '2019-10-04T15:23:30.728Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- reliance-on-cookies-without-validation-and-integrity-checking-in-a-security-decision
---

# [REMOTE] Full Account Takeover At https://██████████████/CAS/

## Metadata

- HackerOne Report ID: 215859
- Weakness: Reliance on Cookies without Validation and Integrity Checking in a Security Decision
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:23:30.728Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
A session cookie **PROD_CAS_SESSION** takes a User ID as an input, hence an attacker is able to insert his victim's User ID and takeover his victim's account. (P.S The User ID is only 6 numbers long). 
## Impact
An attacker is able to insert his victim's User ID into the cookie **PROD_CAS_SESSION** and takeover his victim's account.
## Step-by-step Reproduction Instructions

1. Go to https://██████/MOS/ (This is one of many websites you can do this from)
2. Add a cookie with the domain **███**, the name **PROD_CAS_SESSION*, and the value should be ur victim's User ID (example: **195141**).
3. Refresh the page
4. Done, you will be logged into your victim's account.

**To Get User's Info**
4. At https://████/MOS/, you will notice a dropdown on the right top corner with **Welcome (Your Victim's Name)**, click the dropdown and click **My Profile**
5. Done, you will be able to see your victim's user info.

## Suggested Mitigation/Remediation Actions
Add a more secure session value.

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
