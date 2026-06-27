---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165280'
original_report_id: '1165280'
title: Oauth Misconfiguration Lead To Account Takeover
weakness: Improper Authorization
team_handle: reddit
created_at: '2021-05-29T05:33:22.887Z'
disclosed_at: '2021-10-21T19:53:07.170Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 8
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Oauth Misconfiguration Lead To Account Takeover

## Metadata

- HackerOne Report ID: 1165280
- Weakness: Improper Authorization
- Program: reddit
- Disclosed At: 2021-10-21T19:53:07.170Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Summary:
OAuth is a commonly used authorization framework that enables websites and web applications to request limited access to a user's account on another application. Crucially, OAuth allows the user to grant this access without exposing their login credentials to the requesting application. This means users can fine-tune which data they want to share rather than having to hand over full control of their account to a third party.

The basic OAuth process is widely used to integrate third-party functionality that requires access to certain data from a user's account. For example, an application might use OAuth to request access to your email contacts list so that it can suggest people to connect with. However, the same mechanism is also used to provide third-party authentication services, allowing users to log in with an account that they have with a different websites. 
 
Steps To Reproduce:
1. Signup with oauth method in reddit.com
2. Then logout the account 
3. Then login with the same Gmail account
4. What happens here is, now the attacker can easily log in using the victim's account which bypasses the verification methods.

For fixing this issue:
Either don't let user enter with oauth when there's already another account created with the same email or let the user enter but let him know someone else has already created an account and if it was him or not then ask him to change the password.

## Impact

Only one thing we need here and that is email address. Just by knowing that we can takeover victim's account so the impact here is quite high. Imagine email address is something you can even get if you ask so its not a hard task. But since the oauth does not authenticates the real user attackers can easily takeover the account.

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
