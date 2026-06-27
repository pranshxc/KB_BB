---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129869'
original_report_id: '129869'
title: beta version reveals paths, environment variables and partially files contents
weakness: Information Disclosure
team_handle: apitest
created_at: '2016-04-11T16:50:25.323Z'
disclosed_at: '2016-04-12T09:45:06.740Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# beta version reveals paths, environment variables and partially files contents

## Metadata

- HackerOne Report ID: 129869
- Weakness: Information Disclosure
- Program: apitest
- Disclosed At: 2016-04-12T09:45:06.740Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys!
You should disable error reporting on beta version. It reveals lot of information and even files contents.

How to reproduce:
1) Navigate to http://beta.apitest.io/newsletter, modify csrf-token "_token" to any data.
2) input something to "email" and "name" fields.
3) submit the form. 

As result you will be redirected to exception page with list of files, source code and environment variables.
Please take a look at screenshot.

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
