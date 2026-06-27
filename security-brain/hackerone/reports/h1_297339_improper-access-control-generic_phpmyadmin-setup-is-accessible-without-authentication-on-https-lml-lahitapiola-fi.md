---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '297339'
original_report_id: '297339'
title: PHPMYADMIN Setup is accessible without authentication on https://lml.lahitapiola.fi/
weakness: Improper Access Control - Generic
team_handle: localtapiola
created_at: '2017-12-12T19:17:40.673Z'
disclosed_at: '2017-12-13T13:43:53.489Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
tags:
- hackerone
- improper-access-control-generic
---

# PHPMYADMIN Setup is accessible without authentication on https://lml.lahitapiola.fi/

## Metadata

- HackerOne Report ID: 297339
- Weakness: Improper Access Control - Generic
- Program: localtapiola
- Disclosed At: 2017-12-13T13:43:53.489Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Vulnerability Detail
PhpMyAdmin setup page is accessible over the internet in which it's possible for the user setup the servers with required details.

## Vulnerable Endpoint
https://lml.lahitapiola.fi/admin/phpMyAdmin/setup/index.php

## Attached screenshots
{F246247}

{F246248}

## Impact

Its possible for an attacker to configure the servers without information of the application adminstrator.

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
