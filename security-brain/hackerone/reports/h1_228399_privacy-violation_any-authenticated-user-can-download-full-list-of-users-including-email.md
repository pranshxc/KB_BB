---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228399'
original_report_id: '228399'
title: Any authenticated user can download full list of users, including email
weakness: Privacy Violation
team_handle: discourse
created_at: '2017-05-15T01:08:49.796Z'
disclosed_at: '2017-06-17T03:51:44.105Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- privacy-violation
---

# Any authenticated user can download full list of users, including email

## Metadata

- HackerOne Report ID: 228399
- Weakness: Privacy Violation
- Program: discourse
- Disclosed At: 2017-06-17T03:51:44.105Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The `ExportCsvController` allows users to export different types of entities, if one has guardian access:
https://github.com/discourse/discourse/blob/master/app/controllers/export_csv_controller.rb#L6

However, the guardian check only checks that the entity type is not "admin":
https://github.com/discourse/discourse/blob/master/lib/guardian.rb#L296

But the entity type "admin" does not exist anyway, so the check boils down to whether or not a user has made an export on that day. This means that once a day a user can export any of the entity types in the `ExportCsvFile` job:
https://github.com/discourse/discourse/blob/master/app/jobs/regular/export_csv_file.rb

Including:
A full user list export (names, email addresses, admin status, etc)
Staff actions
etc

As a proof of concept I was able to download a full list of users on https://try.discourse.org

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
