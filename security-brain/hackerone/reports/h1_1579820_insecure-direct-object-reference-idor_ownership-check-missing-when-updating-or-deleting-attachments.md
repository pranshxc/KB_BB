---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1579820'
original_report_id: '1579820'
title: Ownership check missing when updating or deleting attachments
weakness: Insecure Direct Object Reference (IDOR)
team_handle: nextcloud
created_at: '2022-05-24T12:53:28.655Z'
disclosed_at: '2022-07-06T17:50:56.771Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/mail
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Ownership check missing when updating or deleting attachments

## Metadata

- HackerOne Report ID: 1579820
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: nextcloud
- Disclosed At: 2022-07-06T17:50:56.771Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Ownership check is missing for attachments.

## Steps To Reproduce:

1. Open mail app
2. Compose a new message
3. Attach some file
4. Send message
5. Copy the xhr request and modify the attachment ids 
6. See that local_message_id is changed for a different user

When you compose a message and put them into the outbox to send them later we keep a reference for the attachments in oc_mail_attachments. An attacker is able to overwrite the local_message_id for an existing attachment  or delete the given row. Impact is that for the given message in the outbox the attachment is unavailable. 

- It's not possible to delete the actual attachment on file. Only the database reference. 
- It's not possible to send another person's attachment to you or someone else. 

## Supporting Material/References:

https://github.com/nextcloud/mail/blob/1752cbbba12285a4e93ec257d6e06ac1f790b171/lib/Db/LocalAttachmentMapper.php#L89-L118

## Impact

For the given message in the outbox the attachment is unavailable.

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
