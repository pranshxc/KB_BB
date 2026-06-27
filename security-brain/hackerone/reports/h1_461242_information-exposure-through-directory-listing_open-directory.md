---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '461242'
original_report_id: '461242'
title: Open Directory
weakness: Information Exposure Through Directory Listing
team_handle: ratelimited
created_at: '2018-12-12T13:24:14.576Z'
disclosed_at: '2018-12-24T10:17:36.375Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: ratelimited.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Open Directory

## Metadata

- HackerOne Report ID: 461242
- Weakness: Information Exposure Through Directory Listing
- Program: ratelimited
- Disclosed At: 2018-12-24T10:17:36.375Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:** A misconfigured server can show a directory listing, which could potentially yield sensitive information to an attacker. 

**Solution** :     
1.  Disable directory listings in the web- or application-server configuration by default.
2. Restrict access to unnecessary directories and files.
3. Create an index (default) file for each directory.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. go to ratelimited.me
  2. right click on and image and open it
  3.  go to this url https://ratelimited.me/assets/
  4. Click on parent directory
  5. now you can access all the folders shown


Some Examples :
1. https://ratelimited.me/assets/sass/material-kit/sections/
2. https://ratelimited.me/assets/sass/material-kit/plugins/
3. https://ratelimited.me/assets/js/
4. https://ratelimited.me/assets/css/

## Impact

A directory listing provides an attacker with the complete index of all the resources located inside of the directory. The specific risks and consequences vary depending on which files are listed and accessible.

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
