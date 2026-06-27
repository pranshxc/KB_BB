---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '754025'
original_report_id: '754025'
title: SSRF in Export template to ActiveCampaign
weakness: Server-Side Request Forgery (SSRF)
team_handle: stripo
created_at: '2019-12-08T16:57:37.282Z'
disclosed_at: '2020-04-10T07:54:32.182Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in Export template to ActiveCampaign

## Metadata

- HackerOne Report ID: 754025
- Weakness: Server-Side Request Forgery (SSRF)
- Program: stripo
- Disclosed At: 2020-04-10T07:54:32.182Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found a SSRF vulneranility in export template to  email marketing platform (ActiveCampaign).

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Login to your account in 
  1. Go to `https://my.stripo.email/cabinet/#/templates/`
  1.  Click on `Create your first mail` & select one template
  1. Export
  1. Click on `ActiveCampaign`
  1. Insert your server address in `API URL `and a fake string in API Key
  1. Now Click on Export and see your `server logs`
{F654075}

## PoC Video
{F654076}

## Impact

The export template to ActiveCampaign is vulnerable to a  SSRF vulnerability. The vulnerability allows an attacker to make arbitrary HTTP/HTTPS requests.

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
