---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44727'
original_report_id: '44727'
title: Insecure Data Storage in Vine Android App
weakness: Cryptographic Issues - Generic
team_handle: x
created_at: '2015-01-22T11:40:01.178Z'
disclosed_at: '2015-06-24T05:07:26.161Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cryptographic-issues-generic
---

# Insecure Data Storage in Vine Android App

## Metadata

- HackerOne Report ID: 44727
- Weakness: Cryptographic Issues - Generic
- Program: x
- Disclosed At: 2015-06-24T05:07:26.161Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Twitter,

   - **Vulnerability Class:**OWASP M2 : Insecure Data Storage 

Every application needs to store something secret, like a website username,password, cookies etc. , internal storage is the place to do it,  android sandbox prevents other applications from accessing this data but,In vine android app  developers have chosen to store secret information without any additional encryption in place.

   - **Where I found it?**

`/data/data/co.vine.android/databases/webview.db`

   - **POC:**Please see the screenshot of SQLite database.

   - **SEVERITY:**
What is more severe than clear text username password storage and with the JavaScript and file system access enabled , Its not going to be hard for attacker to steal this info from the database or the whole database.

   - **Reference**:
I believe in basics :https://www.owasp.org/index.php/Mobile_Top_10_2014-M2


Please revert if more information needed. It will be fine for me to spare more time in this vulnerability issue.  
#:)#
**Happy to help.**

Regards.

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
