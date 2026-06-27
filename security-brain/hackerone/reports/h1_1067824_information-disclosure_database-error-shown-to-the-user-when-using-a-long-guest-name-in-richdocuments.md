---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1067824'
original_report_id: '1067824'
title: Database error shown to the user when using a long guest name in richdocuments
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2020-12-28T22:33:09.651Z'
disclosed_at: '2021-02-07T07:55:38.116Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Database error shown to the user when using a long guest name in richdocuments

## Metadata

- HackerOne Report ID: 1067824
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2021-02-07T07:55:38.116Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When sharing a file to a guest and the file is allow for editing, the user is asked to enter a guestname if you enter a really long value for that name you get a database error that displays sensitive information:

An exception occurred while executing 'INSERT INTO `oc_richdocuments_wopi`(`fileid`,`owner_uid`,`version`,`canwrite`,`server_host`,`token`,`expiry`,`guest_displayname`,`template_destination`,`hide_download`,`direct`,`is_remote_token`,`template_id`,`share`) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)' with params [8606022, "8JaQyYP5xM7w2PJ6", 0, true, "https:\/\/demo2.nextcloud.com\/", "hUYL4uh9Dals51BoAT2YA7WZ1IJMaCLp", 1609196332, "reallylongnameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee (Guest)", 0, false, false, false, 0, "c4A53CW6wAN2ZZa"]: SQLSTATE[22001]: String data, right truncated: 1406 Data too long for column 'guest_displayname' at row 1

Demo
{F1133198}

## Impact

Information Disclosure

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
