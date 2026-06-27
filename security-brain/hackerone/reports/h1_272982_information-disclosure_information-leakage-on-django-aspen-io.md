---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272982'
original_report_id: '272982'
title: Information leakage on django.aspen.io
weakness: Information Disclosure
team_handle: aspen
created_at: '2017-09-29T13:42:44.839Z'
disclosed_at: '2017-09-29T15:15:44.853Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: django.aspen.io
asset_type: URL
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Information leakage on django.aspen.io

## Metadata

- HackerOne Report ID: 272982
- Weakness: Information Disclosure
- Program: aspen
- Disclosed At: 2017-09-29T15:15:44.853Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Team,

I got a error message that disclose the version of nginx with OS detail, since The version of nginx is vulnerable to integer overflow.
Impact:
By seeing this information attacker can throw only interger overflow attack in order to get sensitive information 
Finally Request you to remove those Information while throwing an error.

Note: I attached POC in the attachment.

Thank you.

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
