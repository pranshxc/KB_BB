---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '472543'
original_report_id: '472543'
title: 'Reflected Xss bypass Content-Type: text/plain'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: pyca
created_at: '2018-12-27T12:03:40.114Z'
disclosed_at: '2018-12-28T00:08:33.201Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: '*.cryptography.io'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Xss bypass Content-Type: text/plain

## Metadata

- HackerOne Report ID: 472543
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: pyca
- Disclosed At: 2018-12-28T00:08:33.201Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello Team:
--------------

1 - vulnerable subdomain : ci.cryptography.io
2 - after i tested this subdomain i found many payloads injected by me reflected but not executed
3 - so that i taked alook at the response and i found Content-Type: text/plain 
4 - so i searched about bypass Content-Type: text/plain and i found this book **cure53** page 73 tell me i can bypass it in IE browser before version 10 

POC:
------

- go to https://ci.cryptography.io/adjuncts/20996283/hudsonyfm6u%3Cscript%3Ealert(document.domain)%3C/script%3Epub5j/plugins/favorite/assets.js
- you will see this {F397354}
- so let's try to install IE version 9 to try xss popup
- this is you will see {F397732}

something else ;
what is the java files main ?! {F397734}

## Impact

this method can affect victims that uses the IE browser before version 10 .

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
