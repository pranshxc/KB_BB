---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1017189'
original_report_id: '1017189'
title: Blind Stored XSS on https://█████████ after filling a request at https://█████
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2020-10-23T17:05:28.616Z'
disclosed_at: '2021-03-11T20:55:55.396Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS on https://█████████ after filling a request at https://█████

## Metadata

- HackerOne Report ID: 1017189
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:55:55.396Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

When you submit a request at https://██████████, the content is being sent to the administrators of the application, and you will be presented with your request status at https://████

The Description field at the request status page is prone to stored xss and blind stored XSS injection, because there is no sanitization on the input being inserted.

As for now this is self (because the link is for the account), i'm 100% sure that when an administrator will check the request his details will get sent to my email, and i have a xss payload stored on my user.

████████

## Step-by-step Reproduction Instructions

1. Register to https://██████████ / login to my account (████)
2. Navigate to https://███
3. Craft your XSS payload on the description window
4. Submit your request
5. Navigate to https://█████████
6. The javascript will execute.

## Suggested Mitigation/Remediation Actions
Sanitizing the input being inserted into the description window field.

##Best regards
nagli

## Impact

Stored blind XSS  on the pac.whs.mil website which could lead to administrator credentials being leaked.

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
