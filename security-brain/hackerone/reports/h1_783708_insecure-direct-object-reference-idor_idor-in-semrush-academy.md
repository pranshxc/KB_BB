---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '783708'
original_report_id: '783708'
title: IDOR in semrush academy
weakness: Insecure Direct Object Reference (IDOR)
team_handle: semrush
created_at: '2020-01-26T18:35:07.634Z'
disclosed_at: '2020-02-28T16:27:07.202Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in semrush academy

## Metadata

- HackerOne Report ID: 783708
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: semrush
- Disclosed At: 2020-02-28T16:27:07.202Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#INTRODUCTION
    
##_I used two accounts to search for this vulnerability:_
- id: 5410425 email: ████-2@anosimple.com
- id: 5407773 email: ████@anosimple.com

##_IP used:_
███

##_Endpoint URL:_
https://www.semrush.com/academy/courses/userEnroll

#EXPLOITATION

##_Description of Security Issue:_
When a user clicks on the "Enroll for free" button in the course pages such as here https://www.semrush.com/academy/library/courses?spec=ALL&lang=en-US, the client makes a request like this: {F696872}.
This page registers the user to the course and returns information concerning the user and the course.
The problem lies in the fact that the server does not verify the userId belongs to the user making the request, so an attacker can pretend to be someone else by modifying the userId with that of the victim.

##_Steps needed to reproduce bug:_
1.Login to your account
2.Go to https://www.semrush.com/academy/library/courses?spec=ALL&lang=en-US
3.On burp suit, press the intercept button on
4.Click on the button "Enroll for free" on a random course
5.Forward the requests until you find this POST request: {F696872}
6.Change the userId with that of the victim and send the request
7.The request has been processed by the server

#RESOLUTION
Check that the userId belongs to the person who registers to the course.

## Impact

##_Number of people concerned:_
The bug affects all semrush academy users.

##_Exploit scenario for this vulnerability:_
An attacker can scrap semrush academy in order to have all the existing courseId or choose a particular course and recover his courseId.
Thereafter either the attacker already knows the victim's userId or he can bruteforce the userId field.
The attacker can then register a user for any course he wishes.
The attacker can also deduce according to the value of "creationDate" if the user has registered for the course or not and when.
The attacker also has access to other variables such as "engagement", "status", "userEngagement", etc...

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
