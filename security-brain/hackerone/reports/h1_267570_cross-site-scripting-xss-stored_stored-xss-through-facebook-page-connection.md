---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267570'
original_report_id: '267570'
title: Stored XSS through Facebook Page Connection
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-09-11T16:42:06.454Z'
disclosed_at: '2020-04-04T14:56:46.377Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 65
asset_identifier: www.kitcrm.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS through Facebook Page Connection

## Metadata

- HackerOne Report ID: 267570
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-04-04T14:56:46.377Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following URL
https://kitcrm.com/users/122686/connections
displays us options to connect our several social networking accounts to kitcrm.
Once i connect my facebook account, the facebook section in above link will list out all my facebook page and will give me an option to select a business page. 
One of my facebook page name is "><img src=x onerror=alert(9)>
F220032: Screenshot from 2017-09-11 22-23-23.png 54.6KB 

Now when i click on that drop-down option an alert will pop-up.
F220033: Screenshot from 2017-09-11 22-25-20.png

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
