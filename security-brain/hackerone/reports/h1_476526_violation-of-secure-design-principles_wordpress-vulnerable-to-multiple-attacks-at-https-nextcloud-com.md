---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '476526'
original_report_id: '476526'
title: WordPress vulnerable to multiple attacks at https://nextcloud.com
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2019-01-08T11:41:18.970Z'
disclosed_at: '2020-03-01T13:39:43.150Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# WordPress vulnerable to multiple attacks at https://nextcloud.com

## Metadata

- HackerOne Report ID: 476526
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2020-03-01T13:39:43.150Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**summary:**
your current version of WordPress is available to multiple attacks check (INFO.php)

**available attacks:**
- Unauthenticated Arbitrary File Deletion
- lib/IPTraf.php User-Agent Header Stored XSS
- Password Creation Restriction Bypass
- wp-admin/admin.php whois Parameter Stored XSS
- XSS & IAA
- Banned IP Functionality Bypass
- XSS in Referer Header
- Username Enumeration

**POC**
I was able to enumerate some of your users check (POC.png)

## Impact

Attacker can use any of these attacks and steal a lot of information from your website
as I did with *Username Enumeration*

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
