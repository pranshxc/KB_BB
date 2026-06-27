---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6935'
original_report_id: '6935'
title: Missing X-Content-Type-Options
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-04-11T00:10:01.272Z'
disclosed_at: '2014-05-15T10:51:54.878Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing X-Content-Type-Options

## Metadata

- HackerOne Report ID: 6935
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-05-15T10:51:54.878Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://www.irccloud.com/#?/addNetwork doesn't have a header settings for X-Content-Type Options which means it is vulnerable to MIME sniffing. The only defined value, "nosniff", prevents Internet Explorer and Google Chrome from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome when downloading extensions. This reduces exposure to drive-by download attacks and sites serving user uploaded content that by clever naming could be treated by MSIE as executable or dynamic HTML files.

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
