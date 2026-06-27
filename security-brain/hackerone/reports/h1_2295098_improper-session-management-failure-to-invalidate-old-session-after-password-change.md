---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2295098'
original_report_id: '2295098'
title: Improper session management - Failure to invalidate old session after password
  change
team_handle: teleport
created_at: '2023-12-22T11:49:36.938Z'
disclosed_at: '2024-01-02T16:04:08.100Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 26
asset_identifier: teleport.sh
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Improper session management - Failure to invalidate old session after password change

## Metadata

- HackerOne Report ID: 2295098
- Weakness: 
- Program: teleport
- Disclosed At: 2024-01-02T16:04:08.100Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

##Failure to Invalidate Session on Password Change

Failure to invalidate a session after a password change is a vulnerability which allows an attacker to maintain access on a service. Most users have the expectation that when they reset their password, no one else can access their account. When sessions are not invalidated upon a password reset, the user's trust is broken. Applications that fail to invalidate sessions when the password is changed are more susceptible to account takeover by an attacker who has gained a foothold in a legitimate user's account.

An attacker may compromise a user's session through a variety of ways including, calling an internal post authentication page, modifying the given URL parameters, phishing a user, by manipulating a form, or by counterfeiting sessions. Once they have gained account access, an attacker may be able to change the password of the account and lock out the legitimate user. The attacker's actions are limited by the privileges of the user's account that they gain access to. This could include viewing or editing sensitive customer data, viewing or editing other user permissions.

##Steps to Reproduce

Create account at using : https://goteleport.com/signup/
Using one browser Chrome, sign into a user's account using the sign in at : https://teleport.sh/
Using a different browser Firefox , sign into the same user's account
Using Browser Chrome, change the password of the account
Using Browser Firefox, observe that the user session is still valid

##Proof of Concept (PoC)

The video below show the password change and the application failing to invalidate the session:

## Impact

##Business Impact

This vulnerability can lead to reputational damage and indirect financial loss to the company as customers may view the application as insecure. Additionally, this can cause escalations where a user knows that their account is compromised, but have no means of evicting an attacker by changing their password.

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
