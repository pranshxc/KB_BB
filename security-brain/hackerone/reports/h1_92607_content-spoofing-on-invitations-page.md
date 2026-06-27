---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92607'
original_report_id: '92607'
title: Content spoofing on invitations page
team_handle: security
created_at: '2015-10-06T17:51:10.850Z'
disclosed_at: '2015-10-21T13:04:35.724Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Content spoofing on invitations page

## Metadata

- HackerOne Report ID: 92607
- Weakness: 
- Program: security
- Disclosed At: 2015-10-21T13:04:35.724Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When you are an owner of a program on h1 , you are allowed to invite external users to access any report through email . As you invite someone , this is how the body of invitation is being sent through email :-

[link to researcher's profile] invited you to join the bug [Title Of The Bug]  for [Name of the program]

So being an owner of a program I control  [Title Of The Bug] and [Name of the program] . So I can create any program on h1 , report a bug to it , keeping the Title of that bug and name of my program as per my choice .

This is how a Verified program on h1 can spoof the body of the email leading to phishing attacks but i suppose h1 trusts all of the verified programs so this may not be a risk .

For the Unverified programs , as you invite an external user , the body of email also contains a warning which minimizes the risk of further phishing attacks BUT it's not necessary to invite someone ONLY through emails ....
For eg.
1. Attacker creates a program , reports a bug to it choosing the title of bug and name of the program as in the attached screenshot .
2.  He then sends a mail to himself thus getting an invitation id !
3. He can then personally invite someone through that invitation .

for eg . visit : https://hackerone.com/invitations/7e28fd3adb7f7bf2c155c66e534a9f69
also see the attached screenshot

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
