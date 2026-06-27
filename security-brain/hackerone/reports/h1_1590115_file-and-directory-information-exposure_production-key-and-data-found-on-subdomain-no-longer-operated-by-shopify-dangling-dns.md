---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1590115'
original_report_id: '1590115'
title: Production Key and Data Found on Subdomain No Longer Operated by Shopify /
  Dangling DNS
weakness: File and Directory Information Exposure
team_handle: shopify
created_at: '2022-06-02T21:24:13.192Z'
disclosed_at: '2024-05-01T18:17:15.231Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: '*.shopifykloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- file-and-directory-information-exposure
---

# Production Key and Data Found on Subdomain No Longer Operated by Shopify / Dangling DNS

## Metadata

- HackerOne Report ID: 1590115
- Weakness: File and Directory Information Exposure
- Program: shopify
- Disclosed At: 2024-05-01T18:17:15.231Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, Shopify team.
I found the subdomain in
http://honeybee-honeybee-ingress-data-presto-us-central1-2.shopify-data-presto-global.shopifykloud.com/languages

I was allowed to view the source code of the app's configuration (I'm not really sure), he used base64 to encode the source file, I decrypted it through a third party and found a lot of source code, even including, some content that should not be on the internet, for this I recorded a demo video where I will show how I decrypted and retrieved sensitive information within the site

I didn't look at all the source code, I found one place where I could prove the harm



'''
SCAN

{"name":"main/settings.py

███


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '███'

'''

## Impact

Key compromise can cause takeover, or direct operation of the production environment

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
