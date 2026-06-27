---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1681178'
original_report_id: '1681178'
title: Reflected XSS at https://██████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-08-26T10:08:17.164Z'
disclosed_at: '2023-09-29T17:26:53.222Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://██████/

## Metadata

- HackerOne Report ID: 1681178
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-09-29T17:26:53.222Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
There exists a reflected XSS within the logout functionality of ServiceNow. This enables an unauthenticated remote attacker to execute arbitrary JavaScript.

## References
* https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1156793

## Impact

Steal cookies to account takeover.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2022-38463

## Steps to Reproduce
1.Go to https://████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)
2.You will see alert box like this.
███████

## Suggested Mitigation/Remediation Actions

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
