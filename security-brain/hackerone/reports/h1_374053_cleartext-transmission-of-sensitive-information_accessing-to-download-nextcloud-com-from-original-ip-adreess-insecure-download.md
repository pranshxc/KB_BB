---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '374053'
original_report_id: '374053'
title: Accessing to download.nextcloud.com from original ip adreess | insecure Download
weakness: Cleartext Transmission of Sensitive Information
team_handle: nextcloud
created_at: '2018-06-29T21:53:29.032Z'
disclosed_at: '2018-07-12T09:31:02.185Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: download.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Accessing to download.nextcloud.com from original ip adreess | insecure Download

## Metadata

- HackerOne Report ID: 374053
- Weakness: Cleartext Transmission of Sensitive Information
- Program: nextcloud
- Disclosed At: 2018-07-12T09:31:02.185Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team ,
##Summary
I found that when I can access from original ip to the web site ,.This disable Https secure connection.
##Description
First I make DNS Lookup to find the ip adress 
`download.nextcloud.com has address 88.198.160.133`
{F313820}
Now When I open The website from download.nextcloud.com I see it's over ssl so Can download securily .
{F313821}
But when I Enter  88.198.160.133 I also access the site so It's not secure to download .
{F313822}
Also this disable many protection when downloading .

## Impact

The user download your app over insecure connection.

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
