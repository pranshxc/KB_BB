---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215083'
original_report_id: '215083'
title: Cleartext Password returned in JSON response
weakness: Cleartext Storage of Sensitive Information
team_handle: pushwoosh
created_at: '2017-03-21T12:12:03.109Z'
disclosed_at: '2018-03-04T06:36:23.833Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Cleartext Password returned in JSON response

## Metadata

- HackerOne Report ID: 215083
- Weakness: Cleartext Storage of Sensitive Information
- Program: pushwoosh
- Disclosed At: 2018-03-04T06:36:23.833Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Password was returned in the JSON response (For changing of password), which could be recovered by accessing the firefox.exe memory dump. The password string is persistent in the RAM (even after restarting Firefox application) until you restart the computer.

Refer to the .docx for more information

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
