---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '262262'
original_report_id: '262262'
title: app.mixmax.com Information Discloure on cal.mixmax.com and Not Signing out
  after Removing information grant access from Google
team_handle: mixmax
created_at: '2017-08-22T16:41:58.192Z'
disclosed_at: '2017-09-24T05:02:51.258Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# app.mixmax.com Information Discloure on cal.mixmax.com and Not Signing out after Removing information grant access from Google

## Metadata

- HackerOne Report ID: 262262
- Weakness: 
- Program: mixmax
- Disclosed At: 2017-09-24T05:02:51.258Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found that there was Email Disclosed in the source code of the public calendar link.

PoC:

1: Visit https://cal.mixmax.com/wwelatestevents
2: View Page Source 
3: Find email at the end of the page.


organizer: {"_id":"596efbabfb652b65a918d96e","services":{"google":{"email":"aliashber76@gmail.com","name":"WWE Latest Events","picture":"https://lh6.googleusercontent.com/-AHk7ZGqHTXM/AAAAAAAAAAI/AAAAAAAAAAA/APJypA3-NXTkdTrQcKP4GyDWf47674JzLw/s96-c/photo.jpg"}}},
    ownerPlanName: null,


This type of information will be disclosed and you can see the email there.

Bug No 2:

I also found that you use gmail account for login and noticed that the user didn't sign out after he had removed app access from his google account.

PoC:
1: Login to your account.
2: Move to https://myaccount.google.com/permissions and delete Mixmax from there.
3: Return to mixmax site and you will not be signed out.

Attack Scenario:

If an attacker get's access to the user's google account he will login in mix max and in this time the user will get to know and will start the process the recovering his account. After he had recovered his account he removed Mixmax from Connected apps so that no one would then be able to access his mixmax account but the attacker who is already signed in will not get signed out and can do harmful damage to the user's Mixmax account.

If you need any other information plz be free to ask.

Regards,
Ali Ashber

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
