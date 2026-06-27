---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230633'
original_report_id: '230633'
title: Weblate- Banner Grabbing-Ngnix Server version
team_handle: weblate
created_at: '2017-05-22T10:57:32.016Z'
disclosed_at: '2017-06-05T06:31:44.644Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Weblate- Banner Grabbing-Ngnix Server version

## Metadata

- HackerOne Report ID: 230633
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-05T06:31:44.644Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey, I have found in the HTTP response header from docs.weblate.org, the nginx web server version  is disclosed.

Ideally application server responds back to users error message in customzied manner by not revealing any sensitive information about webserver or underlying components in applicatio.

Please see the below attached screenshots for issue details.


Url on which i found this issue-https://docs.weblate.org/en/latest/

Please also refer -http://nginx.org/en/security_advisories.html

For More Info refer-https://www.owasp.org/index.php/Testing_for_Web_Application_Fingerprint

Note :Revealing the specific software version of the server might allow the server machine to become more vulnerable to attacks against software that is known to contain security holes. Server implementors are encouraged to make this field a configurable option.

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
