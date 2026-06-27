---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '846389'
original_report_id: '846389'
title: Open redirect at mc-beta-cloud-acronis.com
weakness: Open Redirect
team_handle: acronis
created_at: '2020-04-10T11:43:47.907Z'
disclosed_at: '2022-11-15T09:49:28.190Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- open-redirect
---

# Open redirect at mc-beta-cloud-acronis.com

## Metadata

- HackerOne Report ID: 846389
- Weakness: Open Redirect
- Program: acronis
- Disclosed At: 2022-11-15T09:49:28.190Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Open Redirect Vulnerability

Steps To Reproduce:
Type in this URL:

https://mc-beta-cloud.acronis.com/api/2/idp/authorize?client_id=f2e82dbb-78af-4b5b-bc7f-651d4f42a722&redirect_uri=%2Fbc%2Fapi%2Fgateway%2Fcb&response_type=code&scope=offline_access+openid+profile+email&state=http://evil.com&nonce=yhokbempqmmqllfbwpsfzfmf

You got redirect to evil.com

Parameter: state

## Impact

n attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

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
