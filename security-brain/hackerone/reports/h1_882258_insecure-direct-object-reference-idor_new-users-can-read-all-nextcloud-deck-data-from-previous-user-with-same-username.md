---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '882258'
original_report_id: '882258'
title: New users can read all Nextcloud Deck data from previous user with same username
weakness: Insecure Direct Object Reference (IDOR)
team_handle: nextcloud
created_at: '2020-05-25T13:56:48.398Z'
disclosed_at: '2021-02-14T16:22:30.969Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# New users can read all Nextcloud Deck data from previous user with same username

## Metadata

- HackerOne Report ID: 882258
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: nextcloud
- Disclosed At: 2021-02-14T16:22:30.969Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

First of all: Sorry, i know there is no scope "Deck" but both Joas and Jus pointed me to hackerone to report this security issue.

1. As an administrator create Nextcloud account "test"
2. Log in as "test"
3. Go to Deck app and create some boards, stacks and cards with personal or confidential stuff.
4. As an administrator delete Nextcloud account "test"
5. As an administrator create new Nextcloud account "test" (password doesn't need to match)
6. Log in as "test" (This might be a completely other human than in step 2!)
7. Go to Deck app and see all the secret stuff from the previous user

## Impact

Attacker is able to see confidential or private data from previous users with the same user name.

Since the private data of the users is sacred, it is a no-go that the data isn't hard deleted form the database when the user account gets deleted, but it is even worse that another user with the same username can read all the stuff (without any effort to restore data).

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
