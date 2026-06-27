---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '287688'
original_report_id: '287688'
title: Stored XSS On Wordpress Infogram plugin
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-11-06T10:35:36.716Z'
disclosed_at: '2017-11-15T14:57:55.727Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS On Wordpress Infogram plugin

## Metadata

- HackerOne Report ID: 287688
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-11-15T14:57:55.727Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

There is a Stored XSS Vulnerability On Wordpress Infogram plugin.

**Wordpress version : 4.5**
**Infogram plugin version : 1.5.1**

After installing wordpress and infogram plugin.
I created a project to infogram with the following name  **"><img src=x onerror=prompt(0);>**  and I Created a simple report.

Then I go back to my wordpress site to add an infogram graphic using **Add from infogram** Button.

a window opens with a pop up.

Best regards,

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
