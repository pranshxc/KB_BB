---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1023787'
original_report_id: '1023787'
title: Stored XSS in markdown file with Nextcloud Talk using Internet Explorer
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2020-11-01T10:41:13.962Z'
disclosed_at: '2021-02-19T12:08:10.754Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: nextcloud/text
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in markdown file with Nextcloud Talk using Internet Explorer

## Metadata

- HackerOne Report ID: 1023787
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2021-02-19T12:08:10.754Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While editing a markdown file through the text app, users can create link elements that have a javascript URL such as `javascript:alert(1)`.

Steps to reproduce:
* While editing a markdown file, select some text and click the "Add Link"  button.
* Using a web proxy, intercept the request and change the href value to `javascript:alert(1)`.

{F1060394}

* Refresh the document and click the malicious link created to fire the payload.

{F1060397}

Note that CSP blocks the javascript from running, but browsers such as IE are still vulnerable.

{F1060402}

## Impact

An attacker could execute arbitrary JavaScript code on the web browser of a victim who opens the file and clicks the malicious link.

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
