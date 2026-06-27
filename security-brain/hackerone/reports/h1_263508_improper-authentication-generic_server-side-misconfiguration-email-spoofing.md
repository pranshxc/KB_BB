---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263508'
original_report_id: '263508'
title: Server Side Misconfiguration (EMAIL SPOOFING)
weakness: Improper Authentication - Generic
team_handle: gsa_bbp
created_at: '2017-08-26T04:54:47.208Z'
disclosed_at: '2017-09-14T20:04:28.992Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: https://github.com/18f/federalist-proxy
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Server Side Misconfiguration (EMAIL SPOOFING)

## Metadata

- HackerOne Report ID: 263508
- Weakness: Improper Authentication - Generic
- Program: gsa_bbp
- Disclosed At: 2017-09-14T20:04:28.992Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi team,
Bug Type: Server Security Misconfiguration > Mail Server Misconfiguration > Missing SPF on Email Domain 
Weakness: Improper Authentication
Description: 
i observe this when i send a email from tts-vulnerability-reports@gsa.gov through http://emkei.cz/ to email husnainiqbal02@yahoo.com and after that i check my yahoo mail i recieved it so this is due to Server Security Misconfiguration And Mail Server Misconfiguration.
Steps to reproduce:
1) Open this url http://emkei.cz/
2)Type In ''From email'' field tts-vulnerability-reports@gsa.gov or any one email of your website.
3) After That Send to the victim email like husnainiqbal02@yahoo.com in ''To'' field.
4) Write other details what you want and send it to victim email. 
5) Victim will recieve an email from TTS. 

Reccomendation: 
If you dont Find an email in inbox please check the spam folder also.


Attack scenario:

This can be dangerous ,as attacker can send some fake details or money(cash) or bounty amount like 10,00000 to someone of your users,then your user will claim back for the details. It will cause reputation loss.

PROOF OF CONCEPT:

FOR PROOF OF CONCEPT YOU CAN SEE IN SCREEN SHOT WHICH I AM ATTACHING THAT BY YOUR COMPANY MAIL I AM ABLE TO SEND ANYONE EMAIL WHATEVER I WANT. I TESTED IT ON MY OWN ACCOUNT. PLEASE SEE THE SCREEN SHOT.

THANKS 
BEST REGARDS: 
HUSNAIN IQBAL

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
