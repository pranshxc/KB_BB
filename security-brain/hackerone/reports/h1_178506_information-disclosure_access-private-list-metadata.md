---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178506'
original_report_id: '178506'
title: Access private list metadata
weakness: Information Disclosure
team_handle: instacart
created_at: '2016-10-27T23:17:56.864Z'
disclosed_at: '2016-12-24T08:35:09.037Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Access private list metadata

## Metadata

- HackerOne Report ID: 178506
- Weakness: Information Disclosure
- Program: instacart
- Disclosed At: 2016-12-24T08:35:09.037Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Overview

When user creates a list, they can choose to not make it public. However the attacker can still access the information that user chose to hide.

# Steps to Reproduce

1. Log in to Instacart.
2. Choose a private list that you want to see, for example the one with id = 10.
3. Go to https://www.instacart.com/api/v2/recipes/10
4. Response reveals all metadata of the list including title, description and image.

# Security Implications

The attacker can use this vulnerability to obtain metadata of any list regardless of what the visible flag is set to. Also, since list id is incremental it's easy to fetch metadata for all Instacart lists, both public and private.

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
