---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '640532'
original_report_id: '640532'
title: Active Mixed Content over HTTPS
team_handle: curl
created_at: '2019-07-11T16:36:34.770Z'
disclosed_at: '2019-11-01T09:05:22.768Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Active Mixed Content over HTTPS

## Metadata

- HackerOne Report ID: 640532
- Weakness: 
- Program: curl
- Disclosed At: 2019-11-01T09:05:22.768Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
[Resources Loaded from Insecure Origin (HTTP)]

## Steps To Reproduce:
[Vulnerability Details
detected that an active content loaded over HTTP within an HTTPS page]

Remedy
There are two technologies to defense against the mixed content issues: 
HTTP Strict Transport Security (HSTS) is a mechanism that enforces secure resource retrieval, even in the face of user mistakes (attempting to access your web site on port 80) and implementation errors (your developers place an insecure link into a secure page) 
Content Security Policy (CSP) can be used to block insecure resource retrieval from third-party web sites 
Last but not least, you can use "protocol relative URLs" to have the user's browser automatically choose HTTP or HTTPS as appropriate, depending on which protocol the user is connected with. For example: 
A protocol relative URL to load an style would look like <link rel="stylesheet" href="//example.com/style.css"/>.
Same for scripts <script type="text/javascript" src="//example.com/code.js"></script>
The browser will automatically add either "http:" or "https:" to the start of the URL, whichever is appropriate.

External References

https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content

Remedy References
https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
https://en.wikipedia.org/wiki/Content_Security_Policy

## Impact

Impact
Active Content is a resource which can run in the context of your page and moreover can alter the entire page. If the HTTPS page includes active content like scripts or stylesheets retrieved through regular, cleartext HTTP, then the connection is only partially encrypted. The unencrypted content is accessible to sniffers.
A man-in-the-middle attacker can intercept the request for the HTTP content and also rewrite the response to include malicious codes. Malicious active content can steal the user's credentials, acquire sensitive data about the user, or attempt to install malware on the user's system (by leveraging vulnerabilities in the browser or its plugins, for example), and therefore the connection is not safeguarded anymore.

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
