---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '863551'
original_report_id: '863551'
title: Subdomain takeover of resources.hackerone.com
team_handle: security
created_at: '2020-04-30T22:05:30.338Z'
disclosed_at: '2020-05-15T18:16:49.279Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 94
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Subdomain takeover of resources.hackerone.com

## Metadata

- HackerOne Report ID: 863551
- Weakness: 
- Program: security
- Disclosed At: 2020-05-15T18:16:49.279Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I just went to https://resources.hackerone.com/ and it shows an error "Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again." also i've checked the CNAME is poiting to read.uberflip.com which means if it is not added it can be added to any account, as [Uberflip documentation](https://help.uberflip.com/hc/en-us/articles/360018786372-Custom-Domain-Set-up-Your-Hub-on-a-Subdomain) suggests that after your subdomain is pointing to their CNAME which is read.uberflip.com, your subdomain should be added to your account so it shows the URL you chose for your hub. As i couldn't signup on their website to test due to signup problems, i just wanted your confirmation whether this subdomain is added in uberflip account or not. If not then claim it otherwise any one can add or claim this to their Uberflip account

## Impact

Subdomain takeover.

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
