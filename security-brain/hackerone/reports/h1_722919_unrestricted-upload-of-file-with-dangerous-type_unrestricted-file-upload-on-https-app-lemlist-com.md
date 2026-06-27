---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '722919'
original_report_id: '722919'
title: Unrestricted File Upload on https://app.lemlist.com
weakness: Unrestricted Upload of File with Dangerous Type
team_handle: lemlist
created_at: '2019-10-25T16:48:42.885Z'
disclosed_at: '2020-04-01T09:19:42.564Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- unrestricted-upload-of-file-with-dangerous-type
---

# Unrestricted File Upload on https://app.lemlist.com

## Metadata

- HackerOne Report ID: 722919
- Weakness: Unrestricted Upload of File with Dangerous Type
- Program: lemlist
- Disclosed At: 2020-04-01T09:19:42.564Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi! i found an Unrestricted File Upload on https://app.lemlist.com which let me upload anything.
File Extensions Such as .html and others should not be executed on the server side.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

* 1.) Login to https://app.lemlist.com
* 2.) Go to Settings >  Email Signature > Click the 3 Dots > Upload File
{F617850}
* 3.) Download {F617851} and Upload it 
* 4.) Right Click and Get the Link of the Uploaded File, Visit the Link.
{F617852}

## Impact

attacker can bypass upload restrictions and deface the page.

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
