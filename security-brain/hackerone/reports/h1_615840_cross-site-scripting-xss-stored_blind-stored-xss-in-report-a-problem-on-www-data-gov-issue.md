---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '615840'
original_report_id: '615840'
title: Blind Stored XSS In  "Report a Problem" on www.data.gov/issue/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gsa_bbp
created_at: '2019-06-15T16:23:49.951Z'
disclosed_at: '2019-08-07T20:03:52.924Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS In  "Report a Problem" on www.data.gov/issue/

## Metadata

- HackerOne Report ID: 615840
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gsa_bbp
- Disclosed At: 2019-08-07T20:03:52.924Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Step To Produce : 
1. Open :  https://www.data.gov/issue/
2. fill "Issue Title" and "Description" With XSSHunter Payload
3. XSS Fired In  https://labs.data.gov/crm/admin/report/662445

## Impact

Can steal admin cookies

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
