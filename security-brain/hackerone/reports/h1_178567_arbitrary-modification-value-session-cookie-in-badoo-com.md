---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178567'
original_report_id: '178567'
title: Arbitrary modification value "session" (Cookie) in badoo.com
team_handle: bumble
created_at: '2016-10-28T10:08:27.732Z'
disclosed_at: '2017-06-25T01:26:40.316Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Arbitrary modification value "session" (Cookie) in badoo.com

## Metadata

- HackerOne Report ID: 178567
- Weakness: 
- Program: bumble
- Disclosed At: 2017-06-25T01:26:40.316Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Users who log on through https://m.badoo.com/ receive a session cookie named "session" whose value represents the user identifier.

I have found a way to change the value of the cookie, this error can be used to:

Leave off the application to a particular user to log on again, the attacker would have to cause the victim to visit a particular link.
https://mus1.badoo.com/es/help?platform=4&sessionId=Not_Valid

- Tricking a user to perform a certain action (eg buy credits) believe that this action is for your profile when in fact it is a profile of the attacker.

Proof of Concept
a document is attached to the PoC

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
