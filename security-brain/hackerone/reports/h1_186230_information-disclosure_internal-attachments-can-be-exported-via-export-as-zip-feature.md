---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186230'
original_report_id: '186230'
title: Internal attachments can be exported via "Export as .zip" feature
weakness: Information Disclosure
team_handle: security
created_at: '2016-11-29T03:04:52.536Z'
disclosed_at: '2016-11-30T09:18:19.878Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 257
tags:
- hackerone
- information-disclosure
---

# Internal attachments can be exported via "Export as .zip" feature

## Metadata

- HackerOne Report ID: 186230
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-11-30T09:18:19.878Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello HackerOne Team

This newly disclosed report: #182358 __Partial disclosure of report activity through new "Export as .zip" feature__ was not completely fix.

I have found that i can still view the attachment after it is being removed on the thread.

Best PoC is this #182358 since this is the newly fix and disclosed.

Steps to reproduce

  1. Go to https://hackerone.com/reports/182358
  2. Export the report as .zip
  3. Now extract the .zip file (`HackerOne_Report-security#182358.zip`)
  4. You will see that the image is still there, but base on the thread, you guys removed it on disclosed report.

I have attached the .zip file downloaded and save on my local and i can still view the removed image.

__Disclosed partially removed attachment:__ {F138022}

Regards
Japz

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
