---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '858255'
original_report_id: '858255'
title: Cross site scripting - XSRF Token
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2020-04-24T06:13:55.678Z'
disclosed_at: '2020-06-14T10:40:47.524Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross site scripting - XSRF Token

## Metadata

- HackerOne Report ID: 858255
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2020-06-14T10:40:47.524Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Please follow below mentioned steps for reproducing the vulnerability.
1. Open URL: https://nextcloud.com/enterprise/buy/
2. Fill up valid name and email address and put payload in other fields.
    
    Payload/s:
			<img src="x" onload=alert(document.cookie);>
			<svg/onload=alert(document.cookie);>	
3. Submit it
4. Open email address you mentioned in the email field.
5. Open up the email source.
6. You will be prompted with xsrf-token.

## Impact

As an attacker is getting the xsrf-token, he can utilize it in later attack such as, CSRF.

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
