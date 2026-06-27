---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '713'
original_report_id: '713'
title: Upload profile photo from URL
weakness: Server-Side Request Forgery (SSRF)
team_handle: security
created_at: '2014-01-14T17:04:41.419Z'
disclosed_at: '2014-02-15T03:07:33.332Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Upload profile photo from URL

## Metadata

- HackerOne Report ID: 713
- Weakness: Server-Side Request Forgery (SSRF)
- Program: security
- Disclosed At: 2014-02-15T03:07:33.332Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Using this vulnerability users can upload images from any image URL. 
Just change upload type using inspect element  (from "type=file" to "type=url") , paste URL in text field and hit enter or click on "Update Profile". Your profile photo will be changed to photo from URL.

P.S  Im sorry for my bad english.

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
