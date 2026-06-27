---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '808287'
original_report_id: '808287'
title: Unrestricted file upload on the image of contacts
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2020-03-01T23:44:39.282Z'
disclosed_at: '2020-07-08T15:15:35.627Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Unrestricted file upload on the image of contacts

## Metadata

- HackerOne Report ID: 808287
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2020-07-08T15:15:35.627Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When uploading an image for a contact, on the file upload pop up window it shows that it can accept all files of any data type. For my testing I uploaded a sample executable, named 'SimpleCrackMe.exe' which doesn't do really do anything without passing parameters to it on a terminal when running it. The file was uploaded successfully.

## Impact

An attacker could upload a dangerous executable file like a virus, malware, etc.. If you don't think this is a vulnerability, please let me close the report myself so that I don't lose points

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
