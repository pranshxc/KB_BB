---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '206359'
original_report_id: '206359'
title: Email Spoofing
weakness: Violation of Secure Design Principles
team_handle: portswigger
created_at: '2017-02-14T15:31:02.860Z'
disclosed_at: '2017-02-14T17:38:08.711Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email Spoofing

## Metadata

- HackerOne Report ID: 206359
- Weakness: Violation of Secure Design Principles
- Program: portswigger
- Disclosed At: 2017-02-14T17:38:08.711Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

There is an Email Spoofing Vulnerability.
Steps to reproduce:
1) Go to http://emkei.cz/
2) Fill "From Email" field to admin@portswigger.net or any other portswigger   email.
3) Fill the victim's address (your address) to "TO" field and fill in other details as you wish.
You will receive email from portswigger.net  admin. 
Reference:
https://hackerone.com/reports/575  

Note: If you don't find it in your inbox, see spam folder. If the victim is using Gmail account it might be in spam folder. In other mailing service like yahoo it is directly received in inbox.

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
