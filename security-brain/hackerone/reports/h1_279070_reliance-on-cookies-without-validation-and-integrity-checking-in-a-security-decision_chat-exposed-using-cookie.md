---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '279070'
original_report_id: '279070'
title: Chat exposed using cookie
weakness: Reliance on Cookies without Validation and Integrity Checking in a Security
  Decision
team_handle: legalrobot
created_at: '2017-10-18T10:19:29.098Z'
disclosed_at: '2017-10-19T22:18:21.348Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- reliance-on-cookies-without-validation-and-integrity-checking-in-a-security-decision
---

# Chat exposed using cookie

## Metadata

- HackerOne Report ID: 279070
- Weakness: Reliance on Cookies without Validation and Integrity Checking in a Security Decision
- Program: legalrobot
- Disclosed At: 2017-10-19T22:18:21.348Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

###Hello
**Broken authentication and session management:** Attacker can use cookies of an authenticated user to reads and write the chat on the behalf of user and miss guide the legalrobot team.

**Steps to reproduce:**
 * Sign-in https://app.legalrobot.com/sign-in
 * Check the cookies of domain [legaltobot.com]
 * Cookie responsible for this attack is in attachment [cook.JPG] 
  - name: intercom-session-nmyyq5i5
 * Copy the information of above cookie
 * Signed-out from the account and reuse the cookie by using and cookie editor.
 * As you use the cookie the signing screen will look like attachment [screenshot.JPG]

**Scope:**
While exploiting this cookie I have found that after **Logged out** from legalrobot account this cookie can be used means the session for this cookie is still alive and doesn't destroy by the server.

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
