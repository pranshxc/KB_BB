---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1394982'
original_report_id: '1394982'
title: Unathorised access to admin endpoint on plus-website-staging5.shopifycloud.com
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2021-11-09T00:38:01.820Z'
disclosed_at: '2021-12-03T12:50:10.419Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Unathorised access to admin endpoint on plus-website-staging5.shopifycloud.com

## Metadata

- HackerOne Report ID: 1394982
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2021-12-03T12:50:10.419Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
https://plus-website-staging5.shopifycloud.com/admin/ allows to access/modify and delete partners data.
While the environment seems to be staging, partner's/clients contact details look pretty real.

##Sorry:  
During the testing, I've created Test111 partner account, trying to escalate the issue, however can't find an option to delete it :| So far I  did receive some DNS interaction on my collaboration server, but I've decided to stop testing and ask first. Please let me know if I can play around and try escalating it to RCE or SQLi or something else (If it's matters to you)

## Shops Used to Test:
None

## Relevant Request IDs:
061890664b777d5f7e5cc84eefa5c8c5

## Steps To Reproduce:
Go to https://plus-website-staging5.shopifycloud.com/admin/ and check the administrative menu
█████████

Kind Regards,
j0j0

## Impact

Partners and customers data leakage, probably the issue can be escalated to something more impactful.

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
