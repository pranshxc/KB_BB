---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '916704'
original_report_id: '916704'
title: Access control missing while viewing the attachments in the "All boards"
weakness: Insecure Direct Object Reference (IDOR)
team_handle: nextcloud
created_at: '2020-07-06T13:35:40.906Z'
disclosed_at: '2020-09-29T12:38:59.226Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Access control missing while viewing the attachments in the "All boards"

## Metadata

- HackerOne Report ID: 916704
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: nextcloud
- Disclosed At: 2020-09-29T12:38:59.226Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The vulnerability lies in the "view attachment" of the tasks . When a user uploads the file to the Task, the attachment is given a numeric number and is increased +1 on further uploads. It is easy for any user to view and download all the files uploaded to the tasks by any user. The access is not controlled with the session or csrf token.

Steps to Reproduce:
1. Connect to the server login with user A and visit the webpage. I used the provider "us.cloudamo.com"
2. Visit https://us.cloudamo.com/apps/deck and create a task.
3. Upload any file to the attachments and capture the request. The request will looks like "https://us.cloudamo.com/apps/deck/cards/8420/attachment/30" where 30 is the ID of the uploaded attachment. 
4. Login with  user B and access the URL and you should be able to view the attachment of user A.
5. Since the attachment IDs are numerical number with poor entropy can be easily brute-forced and  one can get all the uploaded attachments by all the users of the particular  provider.

## Impact

Unauthorized user can view and download the files of other users. This may leak the sensitive information of users.

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
