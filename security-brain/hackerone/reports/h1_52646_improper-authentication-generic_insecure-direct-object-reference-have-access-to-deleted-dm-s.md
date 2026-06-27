---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '52646'
original_report_id: '52646'
title: Insecure direct object reference - have access to deleted DM's
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-03-19T19:01:36.118Z'
disclosed_at: '2015-10-12T04:56:07.348Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Insecure direct object reference - have access to deleted DM's

## Metadata

- HackerOne Report ID: 52646
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-10-12T04:56:07.348Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello**,

The bug is straight and simple, 
I have access to deleted DM's.
Once a DM is deleted a user/app will still be able to access the DM's using show DM endpoint

Attack Scenario
====================
Their are two accounts Sam and Molly ,
Sam Dm's Molly something important and both quickly delete the Dm's after the chat,
Sam has given access to a 3rd party app which can access his DM's.
When Sam DM's molly every DM gets a unique id like 123456
and the DM can be accessed using the following API call ,
https://api.twitter.com/1.1/direct_messages/show.json?id={DM-id}
Now let's say Sam and Molly both deleted the DM ,
but the 3rd party app can still access the deleted DM using the above end point.

Steps to reproduce
==========================
- Create 2 account's A and B
- From account A Dm account B
- Note down the Dm id , and make an api 
https://api.twitter.com/1.1/direct_messages/show.json?id=[noted-dm-id]
- Now delete the DM
- Repeat the api call 
https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376
- You will still have access to the deleted DM.

*POC: Check for video attached*



**Regards,
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
