---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188195'
original_report_id: '188195'
title: Login Hints on Admin Panel
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-12-04T11:40:18.448Z'
disclosed_at: '2016-12-05T10:27:00.336Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Login Hints on Admin Panel

## Metadata

- HackerOne Report ID: 188195
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-12-05T10:27:00.336Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

Hope you are doing fine.
I wanted to inform you regarding the enabling of the login hints on your wp-admin panel(https://nextcloud.com/wp-login.php).

Vulnerability: The admin panel shows very "specific" hint information if a hacker tries for a bruteforcing attack.

Steps to reproduce:
1. Navigate to: https://nextcloud.com/wp-login.php 

2. Enter username: "charlietango" 
    Enter password: "charlietango"
    A specific error message is shown stating "Invalid Username".(See attachment: xnc_user_err.png)

3. Now enter the following credentials:
    Enter username: "frank" 
    Enter password: "charlietango"
   A specific error message is shown stating "The password you entered for username frank is incorrect".   (See attachment: xnc_user_exist.png)

Why is this important:
As per step 3, Now the attacker knows that "frank" is an existing user in the system and multitude of attacks can be launched. At the very least, the attacker can spam the user's mailbox with several lost password requests. I believe this is not good and should be fixed.

Please do let me know your thoughts on this or if you need any more information.

Thank You,
Madhur

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
