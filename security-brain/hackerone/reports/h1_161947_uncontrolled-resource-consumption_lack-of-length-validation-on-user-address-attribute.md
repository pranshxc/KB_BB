---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161947'
original_report_id: '161947'
title: Lack of length validation on user address attribute
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2016-08-21T15:15:42.421Z'
disclosed_at: '2019-04-11T08:32:44.950Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Lack of length validation on user address attribute

## Metadata

- HackerOne Report ID: 161947
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2019-04-11T08:32:44.950Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

The input fields for adding mailing address for swag delivery in ```https://hackerone.com/settings/swags``` are not restricted in input lengths.
I was able to add *(and read the contents via my own address page and the team page(who awards the swag))* over **585728 characters** in each of the input fields ```Name, Street, City, State/Province, Postal code, Country, Phone number``` without any restriction or error message.

{F113760}

This may lead to server side Denial Of Service attack or over memory consumption. You need to decrease input lengths( or add one if missing)

Thanks
Rohit Dua
https://github.com/rohit-dua
https://in.linkedin.com/in/rohitdua

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
