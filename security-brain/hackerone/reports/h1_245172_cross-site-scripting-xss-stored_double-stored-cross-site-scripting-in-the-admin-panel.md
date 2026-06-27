---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245172'
original_report_id: '245172'
title: Double Stored Cross-Site scripting in the admin panel
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gsa_bbp
created_at: '2017-07-01T20:03:24.854Z'
disclosed_at: '2017-09-05T20:10:18.621Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: https://github.com/18f/federalist
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Double Stored Cross-Site scripting in the admin panel

## Metadata

- HackerOne Report ID: 245172
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gsa_bbp
- Disclosed At: 2017-09-05T20:10:18.621Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered a Stored XSS attack vector in the `Custom Domain` field

##POC & Reproduction steps
1. Login to the federalist and go to the some instance `http://localhost:1337/sites/<siteid>/settings`
2. Fill the `Custom Domain` field by the
```
javascript:alert(document.domain)
```
and `Demo domain`
```
javascript:alert(document.domain);
```
(it cannot be the same so we bypass the check by adding `;`)

3. Save and press `View Website` button. You will be XSSed.
{F199337}
{F199336}
4) Go to the `http://localhost:1337/sites/<siteid>/published` - and press view on the demo site to test second Stored XSS
{F199338}

##The impact
The XSS requires user interaction (e.g. clicking the button). But still, it is a bad thing. Anyone who gain access here, can conduct stored XSS attack against other admins.

##The root cause & suggested fix
The input fields not sanitized properly - it should allow only alphanumeric characters, and dots.

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
