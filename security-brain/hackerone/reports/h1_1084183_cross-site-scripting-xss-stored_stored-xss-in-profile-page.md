---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1084183'
original_report_id: '1084183'
title: Stored XSS in profile page
weakness: Cross-site Scripting (XSS) - Stored
team_handle: acronis
created_at: '2021-01-22T08:41:02.056Z'
disclosed_at: '2021-11-14T10:59:38.325Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in profile page

## Metadata

- HackerOne Report ID: 1084183
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: acronis
- Disclosed At: 2021-11-14T10:59:38.325Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
There is a stored XSS vulnerability in the users profile page.

Steps:

1-Go to https://forum.acronis.com , create an user and login
2-Go to profile and edit it
3- enter javascript code in Signature field for exampe  use this code in Signature : <xss onmouseover="alert(1)">test</xss>
4-send this profile to other users ,or send this profile link via email to victims.

## Impact

if someone views attacker profile the script will execute

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
