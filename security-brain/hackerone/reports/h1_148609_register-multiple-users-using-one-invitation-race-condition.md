---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148609'
original_report_id: '148609'
title: Register multiple users using one invitation (race condition)
team_handle: keybase
created_at: '2016-07-01T06:08:23.751Z'
disclosed_at: '2016-07-11T19:46:48.257Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
---

# Register multiple users using one invitation (race condition)

## Metadata

- HackerOne Report ID: 148609
- Weakness: 
- Program: keybase
- Disclosed At: 2016-07-11T19:46:48.257Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

It is possible to create multiple accounts using a single invitation_id due to a race condition bug in `/_/api/1.0/signup.json`. 
I have successfully created 8 accounts using invitation with id = 37c5a121adf23e90b875500d
The account usernames: novijosiptest[1,2,4,5,6,8,9,10] (you can delete them, I will not use them).

Steps:
1. Generate an invitation and get the link, click on the blue "I accept - join Keybase!" button
2. Input your data - email, username and passwords
3. When you click Join, a POST request is made to `/_/api/1.0/signup.json`. Quickly repeat this POST request while changing the `email` and `username` to desired values
4. Hopefully more than one account will be registered

It is also worth checking if there is a race condition when registering and cancelling an invite at the same time. I will test this out in a couple days.

Best regards,

Josip Franjković

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
