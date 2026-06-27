---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245340'
original_report_id: '245340'
title: Bypassing Access control, changing owner's name in a private leaderboard
weakness: Improper Access Control - Generic
team_handle: wakatime
created_at: '2017-07-02T14:19:26.869Z'
disclosed_at: '2017-07-31T21:24:02.631Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-access-control-generic
---

# Bypassing Access control, changing owner's name in a private leaderboard

## Metadata

- HackerOne Report ID: 245340
- Weakness: Improper Access Control - Generic
- Program: wakatime
- Disclosed At: 2017-07-31T21:24:02.631Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, 

I would like to mention a bug here that is regarding changing the name of the owner of a leaderboard by a member that is first shown forbidden but when you again try to change owner's name you can see the changes to name made in the pop up that appears.
Basically when I created a private leaderboard  named test1 on my account pig.wig45@gmail.com then in the next step I sent invitation to sahil9619299166@gmail.com so as this email was also mine I accepted the request to join the leaderboard and then I visited the members section  of the leaderboard through my pig.wig45@gmail.com account (owner account)

There I saw an edit option for the name of the member of leaderboard test1 that was the member with email sahil9619299166@gmail.com , so before that I opened a new settings page and made the member with email sahil9619299166@gmail.com the owner and made my account role as member , see below 

{ F199536} 

Then on the editing page when i tried to edit the name of the user to testing  with email sahil9619299166@gmail.com which had now become the owner and I was a member so I got the below forbidden error 

{ F199538}

But when I clicked on edit button again I saw the pop up saying 'Enter new name for testing ' see below pic 

{ F199540} 

So clearly I was able to bypass the access control set for the members of a leaderboard.
So please patch it .

Regards
Sahil tikoo

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
