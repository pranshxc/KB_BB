---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '217007'
original_report_id: '217007'
title: Stored XSS in e.mail.ru (payload affect multiple users)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-03-29T14:09:16.100Z'
disclosed_at: '2017-04-17T15:37:42.570Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in e.mail.ru (payload affect multiple users)

## Metadata

- HackerOne Report ID: 217007
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2017-04-17T15:37:42.570Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

We have found a high risk level STORED XSS in e.mail.ru chat, the status change function allow to inject malicious payload in javascript & HTML, The attack affect multiple users and run in auto mode, no need a user interaction. Vulnerability affect any user that have been invited to your chat on e.mail.ru domain. The criticality of the vulnerability is high because it affect any connected user to chat without any intercation. If attacker will send a specific payload he will be allowed even to read mails, send mails with victim account. We did not try to pass the CSP, our purpose was to submit the report as soon as posibile due to the risk.

Steps to reproduce:

1. Login to first account on e.mail.ru (Lets say the account user is USER-A)
2. run virtual machine or other browser and login to second account Lets say the account user is USER-B)
3. invite yourself with both of account and accept the invitation
4. Run Burp intercept function or any other proxy intercept program on USER-A account.
5. Click on bottom chat function and update your status as online on USER-A
6. Change intercepted parametr type=online to  online"><IMG SRC=/ onerror="alert(1)"></img><"
7. Forward the intercepted request and switch to USER-B interface on VM-BOX
8. In a few second on USER-B we will notice alert box appeared with "1" text inside.

Tested on:
- Chrome
- Firefox

PoC: 
We added 4 images 
Image-1 = Shows both users connected
Image-2 = Shows intercepted request and forwarded to client
Image-3 = Shows results on firefox browser
Image-4 = Shows results on chrome browser


Best from www.afine.pl team

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
