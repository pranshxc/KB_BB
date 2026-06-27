---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '216336'
original_report_id: '216336'
title: Source Code Disclosure
weakness: Information Disclosure
team_handle: urbandictionary
created_at: '2017-03-27T05:58:22.737Z'
disclosed_at: '2019-01-08T00:44:00.842Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- information-disclosure
---

# Source Code Disclosure

## Metadata

- HackerOne Report ID: 216336
- Weakness: Information Disclosure
- Program: urbandictionary
- Disclosed At: 2019-01-08T00:44:00.842Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

URL  http://www.urbandictionary.com/phpinfo.php 

Identified Source Code
<?php echo phpinfo(); ?>

An attacker can obtain server-side source code of the web application, which can contain sensitive data - such as database connection strings, usernames and passwords - along with the technical and business logic of the application.

Impact
Depending on the source code, database connection strings, username, and passwords, the internal workings and business logic of application might be revealed. With such information, an attacker can mount the following types of attacks:
Access the database or other data resources. Depending on the privileges of the account obtained from the source code, it may be possible to read, update or delete arbitrary data from the database.
Gain access to password protected administrative mechanisms such as dashboards, management consoles and admin panels, hence gaining full control of the application.
Develop further attacks by investigating the source code for input validation errors and logic vulnerabilities.
Actions to Take
Confirm exactly what aspects of the source code are actually disclosed; due to the limitations of this type of vulnerability, it might not be possible to confirm this in all instances. Confirm this is not an intended functionality.
If it is a file required by the application, change its permissions to prevent public users from accessing it. If it is not, then remove it from the web server.
Ensure that the server has all the current security patches applied.
Remove all temporary and backup files from the web server.
Required Skills for Successful Exploitation
This is dependent on the information obtained from the source code. Uncovering these forms of vulnerabilities does not require high levels of skills. However, a highly skilled attacker could leverage this form of vulnerability to obtain account information from databases or administrative panels, ultimately leading to the control of the application or even the host the application resides on.

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
