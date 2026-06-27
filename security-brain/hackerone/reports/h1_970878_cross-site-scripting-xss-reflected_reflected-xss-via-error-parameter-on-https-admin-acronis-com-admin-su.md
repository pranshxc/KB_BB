---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '970878'
original_report_id: '970878'
title: Reflected XSS via "Error" parameter on https://admin.acronis.com/admin/su/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2020-08-30T18:53:27.080Z'
disclosed_at: '2021-07-19T17:59:25.019Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS via "Error" parameter on https://admin.acronis.com/admin/su/

## Metadata

- HackerOne Report ID: 970878
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2021-07-19T17:59:25.019Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Hello,

There is possible to inject arbitrary HTML constructions on the page /admin/su/. The problem is in the insufficient escaping of special characters (like <>) for the **Error** parameter. If this parameter contains a specially crafted vector, the application will return the page that will reflect this vector directly into the HTML response without proper encoding.

This XSS vector will work in most modern browsers.

## Steps To Reproduce

1. Open the next URL in the browser: https://admin.acronis.com/admin/su/?Error=%3cscript%3ealert(document.domain)%3c%2fscript%3e

{F969715}

The XSS will be executed automatically when the page will be loaded.

## Impact

A cross-site scripting attack against the application's clients can be used to obtain user authentication information (like cookies), phishing or malware spreading. In this case, an authorized user can be the primary target of this attack, so cookie and credentials stealing are possible ways to exploit this vulnerability.

## Recommendations

It's recommended to provide the processing of web application user input by replacing potentially insecure characters that could be used to format HTML pages to their equivalents that are not HTML format characters. This should be done for any data obtained from external sources and displayed in a browser (including HTTP headers, like Referer).

## Impact

A cross-site scripting attack against the application's clients can be used to obtain user authentication information (like cookies), phishing or malware spreading. In this case, an authorized user can be the primary target of this attack, so cookie and credentials stealing are possible ways to exploit this vulnerability.

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
