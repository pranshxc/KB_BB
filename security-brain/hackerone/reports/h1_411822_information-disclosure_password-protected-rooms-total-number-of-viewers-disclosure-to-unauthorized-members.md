---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411822'
original_report_id: '411822'
title: Password protected rooms total number of viewers disclosure to unauthorized
  members
weakness: Information Disclosure
team_handle: chaturbate
created_at: '2018-09-20T14:55:50.541Z'
disclosed_at: '2018-09-24T11:22:44.646Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Password protected rooms total number of viewers disclosure to unauthorized members

## Metadata

- HackerOne Report ID: 411822
- Weakness: Information Disclosure
- Program: chaturbate
- Disclosed At: 2018-09-24T11:22:44.646Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary##
Password protected rooms are supposed to be completely private, no information should be exposed if you do not have the room's password, and the UI looks like this.

{F348826}

However, through the following endpoint, It is possible to know the total number of viewers of the room even if it is password protected.
https://chaturbate.com/contest/log/{Username}/

## Steps To Reproduce:

  1.  Create a profile and add a Password to the room, lets say for testing purposes the username is "batee5a123" which is my test username.
  2. Go to users and refresh the user list (Just to make sure your are synced) and see yourself there

{F348830}

  3. Open an Incognito instance in your web browser and visit the following endpoint:
https://chaturbate.com/contest/log/batee5a123/ Or whatever your username is instead of "batee5a123", You'll find the total number of viewers there.

{F348824}

  4. For further testing, I made a second account and gave it the password and logged in, then from another browser instance I visited the same endpoint to see it is enumerating the total views and that it increased to 2 after joining with my other test account.

{F348825}

## Impact

Password protected rooms are supposed to be completely private with no exposure of any information what so ever, If even the least information exposed could be used in social engineering or blackmailing any chaturbate user.

The correct response for this matter should be like this (always give zero):

{F348823}

Or show Unauthorized message.

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
