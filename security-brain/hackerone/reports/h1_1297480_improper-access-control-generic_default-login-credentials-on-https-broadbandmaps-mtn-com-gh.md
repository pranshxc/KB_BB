---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1297480'
original_report_id: '1297480'
title: Default Login Credentials on https://broadbandmaps.mtn.com.gh/
weakness: Improper Access Control - Generic
team_handle: mtn_group
created_at: '2021-08-10T00:38:52.825Z'
disclosed_at: '2022-08-25T11:05:03.033Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: mtn.com.gh
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Default Login Credentials on https://broadbandmaps.mtn.com.gh/

## Metadata

- HackerOne Report ID: 1297480
- Weakness: Improper Access Control - Generic
- Program: mtn_group
- Disclosed At: 2022-08-25T11:05:03.033Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team,
I just found out that `broadbandmaps.mtn.com.gh` requires logging in when you visit it, but it turned out that you can actually login as an Admin and do anything on the specific site.
when you visit the mentioned site you will get this   
{F1405776}
it will require to be logged in to perform any action, to bypass this you have to Login with the default credentials `Username`= admin `password`= admin , and for some reasons you can't login with Firefox it only works on Google chrome and  chromium web browser.

## Supporting Material:
-Check this Video >
{F1405806}

## Impact

Access admin Panel due to Default credentials

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
