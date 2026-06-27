---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '203658'
original_report_id: '203658'
title: Restricted file access when it exists in old versions of task or wiki document
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2017-02-05T20:01:34.759Z'
disclosed_at: '2017-02-06T12:04:20.169Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Restricted file access when it exists in old versions of task or wiki document

## Metadata

- HackerOne Report ID: 203658
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2017-02-06T12:04:20.169Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

mongoose

Hey! I think there is strange access rules for restricted file.

### Steps to reproduce:
1. Load by User1 file and set it access level "No one" (file Id for example 12)
2. Make wiki with text `{F12}` by User1
3. Edit new wiki page (change all text or delete) by User1
4. Try to access file from User2: http://phabricator.dev/F12 - User2 has access to file even if it has "No
 one" access level.

It happens because `{F12}` exists in old versions of wiki page and User1 can't do anything to hide his file only if he will restrict view access to entire wiki page. I think access level to file should be evaluated by current version of document, not older.

It can be reproduced also in tasks.

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
