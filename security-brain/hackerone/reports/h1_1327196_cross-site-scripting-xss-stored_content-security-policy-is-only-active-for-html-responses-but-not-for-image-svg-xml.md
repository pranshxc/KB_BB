---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1327196'
original_report_id: '1327196'
title: Content Security Policy is only active for HTML responses  but not for image/svg+xml
weakness: Cross-site Scripting (XSS) - Stored
team_handle: rails
created_at: '2021-09-01T15:42:00.800Z'
disclosed_at: '2023-07-28T00:46:29.884Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Content Security Policy is only active for HTML responses  but not for image/svg+xml

## Metadata

- HackerOne Report ID: 1327196
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: rails
- Disclosed At: 2023-07-28T00:46:29.884Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

- Setup plain Rails application with a simple route and controller
- Configure a Content Security Policy (CSP) for downloading/preview endpoints with `default-src 'none'` (via https://edgeguides.rubyonrails.org/security.html#content-security-policy)
- Send a malicious SVG* file (e.g. attached example) from the controller via `send_data` or `send_file` with  `disposition: 'inline'` (e.g. `send_file '/path/malicious.svg', type: 'image/svg+xml', disposition: 'inline'` / `send_data malicious_svg.content, , type: 'image/svg+xml', disposition: 'inline'`)
- Expect CSP to prevent Java Script code execution as recommended by SVG Working Group specifications (see: https://github.com/w3c/svgwg/issues/266#issuecomment-270482690)
-  See that malicious SVG Java Script is executed
- __Find out that Rails only applies CSP for responses with Content-Type HTML__ (see: https://github.com/rails/rails/blob/c236ff686c6fa987924b8eefeec93c2abcc07843/actionpack/lib/action_dispatch/http/content_security_policy.rb#L20)

Note: ActiveStorage prevents this by filtering via ActiveStorage.content_types_allowed_inline

## Impact

The attacker can trick victim users to execute Java Script in the scope of their active session by uploading the malicious file to the server and sending a link to that file to the victim.

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
