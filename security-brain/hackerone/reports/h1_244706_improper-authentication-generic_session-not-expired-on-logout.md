---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244706'
original_report_id: '244706'
title: Session Not Expired On Logout
weakness: Improper Authentication - Generic
team_handle: wakatime
created_at: '2017-06-30T21:44:06.791Z'
disclosed_at: '2017-07-01T21:38:44.287Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Session Not Expired On Logout

## Metadata

- HackerOne Report ID: 244706
- Weakness: Improper Authentication - Generic
- Program: wakatime
- Disclosed At: 2017-07-01T21:38:44.287Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi Wakatime Security Team,

There is a  session management vulnerability in your website. i.e. user's session is not expiring immediately after the logout.

You can get more information of the vulnerability here - https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en

An attacker can get the user's session cookies by using Session Spoofer, Cookie Staler etc. and thus, can get the access to the user account.

# Steps To Reproduce:

1. Login into your wakatime.com account.
2. Capture any request. For example Account Settings using Burp Proxy. 
3. Logout from the website.
4. Replay the request captured in step 2 and notice it displays the proper response.

Reference From : #353

Hope you fix this soon ;)

Best Regards,
Pratyush Janghel

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
