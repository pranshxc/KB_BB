---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '809'
original_report_id: '809'
title: Improperly implemented password recovery link functionality
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-01-27T20:49:36.770Z'
disclosed_at: '2014-02-27T00:54:55.437Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-authentication-generic
---

# Improperly implemented password recovery link functionality

## Metadata

- HackerOne Report ID: 809
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-02-27T00:54:55.437Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I took a look at live install of Phabricator (https://secure.phabricator.com/) and noticed, that the user gets automatically logged in after clicking the password recovery link (this link is sent to the user's mail). This authentication takes place before the user is asked to enter a new password twice. This can be used be the attacker to log in a user to the attacker's account - the attacker generates a password recovery link to his account, sends it to the user and the user becomes logged in to the attacker's account, when he clicks the link delivered by the attacker.

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
