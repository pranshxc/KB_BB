---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280495'
original_report_id: '280495'
title: Stored Cross-Site scripting in the infographics using links
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-10-19T13:24:27.664Z'
disclosed_at: '2017-12-04T16:57:15.689Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored Cross-Site scripting in the infographics using links

## Metadata

- HackerOne Report ID: 280495
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-12-04T16:57:15.689Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered, that it is possible to conduct Stored XSS attack in the public infographics pages.
Upon pasting the link, we can intercept the request, and change the link source to the malicious - which will result to the Stored XSS

##POC
https://infogram.com/step-by-step-chartsgreaterlesssvg-onloadalert1greater-1ggk2694e7dj2n0
Click on the
{F230771}
You will be XSSed:
{F230772}

##Reproduction steps
1. Create some infographic
2. Use `Add media`:
{F230779}
and type some link, for example, http://google.com
3. Start web debugger, and enable interception mode.
4. Insert the link
5. Catch the request to the 
```
https://infogram.com/api/infographics/update/[_your_project_id]
```
and change 
```
http://google.com
```
to the
```
javascript:alert(document.domain)
```
{F230780}
6. Execute the request, and make infographic Public
7. Visit it and click the link to ensure that XSS works.

##Suggested fix
Check the inserted links on the server side - they must start with the pattern `http[s]://`

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
