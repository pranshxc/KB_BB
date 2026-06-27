---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101330'
original_report_id: '101330'
title: SSL certificate invalid date
weakness: Cryptographic Issues - Generic
team_handle: radancy
created_at: '2015-11-24T01:20:44.976Z'
disclosed_at: '2017-03-31T02:21:01.505Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# SSL certificate invalid date

## Metadata

- HackerOne Report ID: 101330
- Weakness: Cryptographic Issues - Generic
- Program: radancy
- Disclosed At: 2017-03-31T02:21:01.505Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This SSL certificate is either expired or not yet valid. Some browsers will continue connecting to the site after presenting the user with the warning, while others will prompt the user with a dialog box requesting their approval to proceed. These warnings are extremely confusing for the typical web user, and cause most users to question the authenticity of the site they are attempting to view.
This vulnerability affects Server dev.maximum.com

Attack details
The SSL certificate (serial: 00bbd5ac7347a6a588) is expired.
The certificate validity period is between Wed Dec 7 15:35:18 UTC+0300 2011 and Thu Dec 6 15:35:18 UTC+0300 2012


The impact of this vulnerability
This SSL certificate is not valid.

How to fix this vulnerability
Verify Start Date and/or End Dates of your SSL Certificate.

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
