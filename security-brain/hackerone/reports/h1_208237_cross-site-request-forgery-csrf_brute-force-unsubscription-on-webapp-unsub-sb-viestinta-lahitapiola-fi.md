---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208237'
original_report_id: '208237'
title: Brute force unsubscription on /webApp/unsub_sb (viestinta.lahitapiola.fi)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localtapiola
created_at: '2017-02-22T18:03:22.158Z'
disclosed_at: '2017-03-19T02:54:27.028Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Brute force unsubscription on /webApp/unsub_sb (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 208237
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localtapiola
- Disclosed At: 2017-03-19T02:54:27.028Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
CSRF is an attack that tricks the victim into submitting a malicious request. It inherits the identity and privileges of the victim to perform an undesired function on the victim's behalf

**Description:** Any user subscribed to Active Campaign, or admin too, attacker will able to unsubscribe using CSRF attack.

**Domain:** http://viestinta.lahitapiola.fi

## Browsers / Apps Verified In:

  * [Firefox latest version]

## Steps To Reproduce:

1. go to this link : `http://viestinta.lahitapiola.fi/webApp/unsub_sb?id=X2Fi4JiOfQdh0HkKT1xfrvO0vN5UTXiI6kcSQlQgAgA%3D`
  2. Click on `Bekrafta annullering` and intercept the traffic 
{F162916}
  3: intercept the traffic {i am using burpsuite here}, and create CSRF poc
{F162918}
4: send that HTML to victim and done, user unsubscribed from the service.

## Additional material
* Screenshots

Let me know if any further information is required.

Thanks
Regards
Neeraj

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
