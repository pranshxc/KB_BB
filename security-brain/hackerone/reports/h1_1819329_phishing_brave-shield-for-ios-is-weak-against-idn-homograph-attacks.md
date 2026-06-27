---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1819329'
original_report_id: '1819329'
title: Brave Shield for iOS is weak against IDN homograph attacks
weakness: Phishing
team_handle: brave
created_at: '2022-12-31T07:51:19.860Z'
disclosed_at: '2023-06-22T05:50:27.405Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- phishing
---

# Brave Shield for iOS is weak against IDN homograph attacks

## Metadata

- HackerOne Report ID: 1819329
- Weakness: Phishing
- Program: brave
- Disclosed At: 2023-06-22T05:50:27.405Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

In most parts of Brave for iOS, including the address bar, protection against IDN attacks are implemented.
However, Brave Shield has no countermeasures.
For example, when you visit https://www.xn--80ak6aa92e.com , Brave Shield panel in the address bar shows the domain of this site is "apple.com".
This may lead users to be deceived into believing that the site is legitimate.

## Products affected: 

 * Brave for iOS (Version 1.45.2)

## Steps To Reproduce:

 * Visit https://www.xn--80ak6aa92e.com
 * Open Brave Shield panel from the address bar
 * "apple.com" is shown in the panel

## Supporting Material/References:

  * See the screenshot I attached.

## Impact

This may lead users to be deceived into believing that the site is legitimate.

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
