---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '819863'
original_report_id: '819863'
title: XSS in PDF Viewer
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2020-03-16T02:01:22.673Z'
disclosed_at: '2020-05-23T22:54:24.794Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: nextcloud/files_pdfviewer
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in PDF Viewer

## Metadata

- HackerOne Report ID: 819863
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2020-05-23T22:54:24.794Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An outdated version of PDF.js in use allows for the CVE-2018-5158 vulnerability.

When the payload PDF is shown in the supplied PDF viewer, it can execute arbitrary JavaScript.

I have tested the payload PDF, and it is working in the Safari 13.0.5 (the latest version) and Firefox 74.0 (the latest version). Although, it does not work in the latest version of Chrome.

I could not find a way to test it on the desktop client. I assume that it would use the system PDF viewer.

Modifying the payload to fetch other code was luckily blocked because of a CORS policy.

The payload is from [https://bugzilla.mozilla.org/show_bug.cgi?id=1452075](https://bugzilla.mozilla.org/show_bug.cgi?id=1452075).
I have also included the PDF in the attachments.

The payload can be seen in action by checking the JavaScript console. It says "Hello, this is code running in" followed by the path to file where the vulnerability is.

## Impact

An attacker could execute arbitrary JavaScript code on a web browser when a PDF containing an exploit is opened.

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
