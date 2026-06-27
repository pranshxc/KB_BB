---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67929'
original_report_id: '67929'
title: Redirection Page throwing error instead of redirecting to site
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-06-14T18:45:01.721Z'
disclosed_at: '2016-05-25T02:13:58.505Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Redirection Page throwing error instead of redirecting to site

## Metadata

- HackerOne Report ID: 67929
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-05-25T02:13:58.505Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello 

I was just testing and found that http://anysite.com.com/index.php?ref=&quot;&gt;&lt;svg/onload=window.onerror=alert;throw/XSS/;// does not shows the usual External link warning page, but shows some error page .

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
