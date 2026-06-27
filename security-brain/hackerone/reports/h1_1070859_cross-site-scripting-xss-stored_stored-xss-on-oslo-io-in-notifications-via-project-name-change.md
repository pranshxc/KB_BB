---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1070859'
original_report_id: '1070859'
title: Stored XSS on oslo.io in notifications via project name change
weakness: Cross-site Scripting (XSS) - Stored
team_handle: logitech
created_at: '2021-01-04T02:22:21.740Z'
disclosed_at: '2021-01-05T19:06:50.031Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: '*.oslo.io'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on oslo.io in notifications via project name change

## Metadata

- HackerOne Report ID: 1070859
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: logitech
- Disclosed At: 2021-01-05T19:06:50.031Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey Logitech team.

## Summary:
It is possible for an editor on a project to rename a project to a malicious HTML element, which when opened in the notification dropdown will render and fire javascript.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Invite user to join the project and allow editor permissions.
  1. As the editor account, click on any of the projects and click rename. Insert malicious HTML there.
  1. Log in as the owner of the project directory and click on the notification bell on the top right. This will cause the XSS to fire.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

_Fig 1: Inviting the editor to project_
{F1143360}

_Fig 2: Notification Settings for Owner:_
{F1143367}

_Fig 3: Editor Changing Project name to malicious object_
{F1143363}
{F1143364}

_Fig 4: Logging in as the owner again_
{F1143361}

_Fig 5: Opening Notification Bell_
{F1143362}

## Impact

The impact of this vulnerability is that users who are invited onto projects as an editor are able to inject malicious javascript such as keyloggers to escalate their privileges or perform actions as other users.

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
