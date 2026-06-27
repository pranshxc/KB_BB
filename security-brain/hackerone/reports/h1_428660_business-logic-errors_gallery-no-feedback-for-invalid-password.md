---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '428660'
original_report_id: '428660'
title: 'Gallery: No feedback for invalid password'
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2018-10-25T14:42:39.243Z'
disclosed_at: '2019-07-27T09:20:10.842Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: nextcloud/gallery
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Gallery: No feedback for invalid password

## Metadata

- HackerOne Report ID: 428660
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2019-07-27T09:20:10.842Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

CVSS
----

Low 3.1 [CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N)

Description
-----------

The Gallery plugin does not inform a user when password-protecting a file failed in combination with the Password Policy plugin. Because of this, files that the user will rightfully assume to be password-protected are actually publicly accessible.

POC
---

Prerequisite: Enable Gallery and Password Policy plugins & upload an image

View the image in the Gallery:

    http://192.168.0.103/nextcloud/nextcloud/index.php/apps/gallery/#dummy_192x192.png

Now click on "Share" -> "Share link" -> "Password protect" and enter a password that is in violation of the password policy (for example `vjhtdf68`).

The password will not actually be applied, as it violates the policy. However, the feedback is exactly the same as when a password is successfully set; there is no error message. 

A user will now think that the file is password-protected while it is actually publicly accessible.

Solution
---------

The error should be visibly shown, so that a user is aware that no password is set (the same way as is currently already happening in the main file view when setting a password).

## Impact

accidental disclosure of files which should be password protected.

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
