---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '212770'
original_report_id: '212770'
title: Content spoofing due to the improper behavior of the 403 page
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2017-03-12T11:01:32.590Z'
disclosed_at: '2017-05-18T16:46:17.483Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content spoofing due to the improper behavior of the 403 page

## Metadata

- HackerOne Report ID: 212770
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2017-05-18T16:46:17.483Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Content spoofing, also referred to as content injection or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application.

PoC: https://demo.nextcloud.com/.htaccess&&&&&&&&&&&&&%20this%20page%20is%20moved%20to%20http://evil.com/exploit.php%20&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

thanks.

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
