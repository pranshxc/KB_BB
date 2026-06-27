---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1064087'
original_report_id: '1064087'
title: DMARC and SPF records
team_handle: who-covid-19-mobile-app
created_at: '2020-12-22T03:35:52.928Z'
disclosed_at: '2020-12-22T07:07:44.999Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.whocoronavirus.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# DMARC and SPF records

## Metadata

- HackerOne Report ID: 1064087
- Weakness: 
- Program: who-covid-19-mobile-app
- Disclosed At: 2020-12-22T07:07:44.999Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If you are encountering this error of No DMARC Record found, this means that your domain does not have a published DMARC record. DMARC Records are published via DNS as a text(TXT) record. They will let receiving servers know what they should do with non-aligned email received from your domain.


Vulnerable url: whocoronavirus.org


HOW TO REPRODUCE(POC-ATTACHED IMAGE):-

1.GO TO- https://mxtoolbox.com

2.ENTER THE WEBSITE CLICK GO.

3.YOU WILL SEE THE FAULT(No DMARC Record found)

4.In the new page that loads change MXLookup to DMARC Lookup

## Impact

Spammers can forge the "From" address on email messages to make messages appear to come from someone in your domain. If spammers use your domain to send spam or junk email, your domain quality is negatively affected. People who get the forged emails can mark them as spam or junk, which can impact authentic messages sent from your domain

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
