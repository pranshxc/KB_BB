---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '437142'
original_report_id: '437142'
title: Instant open redirect on Live preview WEB Ide opening
weakness: Open Redirect
team_handle: gitlab
created_at: '2018-11-08T14:39:28.541Z'
disclosed_at: '2020-11-04T11:16:59.809Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- open-redirect
---

# Instant open redirect on Live preview WEB Ide opening

## Metadata

- HackerOne Report ID: 437142
- Weakness: Open Redirect
- Program: gitlab
- Disclosed At: 2020-11-04T11:16:59.809Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gitlab team! Asset is my own gitlab installation for Ubuntu.

The issue I want to report is lack of sandbox attribute in iframe pointing to codesandbox. This results content inside iframe redirect top level window on load.

How to reproduce:

1. create index.js with following content:
```
window.open("https://evil.com","_top");
```
2.  create package.json with following content:
```
{
  "main": "index.js",
  "dependencies": {
    "vue": "latest"
  }
}
```
3. open file in Web IDE and load preview

How to fix:

1. add sandbox attribute with needed permissions (for example, you need allow-scripts for sure) on codesandbox iframe.

## Impact

Open redirect on web ide preview load.

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
