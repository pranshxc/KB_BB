---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '968232'
original_report_id: '968232'
title: Stored XSS in collabora via user name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2020-08-27T03:14:13.126Z'
disclosed_at: '2020-09-19T02:00:06.852Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 48
asset_identifier: nextcloud/viewer
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in collabora via user name

## Metadata

- HackerOne Report ID: 968232
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2020-09-19T02:00:06.852Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Affected: collabora and nextcloud

Ubuntu 18.04.5 LTS
Nextcloud 19.0.1 snap version
collabora (CODE)

The name of the user is displayed when him joins to edit the document allowing the attacker trigger xss.

## Impact

* Set the name of the attacker account to <img src=a onerror=alert(window.parent.location)>
* Create a new document → share the document with admin or another victim → the document will appear automatically in the files of the victim as shared
* The attacker opens the document and waits until the victim also opens the document when opening it the payload is executed

{F965228}

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
