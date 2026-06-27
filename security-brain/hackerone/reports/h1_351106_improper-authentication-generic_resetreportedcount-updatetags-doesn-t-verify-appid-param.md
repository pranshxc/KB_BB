---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351106'
original_report_id: '351106'
title: resetreportedcount & updatetags doesn't verify appid param
weakness: Improper Authentication - Generic
team_handle: valve
created_at: '2018-05-13T11:05:19.956Z'
disclosed_at: '2018-07-02T23:49:14.415Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: steamcommunity.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# resetreportedcount & updatetags doesn't verify appid param

## Metadata

- HackerOne Report ID: 351106
- Weakness: Improper Authentication - Generic
- Program: valve
- Disclosed At: 2018-07-02T23:49:14.415Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This **requires** an account that has admin permissions on any community hub & Fiddler (not 100% required, but I'll use it for the demonstration.)

**resetreportedcount**:

Step 1:
Go to any UGC in the hub you have admin access on, open Fiddler if you haven't yet, click Clear Reports and click OK on the dialogbox.

Step 2:
Drag that request over to the composer tab, modify the id param in the body to any UGC (Outside your hub!), and execute the request! You've now reset all reports on that UGC item.

**updatetags**:

Step 1:
Go to any **guide** in the hub you have admin access on, open Fiddler if you haven't yet, click Update Tags and just select a few checkboxes and click Update. 

Step 2: 
Drag that request over to the composer tab, modify the id param in the body to any guide (Outside your hub!), and execute the request! You've now updated that guide's tags.

**Guide before**
{F296857}

**Guide after**
{F296858}

## Impact

An attacker could reset all reports on UGC, and could also change a guide's tags.

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
