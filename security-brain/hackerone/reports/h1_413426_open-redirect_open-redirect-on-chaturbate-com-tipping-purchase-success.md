---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413426'
original_report_id: '413426'
title: Open redirect on chaturbate.com (tipping/purchase_success)
weakness: Open Redirect
team_handle: chaturbate
created_at: '2018-09-24T15:35:42.663Z'
disclosed_at: '2018-10-25T01:42:34.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect on chaturbate.com (tipping/purchase_success)

## Metadata

- HackerOne Report ID: 413426
- Weakness: Open Redirect
- Program: chaturbate
- Disclosed At: 2018-10-25T01:42:34.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I would like to report an open redirect issue on `https://chaturbate.com/`


## Description

An attacker can redirect a user to any external website using the parameter `prejoin_data`, this parameter seems to miss sanitization.


## Steps to Reproduce

Visit the following url:
https://64.38.230.2/tipping/purchase_success/?product_code=4137&prejoin_data=domain%2Fpoc.10degres.net
This will redirect you to my website `http://poc.10degres.net`

**Browsers Verified In:**
* Firefox 56.0, Ubuntu 16.04


## PoC

{F350390}

## Impact

By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. Because the server name in the modified link is identical to the original site, phishing attempts may have a more trustworthy appearance.


## Remediation

Use a whitelist approach to allow redirection to trusted domains.


## See also

https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet




Best regards,

Gwen

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
