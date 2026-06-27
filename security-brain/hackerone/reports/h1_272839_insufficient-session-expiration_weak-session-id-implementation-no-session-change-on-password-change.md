---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272839'
original_report_id: '272839'
title: Weak Session ID Implementation - No Session change on Password change
weakness: Insufficient Session Expiration
team_handle: unikrn
created_at: '2017-09-28T21:50:41.561Z'
disclosed_at: '2017-10-05T16:03:13.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Weak Session ID Implementation - No Session change on Password change

## Metadata

- HackerOne Report ID: 272839
- Weakness: Insufficient Session Expiration
- Program: unikrn
- Disclosed At: 2017-10-05T16:03:13.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** [Weak session id implementation]

**Description:** [Unikrn does not change session id after password is changed. Reusing same session ids, after password is changed is highly risky. 
Example scenario: Hacker has successfully brute forced the password of a victim and has access to the account. The victim notices that something's off and chooses to change the password of the account. Hacker has still full access to the account, even after the password is changed, because of the working session id that he got from the server when he logged in to the victim's account.]


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. [Intercept requests when logged in to unikrn and retrieve current session id]
  2. [Change the password of the user]
  3. [Do the step 1 again and compare the session id]

## Supporting Material/References:

If necessary, check my Proof of Concept video.

https://drive.google.com/file/d/0B28KqsVY5jK6aVdTYzg5RTNMcGM/view

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
