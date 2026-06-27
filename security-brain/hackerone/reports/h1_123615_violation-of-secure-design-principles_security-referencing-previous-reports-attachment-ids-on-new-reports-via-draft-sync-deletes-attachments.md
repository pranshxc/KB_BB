---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123615'
original_report_id: '123615'
title: 'SECURITY: Referencing  previous Reports attachment_IDs on new Reports via
  Draft_Sync DELETES Attachments'
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-03-16T12:57:02.468Z'
disclosed_at: '2016-04-30T12:21:05.322Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# SECURITY: Referencing  previous Reports attachment_IDs on new Reports via Draft_Sync DELETES Attachments

## Metadata

- HackerOne Report ID: 123615
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-30T12:21:05.322Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

***Issue***
New HackerOne exciting addition is the ability to include inline images by using their reference_ID, which is in this case {Fxxxxx}. The reference ID is bind to the its report Context_ID and cant be referenced by others (unique reference

Is seems that if the reference_ID is used in another newest report the attachment is deleted from the original report

Note: Reports must belong to the same reporter

POC
1. Create a Report with an attachment and file it to any team. Notice the reference_ID (Fxxxxx)
2. Create a new Report for any team and reference the ID via a POST in draft_Sync
 `POST /security/reports/draft_sync HTTP/1.1`
As soon as you do the POST Go to `the https://hackeone/security/reports/new`
You will see the reference_ID attachment attached.
3. Go to the report in 1. The reference_ID and attachment is deleted for the original report!

{F79192}


Hope it will be fixed!

Thanks!

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
