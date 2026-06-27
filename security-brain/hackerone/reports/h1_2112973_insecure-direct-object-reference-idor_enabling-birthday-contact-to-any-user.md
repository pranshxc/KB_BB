---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2112973'
original_report_id: '2112973'
title: Enabling Birthday Contact to any user
weakness: Insecure Direct Object Reference (IDOR)
team_handle: nextcloud
created_at: '2023-08-16T20:50:07.494Z'
disclosed_at: '2023-11-21T05:23:11.954Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: nextcloud/calendar
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Enabling Birthday Contact to any user

## Metadata

- HackerOne Report ID: 2112973
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: nextcloud
- Disclosed At: 2023-11-21T05:23:11.954Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Was able to enable ` Birthday Contacts ` any User, Admin, SuperAdmin. from a low privileged user.

## Steps To Reproduce:
- Navigate to Calendar. 
- At the very bottom find calendar settings 
- Click on `Enable Birthday Contacts ` 
- Intercept the following request 

```
POST /remote.php/dav/calendars/{userId}

<x3:enable-birthday-calendar xmlns:x3="http://nextcloud.com/ns"/>
```

## Impact

Users with low privileges enable the "Birthday Contacts" feature for any user, including Admins and SuperAdmins, within the Nextcloud application. By following a simple set of steps, an attacker could navigate to the Calendar section, access the calendar settings, enable the "Birthday Contacts" feature, and intercept a specific request to achieve this unauthorized action.

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
