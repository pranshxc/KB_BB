---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '227522'
original_report_id: '227522'
title: IDOR in editing courses
weakness: Insecure Direct Object Reference (IDOR)
team_handle: radancy
created_at: '2017-05-10T16:25:29.221Z'
disclosed_at: '2017-05-22T17:43:43.880Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in editing courses

## Metadata

- HackerOne Report ID: 227522
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: radancy
- Disclosed At: 2017-05-22T17:43:43.880Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description

This vulnerability consists in :
https://mijn.werkenbijdefensie.nl/instellingen/gegevens/

This vulnerability allows an attacker to edit courses that do not belong to him and remove them from the users account.
The edited course ends up in the attackers  account, but gets deleted from the account of the user that made the course.

#Proof of concept

* Create 2 accounts
* go to https://mijn.werkenbijdefensie.nl/instellingen/gegevens/
* start intercepting the requests
* add a course in one account and look at the reponse of the POST request that is made to add this course. It is a number.
* Now go to the other account also make a course.
* Edit this course, and capture the POST of the request that is made to edit the course.
* Repeat the request but change the "id" parameter to the id the course that was made in the other account.
* reload the page
* The course got removed from the creator's account and was inserted into the account of the attacker.

#impact
Attacker can remove all courses of all users by iterating trough all the course id's.

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
