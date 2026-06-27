---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1320242'
original_report_id: '1320242'
title: Password reset token leak on third party website via Referer header [██████████]
team_handle: mtn_group
created_at: '2021-08-26T13:18:36.239Z'
disclosed_at: '2022-09-01T20:21:48.701Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: mtnbusiness.com.ng
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Password reset token leak on third party website via Referer header [██████████]

## Metadata

- HackerOne Report ID: 1320242
- Weakness: 
- Program: mtn_group
- Disclosed At: 2022-09-01T20:21:48.701Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

██████████

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

##Steps To Reproduce:

1) Request a password reset link for a valid account on ████████
2) Click on the reset link from your link
3) Before resetting the password click on the Facebook link footer section
4) You will notice the following request in Burpsuite

## Supporting Material/References:

## Impact

As you can see in the referrer the reset token is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can compromise the user accounts easily.

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
