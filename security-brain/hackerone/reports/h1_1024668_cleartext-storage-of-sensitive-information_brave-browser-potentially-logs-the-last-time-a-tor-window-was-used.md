---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1024668'
original_report_id: '1024668'
title: Brave Browser potentially logs the last time a Tor window was used
weakness: Cleartext Storage of Sensitive Information
team_handle: brave
created_at: '2020-11-02T17:48:48.745Z'
disclosed_at: '2020-11-04T18:36:48.681Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/brave/brave-core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Brave Browser potentially logs the last time a Tor window was used

## Metadata

- HackerOne Report ID: 1024668
- Weakness: Cleartext Storage of Sensitive Information
- Program: brave
- Disclosed At: 2020-11-04T18:36:48.681Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

A vulnerability in the Brave Browser allows an attacker to view the last time a Tor session was used in incognito mode. A local, on-disk attacker could read the Brave Browser's "Local State" json file and identify the last time a Tor session was used, affecting the confidentiality of a user's Tor session.

For example, the "Local State" file of a user who has recently used a Tor session would list a key value pair with a timestamp as accurate as "13248493693576042". This allows an attacker to fingerprint, or prove beyond reasonable doubt, that a user was using Tor at that very specific moment in time.

## Products affected: 

Brave 1.18.27 and below

## Steps To Reproduce:

 Start a Tor session in Brave Browser

## Supporting Material/References:

As discussed with security@ team in email chain titled:

Re: [Security] CVE Request 981386 - Brave Browser (All) - Exposure of
 Sensitive Information to an Unauthorized Actor While Using Tor Feature

And fixed in PR 7010:
https://github.com/brave/brave-core/pull/7010

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Violate the confidentiality of a user's Tor session.

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
