---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4792'
original_report_id: '4792'
title: HttpOnly flag not set for cookie on concrete5.org
weakness: Violation of Secure Design Principles
team_handle: concretecms
created_at: '2014-03-25T20:30:01.169Z'
disclosed_at: '2014-04-16T11:12:07.719Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- violation-of-secure-design-principles
---

# HttpOnly flag not set for cookie on concrete5.org

## Metadata

- HackerOne Report ID: 4792
- Weakness: Violation of Secure Design Principles
- Program: concretecms
- Disclosed At: 2014-04-16T11:12:07.719Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The HttpOnly flag is not set on concrete5.org, making it easy to steal the cookie when a XSS is present on the site.

See [HttpOnly on OWASP](https://www.owasp.org/index.php/HttpOnly) for more information.

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
