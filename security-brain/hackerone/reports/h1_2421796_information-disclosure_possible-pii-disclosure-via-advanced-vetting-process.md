---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2421796'
original_report_id: '2421796'
title: Possible PII Disclosure via Advanced Vetting Process - ██████
weakness: Information Disclosure
team_handle: security
created_at: '2024-03-18T22:49:50.482Z'
disclosed_at: '2024-05-13T14:45:44.506Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Possible PII Disclosure via Advanced Vetting Process - ██████

## Metadata

- HackerOne Report ID: 2421796
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2024-05-13T14:45:44.506Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
It might be possible to extract PII from Hackerone Users' via **HackerOne Advanced Vetting** process. As I tested this functionality from a sandboxed program, I'm not fully sure. An unauthozied user can download the **Advanced Vetting** term acceptance data from the ███ link. The csv file contains `Name of Finder,Username,Advanced Finder Vetting,Address (optional),Finder's Country,Date signed`. Also it has been observed that any logged-in user can download the terms_acceptance_data.
███████

### Steps To Reproduce
1.  Login to the H1 account.
2.  Go to ████ & ████ URLs. The csv file will be contains the Advanced Vetting acceptance details. Even though you don't have access to `███████` & `████████` programs. 

██████
█████████

### HTTP Request
```js
GET /█████/terms_acceptance_data.csv HTTP/2
Host: hackerone.com
Cookie: XXXXX
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
```

## Impact

Possible PII Leakage.

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
