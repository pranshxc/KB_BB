---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '617896'
original_report_id: '617896'
title: Bypass Email Verification using Salesforce -- Reproducible in gitlab.com
weakness: Violation of Secure Design Principles
team_handle: gitlab
created_at: '2019-06-18T07:51:06.730Z'
disclosed_at: '2019-12-13T21:00:19.953Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Bypass Email Verification using Salesforce -- Reproducible in gitlab.com

## Metadata

- HackerOne Report ID: 617896
- Weakness: Violation of Secure Design Principles
- Program: gitlab
- Disclosed At: 2019-12-13T21:00:19.953Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
The salesforce login integration allows attacker to bypass email verification -- user is able to signup with any email domain they want, effectively bypass all email domain whitelist/blacklist restriction or any other 3rd party using gitlab instance's email address.

It is possible because salesforce allow admin to create user with arbitrary email, and I believe this is what gitlab engineer forgot to consider while implementing salesforce integration.

Please follow along to see how I was able to create an account `███████` in gitlab.com

### Steps to reproduce
- Visit https://bugcrowd-ngalog-3.oktapreview.com/
- Enter creds `██████████`:`██████████`
- Click salesforce to login salesforce
- Open new tab and visit https://gitlab.com/users/sign_in
- Click login with salesforce
- you will be logged in as `████` by visiting `https://gitlab.com/profile/emails`



### Impact
Bypass email domain restriction and able to signup with arbitrary email domain

### What is the current *bug* behavior?
Able to signup with any email domain

### What is the expected *correct* behavior?
should need email verification


### Relevant logs and/or screenshots
{F511255}

## Impact

described above

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
