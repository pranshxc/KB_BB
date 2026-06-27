---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101909'
original_report_id: '101909'
title: account.ubnt.com CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: ui
created_at: '2015-11-24T21:58:43.155Z'
disclosed_at: '2016-12-05T23:50:51.984Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# account.ubnt.com CSRF

## Metadata

- HackerOne Report ID: 101909
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: ui
- Disclosed At: 2016-12-05T23:50:51.984Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good Evening Sir, 
I want to inform you that i have successfully discovered a problem on  the API (django Restfull API) you used to manage the security of 
https://account.ubnt.com
The vulnerability type : CSRF
Vulnerability description : 
An attacker create a web page with the code attached to this  report : "hacking_code.html"
then transfer the link of the file to the  victim (note victim need to be logged in to his account)
once the victim visit the link , his password will be changed immediatly to the password set by the hacker 
Note: an attacker can also change user information (name , email , etc...).
You can watch this video as proof of concept : 
Link : https://mega.nz/#!JZ1DxYyb
and to make this video private you may need to be asked for decryption key : 
the key is :  !██████

Impact : Critical as the account.ubnt.com is the site that manage all acounts on the ubnt.com (ex: community.ubnt.com , store.ubnt.com) , i see this require a quick fix and i am ready to help

How to fix this : 1st you need to enable the csrf_token of Django ; 2nd when change user information you may ask the user for his current password.


PS: if you need any help coding a solution i am ready to do this for you , I have a great knowledge on  DJango Development and i am ready to this for you for free :p 

if you need any thing urgent feel free to call me +█████████ , or mail me ! ███████

Thank you for your time
Best Regards , 
Ben khlifa Fahmi 
CO-Founder & Pentester at Tunisian Whitehats Security

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
