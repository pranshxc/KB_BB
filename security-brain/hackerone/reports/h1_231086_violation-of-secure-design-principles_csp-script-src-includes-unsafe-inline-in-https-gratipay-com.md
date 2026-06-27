---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '231086'
original_report_id: '231086'
title: CSP "script-src" includes "unsafe-inline" in https://gratipay.com
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-05-23T12:57:07.282Z'
disclosed_at: '2017-07-10T09:59:44.036Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSP "script-src" includes "unsafe-inline" in https://gratipay.com

## Metadata

- HackerOne Report ID: 231086
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-07-10T09:59:44.036Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#SUMMARY:

Related Report: #225833

Gratipay is using unsafe-inline in script-src csp headers which allows the use of inline resources, such as inline <script> elements, javascript: URLs, inline event handlers, and inline <style> elements.
Proof Of Concept

#By Using cURL:

      curl -I https://gratipay.com


The results See my attached photo.

Above CSP headers containing "script-src: header which have "unsafe-src" attribute in it.

This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Regards,

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
