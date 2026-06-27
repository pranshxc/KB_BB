---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '53858'
original_report_id: '53858'
title: Insecure Direct Object Reference - access to other user/group DM's
weakness: Privilege Escalation
team_handle: x
created_at: '2015-03-29T17:15:04.612Z'
disclosed_at: '2015-10-03T18:48:57.984Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- privilege-escalation
---

# Insecure Direct Object Reference - access to other user/group DM's

## Metadata

- HackerOne Report ID: 53858
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2015-10-03T18:48:57.984Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello**,

I found a way to access group DM's which i don't have access to,
Conditions to be met:
- Should have been in that DM group atleast once.

Exploitation ways:
===============
- let's say they're three twitter profiles, Naruto , Goku and Eren.
- Naruto creates a DM group in between himself , Goku and Eren.
- Now Eren leaves the DM group, at this moment Goku and Naruto think that their DM's are private and Eren won't be able to see the DM's cause he just the left group.
- But Eren can still access the DM's by just navigating himself to 
`https://mobile.twitter.com/a/messages/582225197727506432/delete`

  where **582225197727506432** is the DM id.

Steps to Reproduce:
=================
- Create three profiles A,B and C
- From account A create a DM group for A, B and C
- Leave the DM group from account C 
- Now message something in the DM group from account A or account B.
- A unique DM id will be created for that message.
- Note down the DM ID and 
 From Account C navigate yourself to 
`https://mobile.twitter.com/a/messages/[DM ID]/delete`
Replace the [DM ID] with your noted DM ID in the above steps.

POC: http://i.imgur.com/j08a01n.png


**Regards
Wesecureapp**

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
