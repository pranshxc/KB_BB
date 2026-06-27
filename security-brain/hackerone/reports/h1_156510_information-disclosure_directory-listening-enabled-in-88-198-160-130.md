---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156510'
original_report_id: '156510'
title: 'Directory listening enabled in: 88.198.160.130'
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-08-04T14:18:19.756Z'
disclosed_at: '2016-09-04T12:39:10.493Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Directory listening enabled in: 88.198.160.130

## Metadata

- HackerOne Report ID: 156510
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-09-04T12:39:10.493Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
=========
The Directory Listing option is still enabled in the web server **88.198.160.130** , which displays all the files and folders contained in the directories:
 **core** 
**apps**
**config**
**lib**
**settings**
**resources**

PoC:
====
Visit the following links:
```
http://88.198.160.130/core/
http://88.198.160.130/apps/
http://88.198.160.130/config/
http://88.198.160.130/lib/
http://88.198.160.130/settings/
http://88.198.160.130/resources/
```

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
