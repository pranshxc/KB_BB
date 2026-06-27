---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409701'
original_report_id: '409701'
title: SSRF in hatchful.shopify.com
weakness: Server-Side Request Forgery (SSRF)
team_handle: shopify
created_at: '2018-09-14T05:22:39.504Z'
disclosed_at: '2019-04-04T13:09:45.098Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in hatchful.shopify.com

## Metadata

- HackerOne Report ID: 409701
- Weakness: Server-Side Request Forgery (SSRF)
- Program: shopify
- Disclosed At: 2019-04-04T13:09:45.098Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability similar to https://hackerone.com/reports/156877 , that I found in your old version of your logo-creator.
During logo-creating process the user can select logo in  wysiwyg editor, then enter email address and wait. In this moment server send to user's browser large amount of data through websockets. Among these data there are svg files (with escaped characters ",quotation mark ) . Then, this svg-files browser send to server to convert in png, and png-files send to user through link in email.

User can change svg-files that browser send to server, and can insert own xlink:href object and :

Link to local image files, to fingerprint versions of libraries installed on server;
"Billion laughs" attack, possible DoS attack to converter server;
Try to change protocol to ftp and connect to ftp-servers;
Try to exploit vulnerabilities like "Imagetragic", or XXE

## Impact

Read files from the  server
Abuse the trust relationship between the vulnerable server and others
Retrieve sensitive information from server

Try to :
Scan the internal network to which the server is connected to
Use other image-converter vulnerabilities

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
