---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '315205'
original_report_id: '315205'
title: Debug information disclosure on oauth-redirector.services.greenhouse.io
weakness: Information Exposure Through Debug Information
team_handle: greenhouse
created_at: '2018-02-12T14:25:54.376Z'
disclosed_at: '2020-02-29T07:55:34.158Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: app.greenhouse.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# Debug information disclosure on oauth-redirector.services.greenhouse.io

## Metadata

- HackerOne Report ID: 315205
- Weakness: Information Exposure Through Debug Information
- Program: greenhouse
- Disclosed At: 2020-02-29T07:55:34.158Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The configuration of the Sintra framework application hosted at `oauth-redirector.services.greenhouse.io` exposes internal information when exceptions occur. The application is configured with the `show_exceptions` setting which causes internal application configuration, environment variables and source code snippets to be exposed when exceptions occur.

**Description:**
When an unhandled exception occurs (such as providing an invalid `oauth_redirect_uri` cookie value to `/integrations/oauth/create`) the application produces a nicely formatted error page which lists internal application data such as configuration, environment variables and source code snippets.

This issue was identified whilst assessing the security of the OAuth login function at https://app.greenhouse.io/users/sign_in

## Steps To Reproduce:
1. Send the following HTTP request to https://oauth-redirector.services.greenhouse.io/integrations/oauth/create?state=x&code=x:

```HTTP
GET /integrations/oauth/create?state=x&code=x HTTP/1.1
Host: oauth-redirector.services.greenhouse.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.<x>greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback
Connection: close

```

## Supporting Material/References:
See the attached screenshot and saved HTML of an application error.

## Impact

Information provided by this exception, or other exceptions exposed by the Sintra framework due to the `show_exceptions` configuration setting, could allow an attacker to obtain sensitive internal configuration or source code snippets.

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
