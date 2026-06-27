---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260221'
original_report_id: '260221'
title: Information Exposure Through Directory Listing
weakness: Information Exposure Through Directory Listing
team_handle: nextcloud
created_at: '2017-08-15T06:09:26.557Z'
disclosed_at: '2018-05-17T09:04:38.697Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: apps.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Information Exposure Through Directory Listing

## Metadata

- HackerOne Report ID: 260221
- Weakness: Information Exposure Through Directory Listing
- Program: nextcloud
- Disclosed At: 2018-05-17T09:04:38.697Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello.

I found open directories on the site https://apps.nextcloud.com, which can be viewed by any unauthorized user. There is an error at https://apps.nextcloud.com/static/. F212856
All directories and files in them, starting with `/static/` can be viewed or downloaded with all the content. Perhaps there is some kind of confidential information. 

Decision:
Disable directory browsing.  If this is required, make sure the listed files does not induce risks.

Thank you

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
