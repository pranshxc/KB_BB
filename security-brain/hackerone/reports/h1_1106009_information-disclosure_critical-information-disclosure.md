---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1106009'
original_report_id: '1106009'
title: critical information disclosure
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2021-02-17T22:01:23.421Z'
disclosed_at: '2021-03-11T21:27:08.208Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- information-disclosure
---

# critical information disclosure

## Metadata

- HackerOne Report ID: 1106009
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-03-11T21:27:08.208Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description:

hey all ,

I have found critical information through this endpoint /██████;

this endpoint contains all env vars used in a  www.██████ such as server credentials, db ,mail , twitter client_id and client_secret , facebook client_id and client_secret, etc...

## Impact

full access control on  every services on website

## System Host(s)
www.█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to

https://www.█████████/████████; 

you need to put ; to bypass 401 error

## Suggested Mitigation/Remediation Actions

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
