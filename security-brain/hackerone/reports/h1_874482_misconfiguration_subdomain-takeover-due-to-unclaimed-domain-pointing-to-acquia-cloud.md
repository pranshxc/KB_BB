---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '874482'
original_report_id: '874482'
title: Subdomain Takeover due to unclaimed domain pointing to Acquia Cloud
weakness: Misconfiguration
team_handle: insulet_corporation
created_at: '2020-05-14T21:39:08.263Z'
disclosed_at: '2021-01-14T14:00:28.738Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- misconfiguration
---

# Subdomain Takeover due to unclaimed domain pointing to Acquia Cloud

## Metadata

- HackerOne Report ID: 874482
- Weakness: Misconfiguration
- Program: insulet_corporation
- Disclosed At: 2021-01-14T14:00:28.738Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

ssue Details

The consultant identified that subdomain http:// or https://qa.myomnipod.com 

Web Site Not Found

Sorry, we could not find any content for this web address. Please check the URL.

If you are an Acquia Cloud customer and expect to see your site at this address, you'll need to add this domain name to your site via the Acquia Network management console.

Error Is displayed.

How did you come across this bug ?

Using enumeration, I was able to discover this domain and determined it

NOTE: The hostname was not claimed by me also because i need to pay certain amount to host a website.

## Impact

Sub-domain take over attacks can happen when a company creates a dns entry that points to a third party service, however forgets about the third party application leaving it vulnerable to be hijacked by another party. Hackers can claim subdomains with the help of external services. This attack is practically non-traceable.

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
