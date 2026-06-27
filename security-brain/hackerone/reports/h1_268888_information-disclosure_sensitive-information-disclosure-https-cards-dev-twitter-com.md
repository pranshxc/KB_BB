---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '268888'
original_report_id: '268888'
title: Sensitive Information Disclosure https://cards-dev.twitter.com
weakness: Information Disclosure
team_handle: x
created_at: '2017-09-16T13:43:53.639Z'
disclosed_at: '2017-09-29T23:07:06.666Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Sensitive Information Disclosure https://cards-dev.twitter.com

## Metadata

- HackerOne Report ID: 268888
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2017-09-29T23:07:06.666Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Twitter Team, 

While researching through one of your domain cards-dev.twitter.com i discovered that the host is disclosing sensitive information when a user browses to a specific directory  
https://cards-dev.twitter.com:443/keys/.

The application downloads a file json.json which discloses the following information
`"customer_key":"████"` 
`"customer_secret":"█████████"`
`"jira_password":"██████"`

I am checking that can this information be used to further escalate any vulnerability. 

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
