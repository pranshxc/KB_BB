---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '74147'
original_report_id: '74147'
title: Potential for financial loss, negative Values for "Buy fee" and "Sell Fee"
weakness: Violation of Secure Design Principles
team_handle: enter
created_at: '2015-07-06T16:12:45.378Z'
disclosed_at: '2015-11-26T20:49:47.993Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Potential for financial loss, negative Values for "Buy fee" and "Sell Fee"

## Metadata

- HackerOne Report ID: 74147
- Weakness: Violation of Secure Design Principles
- Program: enter
- Disclosed At: 2015-11-26T20:49:47.993Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Issue**
It is possible to set negative values for the Buy Fee and Sell Fee, which will cause unexpected transfers etc. 
as these settings override the settings at the location.

**PoC**
1. Go to the Operator Wallet's Settings.
2. Click on the users tab.
3. Select any user. 
4. Go to settings tab of that user.
5. Select any kiosk.
6. Click on Save .Capture the request and set negative values for Sell Fee and Buy Fee.

To verify, next time when you try to view these settings, the server responds with the set negative values.

Thanks
crab

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
