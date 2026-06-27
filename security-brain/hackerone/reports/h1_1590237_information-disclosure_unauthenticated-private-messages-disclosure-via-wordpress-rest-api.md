---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1590237'
original_report_id: '1590237'
title: Unauthenticated Private Messages DIsclosure via wordpress Rest API
weakness: Information Disclosure
team_handle: automattic
created_at: '2022-06-03T04:28:27.864Z'
disclosed_at: '2022-08-04T10:45:17.078Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: WordPress Plugins & Themes
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Unauthenticated Private Messages DIsclosure via wordpress Rest API

## Metadata

- HackerOne Report ID: 1590237
- Weakness: Information Disclosure
- Program: automattic
- Disclosed At: 2022-08-04T10:45:17.078Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnearble Plugin: Senei LMS

Hi there,
Hope you are doing well,
So, i noticed that their is an option to contact teacher on Sensei LMS which is meant to private.
By default, other user can't see the question I asked to the teacher.
But using the  `/wp-json/wp/v2/sensei-messages/<numericID>` where numeric ID can be bruteforced.
Those private questions asked to teacher is still visible to any Unauthenticated User.
{F1754958}

Steps to reproduce:
Create any course then as a student, ask question on that course.
Now, the message is visible through `/wp-json/wp/v2/sensei-messages/<numericID>` 
Sensei LMS lacks authentication in a REST API endpoint, allowing unauthenticated users to discover private questions sent between teacher and student on the site.

## Impact

Disclosure of Private Questions to Unauthenticated User.

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
