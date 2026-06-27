---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12613'
original_report_id: '12613'
title: X-Content-Type-Options header missing
weakness: Violation of Secure Design Principles
team_handle: joola-io
created_at: '2014-05-20T12:23:48.642Z'
disclosed_at: '2014-07-08T10:00:33.872Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# X-Content-Type-Options header missing

## Metadata

- HackerOne Report ID: 12613
- Weakness: Violation of Secure Design Principles
- Program: joola-io
- Disclosed At: 2014-07-08T10:00:33.872Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team

The doesn't have a header settings for X-Content-Type Options which means it is vulnerable to MIME sniffing. The only defined value, "nosniff", prevents Internet Explorer and Google Chrome from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome when downloading extensions. This reduces exposure to drive-by download attacks and sites serving user uploaded content that by clever naming could be treated by MSIE as executable or dynamic HTML files.

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
