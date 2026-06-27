---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '910427'
original_report_id: '910427'
title: XSS on Videos IA
weakness: Cross-site Scripting (XSS) - Stored
team_handle: duckduckgo
created_at: '2020-06-28T17:16:43.442Z'
disclosed_at: '2020-07-31T19:39:24.889Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 67
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS on Videos IA

## Metadata

- HackerOne Report ID: 910427
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: duckduckgo
- Disclosed At: 2020-07-31T19:39:24.889Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Failure found in the videos tab.

A user was created on a [website] (https://rutube.ru/video/83a4775f020b3fd68efd3dc9a73031e8/) one with the tag `"> <img src = x onerror = alert (1)> `.

When we search DuckDuckGo for the video or user tag, we find a xss flaw in [page] (https://duckduckgo.com/?q=%22%2F%3E%22%2F%3E%3Cimg+src%3Dxss+onerror%3Dalert(2)%3E&t=hk&iar=videos&iax=videos&ia=videos&iai=https%3A%2F%2Frutube.ru%2Fvideo%2F83a4775f020b3fd68efd3dc9a73031e8%2F)  detail, in the class tag with the name `c-detail__user`

{F886397}
{F886398}

## Impact

Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.

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
