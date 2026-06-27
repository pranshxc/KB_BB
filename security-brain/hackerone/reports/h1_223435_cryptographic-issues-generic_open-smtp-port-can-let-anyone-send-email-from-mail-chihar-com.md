---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223435'
original_report_id: '223435'
title: Open SMTP port can let anyone send email from mail.chihar.com
weakness: Cryptographic Issues - Generic
team_handle: weblate
created_at: '2017-04-24T13:07:36.985Z'
disclosed_at: '2017-05-20T12:34:24.535Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
tags:
- hackerone
- cryptographic-issues-generic
---

# Open SMTP port can let anyone send email from mail.chihar.com

## Metadata

- HackerOne Report ID: 223435
- Weakness: Cryptographic Issues - Generic
- Program: weblate
- Disclosed At: 2017-05-20T12:34:24.535Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

An open SMTP port 587 can let anyone connect and send emails impersonating someone in your the company if he could enumerate the email addresses.

POC - 
1.  I performed an nmap scan and was able to find an open port 587 for SMTP
2. I did a netcat connection to it and was able to run commands such as HELO and EHLO(which is harmless)
3. I could even use commands STARTTLS and MAIL TO.
4. I can impersonate the support team of weblate and send an email to one of the employees asking them to visit a link and even though they know about phishing they might do it and hence stealing their sessionID.

The image shows few commands which I was able to run on the server.

Pretty much all the companies have strong email security policies and hence you should implement it and deny end user access to the SMTP server.

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
