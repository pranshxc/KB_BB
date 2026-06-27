---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118033'
original_report_id: '118033'
title: X-Content-Type Header Missing For aspen.io
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-02-22T20:23:53.051Z'
disclosed_at: '2017-06-15T16:42:18.413Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# X-Content-Type Header Missing For aspen.io

## Metadata

- HackerOne Report ID: 118033
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-06-15T16:42:18.413Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform.
http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
https://www.owasp.org/index.php/List_of_useful_HTTP_headers.
Thanks

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
