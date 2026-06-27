---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154827'
original_report_id: '154827'
title: More content spoofing through dir param in the files app
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-07-29T05:41:44.494Z'
disclosed_at: '2016-11-04T17:16:25.899Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# More content spoofing through dir param in the files app

## Metadata

- HackerOne Report ID: 154827
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-11-04T17:16:25.899Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi! It's still possible to use an invalid `dir` param to spoof messages in the directory breadcrumbs area.

For example, you can use URL-encoded periods to bypass the directory traversal prevention. By referencing a path that returns a 301, you can add a message in the dir param F108266:

https://demo.nextcloud.com/index.php/apps/files/?dir=%2E%2E/%2E%2E/%2E%2E/.well-known/caldav/Error%20-%20please%20restart%20your%20computer%20to%20continue

Also, in Chrome, the presence of a null byte (%00) in the url causes a CSP error for an ajax request upon pageload, which prevents the redirect to `dir=/` and allows you to put a message in the dir param F108267:

https://demo.nextcloud.com/index.php/apps/files/?dir=%00Error!%20Please%20restart%20your%20computer%20and%20try%20again

Please let me know if you need more info. Thanks!

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
