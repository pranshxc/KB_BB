---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164483'
original_report_id: '164483'
title: link reset problem
team_handle: phabricator
created_at: '2016-08-30T16:59:12.264Z'
disclosed_at: '2016-08-30T17:14:02.755Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
---

# link reset problem

## Metadata

- HackerOne Report ID: 164483
- Weakness: 
- Program: phabricator
- Disclosed At: 2016-08-30T17:14:02.755Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello,
i found out about an issue in your password reset links and their expiration
Steps to reproduce:
Request a password reset link to an account
Login to the account afterwards
Logout and use the link to reset the password
The link would not be expired

Now i know that the links need to expire after a certain time, but thinking logically there is no point of keeping the link alive once the user has logged in, It indicates the possibility that the user's original email has been compromised and the attacker has requested the link, This way the user's account can be compromised.

Attack Scenario:
Attacker requests the password reset link, User logs in, Link does not expire even after that. The attacker can use the link easily. Infact requesting a link when the account is logged in from a location should be prohibited to prevent compromise

I think this should be fixed,
Thanks

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
