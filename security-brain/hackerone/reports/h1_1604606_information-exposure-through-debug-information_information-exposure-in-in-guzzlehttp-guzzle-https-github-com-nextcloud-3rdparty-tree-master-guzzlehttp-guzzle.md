---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1604606'
original_report_id: '1604606'
title: Information exposure in in guzzlehttp/guzzle (https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)
weakness: Information Exposure Through Debug Information
team_handle: nextcloud
created_at: '2022-06-16T21:19:11.635Z'
disclosed_at: '2022-09-16T02:52:19.205Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: nextcloud/3rdparty
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# Information exposure in in guzzlehttp/guzzle (https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)

## Metadata

- HackerOne Report ID: 1604606
- Weakness: Information Exposure Through Debug Information
- Program: nextcloud
- Disclosed At: 2022-09-16T02:52:19.205Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Affected versions of this package are vulnerable to Information Exposure which fails to strip the Authorization header on HTTP downgrade, this depency is out of date and it can leat to still authorization header.
## Steps To Reproduce:

(https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)
  Introduced through: guzzlehttp/guzzle@7.4.0, aws/aws-sdk-php@3.184.6, php-http/guzzle7-adapter@1.0.0, php-opencloud/openstack@3.1.0, microsoft/azure-storage-blob@1.5.2
  From: guzzlehttp/guzzle@7.4.0
  From: aws/aws-sdk-php@3.184.6 > guzzlehttp/guzzle@7.4.0
  From: php-http/guzzle7-adapter@1.0.0 > guzzlehttp/guzzle@7.4.0

##Fix:
You can update to 7.4.4, 6.5.7 to fix this information exposure.

## Impact

Affected versions of this package are vulnerable to Information Exposure which fails to strip the Authorization header on HTTP downgrade.

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
