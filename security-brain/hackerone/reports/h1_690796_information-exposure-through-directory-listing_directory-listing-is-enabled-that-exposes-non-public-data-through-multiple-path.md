---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '690796'
original_report_id: '690796'
title: Directory listing is enabled that exposes non public data through multiple
  path
weakness: Information Exposure Through Directory Listing
team_handle: nextcloud
created_at: '2019-09-09T08:59:58.285Z'
disclosed_at: '2020-02-01T04:39:52.072Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Directory listing is enabled that exposes non public data through multiple path

## Metadata

- HackerOne Report ID: 690796
- Weakness: Information Exposure Through Directory Listing
- Program: nextcloud
- Disclosed At: 2020-02-01T04:39:52.072Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Directory Listing is enabled on https://try.nextcloud.com and it shows out a few files on the server + The server version.

POC: https://try.nextcloud.com/assets/
        https://try.nextcloud.com/css/
        https://try.nextcloud.com/js/

## Impact

This could leak sensitive information on the server and it also allows an attacker to gain knowledge about the web-technology used by the website

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
