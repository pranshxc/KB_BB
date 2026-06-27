---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '121827'
original_report_id: '121827'
title: Account Takeover
weakness: Cross-Site Request Forgery (CSRF)
team_handle: bumble
created_at: '2016-03-09T19:17:05.609Z'
disclosed_at: '2016-03-12T13:47:00.877Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Account Takeover

## Metadata

- HackerOne Report ID: 121827
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: bumble
- Disclosed At: 2016-03-12T13:47:00.877Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello this is regarding an account takeover via import image from facebook option, when we import fb photos a link with a token generated which is valid for any user and it can be use to replace user linked fb account to attacker fb account And then login via fb to takeover account

Note: I tested it on https://m.Badoo.com
-

Steps to reproduce :-
--

1 -Create two Badoo account attacker & victim and link 2 diff fb account in each of them

2- Login as 'attacker' and go to import photos via fb and copy the link from URL bar 

3- Now login as 'victim' in diffrent browser and open the link and click cancel.

4- FB account of 'victim' is replaced with FB account of 'attacker' (Removed from 'victim' one)

5-Login via attacker FB account and you will be logged in 'User' account 

Congo u just hacked victim account 

More explanation
--
Suppose a user have an account of attacker 'A' with FB linked which 'FB-of-A' and a victim account 'B' with fb linked which is 'FB-of-B' now attacker create a link to import photos from his fb and give it to victim 'B' he opens it and press cancel but this have changed his FB account 'FB-of-B' to attacker's FB account 'FB-of-A', And now attacker can login with his fb account in victim's badoo account.

I have made a PoC video on mobile so if u need i will send it or please wait i will send u PC made within mext 24 hours

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
