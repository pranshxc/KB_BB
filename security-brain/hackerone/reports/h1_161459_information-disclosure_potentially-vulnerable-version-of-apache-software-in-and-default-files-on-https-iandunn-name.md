---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161459'
original_report_id: '161459'
title: Potentially vulnerable version of Apache software in and default files on https://iandunn.name/
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2016-08-19T21:10:32.615Z'
disclosed_at: '2016-09-27T21:46:08.780Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Potentially vulnerable version of Apache software in and default files on https://iandunn.name/

## Metadata

- HackerOne Report ID: 161459
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2016-09-27T21:46:08.780Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

The underlying web server for https://iandunn.name/ is not configured to hide the version of Apache in place. As a result, when attempts are made for the following files, a verbose response is received revealing the underlying Apache version. 

It should be noted that the underlying software could be back-ported and a newer version could be in place and should be investigated further. However, since the version reported is publicly known to contain vulnerabilities, a malicious attacker may be convinced to investigate further more malicious vulnerabilities.

Potentially Vulnerable version of Apache in place:

https://iandunn.name/wordpress/wp-admin.php
https://iandunn.name/wordpress/wp-config.php

Additionally, the following default WordPress file was identified revealing the version of WordPress in place: and should be removed:

https://iandunn.name/wordpress/readme.html

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
