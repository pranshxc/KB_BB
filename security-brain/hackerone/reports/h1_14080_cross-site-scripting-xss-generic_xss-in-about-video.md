---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14080'
original_report_id: '14080'
title: XSS in "About Video"
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-30T06:44:50.268Z'
disclosed_at: '2014-07-06T19:13:05.881Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in "About Video"

## Metadata

- HackerOne Report ID: 14080
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-07-06T19:13:05.881Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

- http://my.mail.ru/video/top
- добавить видео
- в описании видео вставить к примеру "><img src=x onerror=alert(document.cookie)>
- открыть видео из альбома

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
