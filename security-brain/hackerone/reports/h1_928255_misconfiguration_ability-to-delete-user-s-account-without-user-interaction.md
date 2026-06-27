---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '928255'
original_report_id: '928255'
title: Ability To Delete User(s) Account Without User Interaction
weakness: Misconfiguration
team_handle: gitlab
created_at: '2020-07-20T21:34:45.676Z'
disclosed_at: '2021-03-17T20:11:03.367Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 215
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# Ability To Delete User(s) Account Without User Interaction

## Metadata

- HackerOne Report ID: 928255
- Weakness: Misconfiguration
- Program: gitlab
- Disclosed At: 2021-03-17T20:11:03.367Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary:
Gitlab allows its user to exercise their GDPR rights (Right to Access/Delete) user data by sending an email to gdpr-request@gitlab.com however gitlab team doesn't ask for security question(i.e Date Of Birth) before deleting the user account moreover doesn't authenticate the incoming emails from their  instance which allows an attacker to delete user accounts without user interaction :
██████

### Steps to reproduce
1. Send an spoofed email from victim's email address to gdpr-request@gitlab.com from a reputable SMTP (e.g: Sendgrid):
███████
2. Victim will receive the following  confirmation email:

{F914565}
3. In the next few days victim's account will be deleted :

██████

### Fix :
* Add second verification i.e ask for DOB,Government ID.

## Impact

Since Gitlab doesn't verify the request with an Valid ID before triggering Right to Access/Deletion this breaches the GDPR Law(Article 15) & moreover allows an attacker to delete User Accounts without user interaction.

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
