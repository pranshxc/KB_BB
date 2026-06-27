---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '662204'
original_report_id: '662204'
title: Persistent XSS via filename in projects
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2019-07-28T10:22:56.058Z'
disclosed_at: '2020-03-01T13:18:39.631Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Persistent XSS via filename in projects

## Metadata

- HackerOne Report ID: 662204
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2020-03-01T13:18:39.631Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

CVSS
----

Medium 5.4 [CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N)

Description
-----------

Affected: Talk / Spreed 6.0.3

The name of a file is echoed without encoding when moving the mouse onto it in the projects tab of a conversation, leading to persistent XSS.

A successful attack requires an account with low-level permissions as well as a usual amount of user interaction (interacting with the project of a talk in a usual manner).

Successful exploitation allows the attacker to take over the account of the attacked user. If the attacked user is an administrator, this would allow a user full access to the application & files.

POC
--- 

To place the payload as the attacker:

- create a file named `test'"><img src=x onerror=alert(document.location)>.txt`. Share the file with the victim. 
- Create a new conversation: Talk -> new conversation -> enter a name.
- Invite the victim: Participants -> Add participant -> select the user
- Add a project: Projects -> Add a project -> Link to a file -> select the file from step 1. 

To trigger the payload as the victim: 

- open the conversation -> projects -> hover over the file symbol to trigger the payload.

## Impact

Successful exploitation allows an attacker to read any data the attacked user has access to, or to perform arbitrary requests the user can perform.

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
