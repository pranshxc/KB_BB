---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269426'
original_report_id: '269426'
title: Tor Project - Full Path Disclosure
weakness: Information Exposure Through an Error Message
team_handle: torproject
created_at: '2017-09-19T07:37:53.055Z'
disclosed_at: '2023-11-28T09:00:24.082Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Tor Project - Full Path Disclosure

## Metadata

- HackerOne Report ID: 269426
- Weakness: Information Exposure Through an Error Message
- Program: torproject
- Disclosed At: 2023-11-28T09:00:24.082Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

While you are primarily interested in the network/browser issues, I would like to report a web bug I discovered and thought the best place to do that would be here.

# Vulnerability

Type: Full Path Disclosure [CWE-209]
Affected endpoint: https://explorer.ooni.torproject.org
Example: https://explorer.ooni.torproject.org//x

# Details
Vulnerability details as follows.

## Impact
This security vulnerability could potentially allow a malicious hacker to map an attack against internal systems. For example, if this were to be chained with another vulnerability such as path traversal; it may lead to compromise of internal systems.

## Mitigation
Typically these sort of errors occur from incorrect data types, in this case it seems like it is just a simple 404 page which is however leaking too much information to the user. 

A best practice method is to log these type of errors to a local text file, while showing the user a friendly 404 message. This is often achieved by disabling error reporting on the application side.

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
