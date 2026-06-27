---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1125143'
original_report_id: '1125143'
title: No DMARC record at cordacon.com
team_handle: r3
created_at: '2021-03-13T19:47:01.610Z'
disclosed_at: '2021-08-18T08:27:15.217Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: cordacon.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# No DMARC record at cordacon.com

## Metadata

- HackerOne Report ID: 1125143
- Weakness: 
- Program: r3
- Disclosed At: 2021-08-18T08:27:15.217Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I am happy to receive your invitation, and i will try my best to keep R3 secured.

As this is my first report and can be considered as low severity and some companies even considered it as N/A, but as I see in your policy its not mention as out of scope.

one of your domain has no DMARC record, which can give attacker access to your domain to send phishing emails to every one with the sender eg `admin@cordacon.com`


## Steps To Reproduce:
1. Visit https://mxtoolbox.com
2. Type the domain cordacon.com
3. click on Ok your will see no DMARC record

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Attacker access to your domain to send phishing emails to every one with the sender eg `admin@cordacon.com`
Or black mail your domain because sometimes the email will be in spam folder, any one receive such email will think that its from you and you're scammers.

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
