---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '937921'
original_report_id: '937921'
title: 'app.lemlist.com : Admin Panel Access'
weakness: Improper Access Control - Generic
team_handle: lemlist
created_at: '2020-07-23T09:45:36.721Z'
disclosed_at: '2020-07-23T13:20:43.778Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# app.lemlist.com : Admin Panel Access

## Metadata

- HackerOne Report ID: 937921
- Weakness: Improper Access Control - Generic
- Program: lemlist
- Disclosed At: 2020-07-23T13:20:43.778Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi team,

### Steps To Reproduce:
While doing some  analyse for javascript files in  [app.lemlist.com](https://app.lemlist.com) i found interesting endpoints . is the **admin** panal and is not protected , any normal user can access the panel .

## Steps To Reproduce:
(Add details for how we can reproduce the issue)

  1. Log into your account.
  1. visit on of the link below.

https://app.lemlist.com/admin
https://app.lemlist.com/admin/i18n
https://app.lemlist.com/admin/mailboxes/123

## Impact

Incorrect access restriction to the authorized interface.

Best Regards,
@omarelfarsaoui

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
