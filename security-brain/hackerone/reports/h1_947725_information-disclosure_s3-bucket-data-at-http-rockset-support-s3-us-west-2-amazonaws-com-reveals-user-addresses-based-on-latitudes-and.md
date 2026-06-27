---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '947725'
original_report_id: '947725'
title: S3 bucket data at http://rockset-support.s3-us-west-2.amazonaws.com/ reveals
  user addresses based on latitudes and longitudes.
weakness: Information Disclosure
team_handle: rockset
created_at: '2020-07-30T09:51:44.819Z'
disclosed_at: '2020-08-05T14:38:57.976Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- information-disclosure
---

# S3 bucket data at http://rockset-support.s3-us-west-2.amazonaws.com/ reveals user addresses based on latitudes and longitudes.

## Metadata

- HackerOne Report ID: 947725
- Weakness: Information Disclosure
- Program: rockset
- Disclosed At: 2020-08-05T14:38:57.976Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

At the s3 bucket located at http://rockset-support.s3-us-west-2.amazonaws.com/, a file was found called ``data.json.15``that contains of interest latitudes and latitudes of user addresses.
{F930036}

**Steps to reproduce:**
1, Download the file in the bucket with the command:
```
aws s3 sync s3://rockset-support .
```
2. Open the file labelled ``data.json.15``.
3. For each line, there will be a set of latitudes and longitudes. Copy a single pair. 
{F930037}

4. Open Google Maps, enter the coordinates and click search.
{F930058}

## Impact

Specific user location information violates the privacy policy stated by Rockset for its users allowing both targeted phishing attacks and physical risk.

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
