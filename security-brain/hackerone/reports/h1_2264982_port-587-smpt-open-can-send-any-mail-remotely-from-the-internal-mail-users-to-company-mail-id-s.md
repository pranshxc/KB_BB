---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2264982'
original_report_id: '2264982'
title: 'Port 587 SMPT Open: Can send any mail remotely from the internal mail users
  to company mail id''s.'
team_handle: sidefx
created_at: '2023-11-27T11:54:03.253Z'
disclosed_at: '2024-02-01T16:06:18.126Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 61
asset_identifier: '*.sidefx.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Port 587 SMPT Open: Can send any mail remotely from the internal mail users to company mail id's.

## Metadata

- HackerOne Report ID: 2264982
- Weakness: 
- Program: sidefx
- Disclosed At: 2024-02-01T16:06:18.126Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
While, testing I thought to do nmap scan on the main domain. I found that SMTP port to be open. I tried connecting with telnet and to the surprise it allowed me to connect. Initially i tried HELO and EHLO commands and the server responded to it. Then i tried if i can mail to outsider but nope, it was relay denied from the server. Then I found out to mail id's of company and tried sending the data and boom server queued the mail.

## Steps To Reproduce:

  1. Run this command in your terminal, " nmap -p 587 206.223.178.168"(IP of the company sidefx.com), you'll see SMTP port open.
  2. now to connect to the port smtp remotely using "telnet 206.223.178.168 587" and the server gets connected.
  3. Try different commands for smtp to respond for example HELO *, EHLO *, VRFY * and other which don't harm the server, the server will respond 250 1.0.0 ok
  4. Now I tried 
   >MAIL FROM: support@sidefx.com server replied 250 2.1.0 ok
   >RCPT TO: media@sidefx.com server replied 250 2.1.0 ok
   > DATA(enter)
       subject: test mail (next line by pressing enter)
       this is test mail (next line by pressing enter)
       . ( this '.' is for ending the mail body)
   And here the server queued my mail 
{F2885814}


## Supporting Material/References:

https://exploit-notes.hdks.org/exploit/email/smtp-pentesting/ (for testing purposes)

## Impact

Attacker can remotely send the data he wants to send to the mail users of company remotely, including the user admin, root and administrator as they are verified using the VRFY to the smtp.  The attacker can also maliciously perform RCE through LFI as the server is allowing many actions to perform ( https://www.hackingarticles.in/smtp-log-poisioning-through-lfi-to-remote-code-exceution/). Attacker can send phishing links to the other mail id's as they are from the legitimate source( company's mail user).

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
