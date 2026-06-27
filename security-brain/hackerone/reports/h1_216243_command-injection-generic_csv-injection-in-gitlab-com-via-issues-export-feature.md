---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '216243'
original_report_id: '216243'
title: CSV injection in gitlab.com via issues export feature.
weakness: Command Injection - Generic
team_handle: gitlab
created_at: '2017-03-26T15:58:04.615Z'
disclosed_at: '2017-07-21T06:14:48.309Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- command-injection-generic
---

# CSV injection in gitlab.com via issues export feature.

## Metadata

- HackerOne Report ID: 216243
- Weakness: Command Injection - Generic
- Program: gitlab
- Disclosed At: 2017-07-21T06:14:48.309Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear GitLab bug bounty team,

# Summary
---

GitLab allows users to export issues as a .csv file. By injecting a payload into an issue title an attacker could exfiltrate data or execute code on the target machine. For instance, by naming an issue `=cmd|' /C calc'!A0` I am able to open up calc.exe on Windows.

# Steps to reproduce
---

1) Create an issue with `=cmd|' /C calc'!A0` as the title;
2) Export all issues (The file is sent as an email attachment);
3) Open the .csv file on a Windows machine.

**Result:** calc.exe pops up.

# Fix
---

Prefix `=`, `+`, `-` and `@` symbols with a `'` in issues when exporting them to a .csv file.

If you require any further information, feel free to contact me.

Best regards,
Ed

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
