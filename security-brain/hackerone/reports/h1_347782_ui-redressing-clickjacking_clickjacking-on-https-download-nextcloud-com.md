---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '347782'
original_report_id: '347782'
title: Clickjacking on https://download.nextcloud.com
weakness: UI Redressing (Clickjacking)
team_handle: nextcloud
created_at: '2019-07-24T13:15:37.331Z'
disclosed_at: '2019-11-11T15:24:09.625Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: download.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking on https://download.nextcloud.com

## Metadata

- HackerOne Report ID: 347782
- Weakness: UI Redressing (Clickjacking)
- Program: nextcloud
- Disclosed At: 2019-11-11T15:24:09.625Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

This page is vulnerable to clickjacking https://download.nextcloud.com

Steps to Reproduce:

1. Copy the following code and save it as clickjacking.html
<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://download.nextcloud.com" width="500" height="500"></iframe>
   </body>
</html>

2. Open it in browser

You can see the website is vulnerable to clickjacking

## Impact

Anyone can be tricked to download files without their intention

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
