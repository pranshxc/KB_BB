---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1178239'
original_report_id: '1178239'
title: session takeover via open protocol redirection on streamlabs.com
weakness: Open Redirect
team_handle: logitech
created_at: '2021-04-28T10:17:48.432Z'
disclosed_at: '2021-09-01T15:49:43.285Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: '*.streamlabs.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# session takeover via open protocol redirection on streamlabs.com

## Metadata

- HackerOne Report ID: 1178239
- Weakness: Open Redirect
- Program: logitech
- Disclosed At: 2021-09-01T15:49:43.285Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi Logitech team, on streamlabs.com the endpoint: `streamlabs.com/global/identity?popup=1&r=protocol://merch.streamlabs.com` redirect any authenticated user to a arbitrary protocol, and it merge the redirect link with an access_token.

{F1281409}

this means that if a malicious app that handle the protocol is installed on the device the access token will be steal by this app and consequently a session takeover is possible on multiple streamlabs domain 

## Steps To Reproduce:


  1. once authenticated on streamlabs.com go to: streamlabs.com/global/identity?popup=1&r=test://merch.streamlabs.com and intercept the request in burp.
  2. grab the redirection link in the response(as a malicious app can do, especially on mobile systems), change the protocol to https and open it in a private browser window
  3. finally in the private browser window go to: https://merch.streamlabs.com/ or https://streamlabs.com/<your_store_name> or https://streamlabs.com/my-portal?origin=cs

in every case you will be logged in as the victim

{F1281408}

{F1281407}

##possible fix

implement a protocol check on the redirection in this endpoint

## Supporting Material/References:

i attached 3 images

## Impact

session takeover by  malicious apps(on mobile systems, it's more common)

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
