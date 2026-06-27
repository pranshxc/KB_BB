---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148911'
original_report_id: '148911'
title: User enumeration  via Password reset page [Minor]
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-07-02T20:22:41.788Z'
disclosed_at: '2016-07-02T20:44:55.473Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# User enumeration  via Password reset page [Minor]

## Metadata

- HackerOne Report ID: 148911
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2016-07-02T20:44:55.473Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey, I've found a 'minor' issue in bridge.cspr.ng [CMS Airship]

The issue is 'username enumeration' 

Means, an attacker can know that if a user exists or not; just by noticing the error! So, once the attacker knows that a user exists, he can launch a *brute force* attack against it!

### Steps of replication
1. Go to password reset page
2. Enter an username which exists, there would be no error, and it will be redirected to login page
3. Enter an username which doesn't exists, there would be an error saying something like 'user account doesn't exists etc..'

### Mediation
- Error should be same in both conditions like, every time it should redirect to login page; or you can also fix by adding this: "If email/username exists in our DB, an email for your password reset will be sent!" etc..

Hope you'll fix this soon! 

Thanks
-Ahsan

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
