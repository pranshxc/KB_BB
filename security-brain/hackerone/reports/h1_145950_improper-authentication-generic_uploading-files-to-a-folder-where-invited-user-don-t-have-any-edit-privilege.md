---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145950'
original_report_id: '145950'
title: Uploading files to a folder where invited user don't have any EDIT privilege
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-19T23:33:59.213Z'
disclosed_at: '2016-07-19T13:06:41.966Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# Uploading files to a folder where invited user don't have any EDIT privilege

## Metadata

- HackerOne Report ID: 145950
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-07-19T13:06:41.966Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Any invited user to a shared folder with no edit privilege can create files in it through copy feature of ``Nextclod`` android app.

### Steps to reproduce it

+ Create any folder and invite a user in it without any edit privilege.
+ Now login from invited user account through android app.
+ Copy any file from your ``nextcloud`` root folder to shared folder.
+ Check nextcloud web app!! Copied file will show in shared folder

Thanks

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
