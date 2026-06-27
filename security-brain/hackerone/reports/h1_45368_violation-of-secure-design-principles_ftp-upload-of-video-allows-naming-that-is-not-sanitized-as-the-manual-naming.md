---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '45368'
original_report_id: '45368'
title: ftp upload of video allows naming that is not sanitized as the manual naming
weakness: Violation of Secure Design Principles
team_handle: vimeo
created_at: '2015-01-27T10:16:48.739Z'
disclosed_at: '2015-01-29T16:36:13.045Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# ftp upload of video allows naming that is not sanitized as the manual naming

## Metadata

- HackerOne Report ID: 45368
- Weakness: Violation of Secure Design Principles
- Program: vimeo
- Disclosed At: 2015-01-29T16:36:13.045Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have uploaded via ftp (Vimeo Pro account) a filename

""><img src = x onerror=alert(2)>".mp4

And as you can see in the screenshot it is put automatically as the name of the video. But I cannot put this name (""><img src = x onerror=alert(2)>".mp4) manually

So I think it needs the same sanitization of the name as it's done after the manual editing.

Even if the XSS is not reflected now (in this case) it can be when doing other actions involving the video name (sharing, follow, link, like etc)

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
