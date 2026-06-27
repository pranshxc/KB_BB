---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47627'
original_report_id: '47627'
title: Email Enumeration (POC)
weakness: Violation of Secure Design Principles
team_handle: enter
created_at: '2015-02-13T11:07:15.303Z'
disclosed_at: '2015-05-27T15:57:29.968Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email Enumeration (POC)

## Metadata

- HackerOne Report ID: 47627
- Weakness: Violation of Secure Design Principles
- Program: enter
- Disclosed At: 2015-05-27T15:57:29.968Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI i am opening the ticket again now i have a poc to show you
First here is the issue again:
1.log in robocoin account go to settings 2.choose change my email 3.enter your pass 4.enter any email you want to check 5.if the email isn't registered a message appears saying(the email is changed ) 6.if it is registered the message appearing is(Email address is already registered.) BY automating the process you can easily enumerate users emails . what is the impact : 1.Mass password reset requests to registered users(spam) 2.imagine a new company like robocoin want to advertise it will easily enumerate emails of robocoin and send the customers emails to convince them to join their company and leave circle this may cause you to loose some of your customers(targeted advertising through robocoin database) . there are other impact but those are most severe
Here is the fix:
I am very sorry.This was written from my mobile as i had problems regarding my Wifi.
Here is the fix: 
when a user try to assign an email that is already registered to your accounts tell him that (An error has occured)or(we have sent a verification email to your email address)or anything not revealing he is registered to you .
Here is the POC: 
i have carried the attack on sample of 350 emails to avoid server overload(attached is a poc picture
the result is by using burpsuite i can bruteforce the change email feature and enumerate users by the status in intruder attack:
200--->Not registered and can be added
500--->registered and error message
400---> this is invalid email because for example it doesn't have @ sign in it
Is this ok with you

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
