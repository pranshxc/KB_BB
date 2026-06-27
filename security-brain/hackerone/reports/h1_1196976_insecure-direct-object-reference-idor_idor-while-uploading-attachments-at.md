---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1196976'
original_report_id: '1196976'
title: IDOR while uploading ████ attachments at [█████████]
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2021-05-14T04:39:24.550Z'
disclosed_at: '2021-06-30T20:47:06.093Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR while uploading ████ attachments at [█████████]

## Metadata

- HackerOne Report ID: 1196976
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2021-06-30T20:47:06.093Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
There is an IDOR vulnerability in uploading attachments to the ████ section where an attacker can upload attachments in other user's █████████ if there is no attachment uploaded by a user. If this vulnerability will be used with a Race condition, it can allow an attacker to upload attachments in all-new █████████ created by users.

## Impact

A user can upload attachments to other users ███.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to ██████
2. Login
3. Go to https://███/█████
4. Add a new █████████ and upload an attachment with that and submit it.
5. Send the request to the repeater.

████
6. Change the `███Id` parameter value to the victim user's ██████████ id.

█████████
7. Click on the send button and you will see `success` in response.
8. It will be uploaded in the victim user █████ section.

## Suggested Mitigation/Remediation Actions

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
