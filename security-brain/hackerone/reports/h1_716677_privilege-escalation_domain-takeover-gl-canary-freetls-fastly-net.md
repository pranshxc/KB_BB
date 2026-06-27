---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '716677'
original_report_id: '716677'
title: Domain Takeover - gl-canary.freetls.fastly.net
weakness: Privilege Escalation
team_handle: gitlab
created_at: '2019-10-17T19:13:16.156Z'
disclosed_at: '2023-05-30T06:50:33.091Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Domain Takeover - gl-canary.freetls.fastly.net

## Metadata

- HackerOne Report ID: 716677
- Weakness: Privilege Escalation
- Program: gitlab
- Disclosed At: 2023-05-30T06:50:33.091Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gitlab!

The domain `gl-canary.freetls.fastly.net` is whitelisted in gitlab.com Content Security Policy. See `Content-Security-Policy` HTTP header from gitlab.com:

```
Content-Security-Policy: connect-src 'self' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net wss://gitlab.com https://sentry.gitlab.net https://customers.gitlab.com https://snowplow.trx.gitlab.net; frame-ancestors 'self'; frame-src 'self' https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://content.googleapis.com https://content-compute.googleapis.com https://content-cloudbilling.googleapis.com https://content-cloudresourcemanager.googleapis.com https://*.codesandbox.io; img-src * data: blob:; object-src 'none'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://www.gstatic.com/recaptcha/ https://apis.google.com 'nonce-bjSllX/7AnVrXL1QQxsb+w=='; style-src 'self' 'unsafe-inline' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net; worker-src https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://gitlab.com blob:
```

This domain can be controlled from any fastly.com account:
1. Register at https://www.fastly.com/signup
2. Go to https://manage.fastly.com/services/all
3. Create a new service 
4. Use `gl-canary.global.ssl.fastly.net` as domain. (Fastly automatically creates <name>.freetls.fastly.net. See https://docs.fastly.com/en/guides/setting-up-free-tls#support-for-http2-ipv6-and-tls-12)
5. Configure hosts

## Impact

An attacker can use the domain to bypass the CSP and execute malicious client-side code (for example, the client application may have an XSS vulnerability).
The domain could potentially be used elsewhere in Gitlab application (CDN, for example).

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
