---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1379158'
original_report_id: '1379158'
title: Reflected Cross-Site Scripting/HTML Injection
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: informatica
created_at: '2021-10-23T08:48:55.563Z'
disclosed_at: '2021-12-17T16:54:03.525Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross-Site Scripting/HTML Injection

## Metadata

- HackerOne Report ID: 1379158
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: informatica
- Disclosed At: 2021-12-17T16:54:03.525Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The default ASP page at https://███/redirect/default.asp is vulnerable to reflected Cross-Site Scripting in the "url" parameter. To reproduce the issue just visit the following URL and an alert should pop up:
- https://██████████/redirect/?url=%3Cscript%3Ealert(document.domain)%3C/script%3E

It seems that the redirects subdomain is used to forward users to internal resources, so this vulnerability could be used to execute JavaScript in the context of an internal user and use the browser as a proxy or steal credentials for internal resources.

In a practical attack scenario, the XSS payload could change the location of the following VPN endpoints to a phishing site and capture VPN credentials:
- https://██████████
- https://██████
- https://███

## Impact

This vulnerability could be used practically in phishing attacks to proxy traffic through internal users' browsers and ultimately lead to internal credential leaks.

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
