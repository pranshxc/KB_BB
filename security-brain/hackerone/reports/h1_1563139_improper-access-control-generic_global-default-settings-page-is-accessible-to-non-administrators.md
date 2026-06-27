---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1563139'
original_report_id: '1563139'
title: Global default settings page is accessible to non-administrators
weakness: Improper Access Control - Generic
team_handle: phabricator
created_at: '2022-05-09T00:25:46.297Z'
disclosed_at: '2022-05-09T22:25:46.442Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-access-control-generic
---

# Global default settings page is accessible to non-administrators

## Metadata

- HackerOne Report ID: 1563139
- Weakness: Improper Access Control - Generic
- Program: phabricator
- Disclosed At: 2022-05-09T22:25:46.442Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If you go to /settings/, it correctly redirects to /settings/user/username/ and does not give you the option to change global default settings. However if you go straight to /settings/builtin/global/, any user can edit the global default settings. According to https://secure.phabricator.com/D16048, it's supposed to be an administrator panel.

mongoose

## Impact

At worst, you can disrupt a Phabricator installation and change the accessibility theme, language, disable everyone's notifications. But there aren't any very sensitive settings that you can modify.

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
