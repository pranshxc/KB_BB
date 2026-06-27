---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9116'
original_report_id: '9116'
title: Unproper usage of Mobile Number that will lead to Information Disclosure
weakness: Cryptographic Issues - Generic
team_handle: mailru
created_at: '2014-04-22T15:39:25.165Z'
disclosed_at: '2014-05-22T15:42:15.073Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Unproper usage of Mobile Number that will lead to Information Disclosure

## Metadata

- HackerOne Report ID: 9116
- Weakness: Cryptographic Issues - Generic
- Program: mailru
- Disclosed At: 2014-05-22T15:42:15.073Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

We know that our mobile number is connected to some subdomains of mail.ru like calendar, cloud and etc.

I found out that using 1 Mobile Number can create or use it to MANY ACCOUNTS.

This is what I did..

I have a main account in mail.ru
Email: atomtheman@mail.ru
with Mobile Number of: 639154219078
Screen shot: [Link](http://prntscr.com/3cdgm3)

Then, I try to use the USED Mobile number in my main to connect to a NEW Account

Email: atomtheman10@gmail.com
with Mobile Number of: 639154219078 [SAME IN MY MAIN ACCOUNT]
Screen shot: [Link](http://prntscr.com/3cdh0t)

so, what is the bug here.. I choose the Information Disclosure Why?
Just what I say Mobile Numbers are connected to some subdomains like calendar, cloud and etc.

Main Account = User #1
New Account = User #2

Scenario:
so let's say in CALENDAR.
User #1 Make a PRIVATE EVENT in his calendar.mail.ru and he checked the SMS to make an aler 15 minutes before the exact event time.
Screen shot: [Link](http://prntscr.com/3cdi5c)

But because of unproper usage of Mobile Number that can use 1 mobile number to multiple accounts

the SECRET EVENT may disclose to User #2.

Get the point?

so my suggestion here is 1 MOBILE NUMBER = 1 ACCOUNT.

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
