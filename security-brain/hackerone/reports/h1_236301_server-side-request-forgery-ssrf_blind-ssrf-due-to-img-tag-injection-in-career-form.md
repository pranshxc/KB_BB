---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '236301'
original_report_id: '236301'
title: Blind SSRF due to img tag injection in career form
weakness: Server-Side Request Forgery (SSRF)
team_handle: mixmax
created_at: '2017-06-03T19:55:27.379Z'
disclosed_at: '2017-07-19T02:35:17.610Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF due to img tag injection in career form

## Metadata

- HackerOne Report ID: 236301
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mixmax
- Disclosed At: 2017-07-19T02:35:17.610Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
There is SSRF vulnerability due to img tag injection in career form. Attacker can inject multiple tags and perform multiple requests on remote hosts.

**POC**
1. Visit https://mixmax.com/careers.
2. Click on `Apply now`.
3. Insert img tag `<img src=https://your_choice.com>` in all the fields.
4. Click on `Send Application`.
5. Check server logs.

I got the following ip and user-agent headers.
IP: 66.249.84.213
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)

Thanks

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
