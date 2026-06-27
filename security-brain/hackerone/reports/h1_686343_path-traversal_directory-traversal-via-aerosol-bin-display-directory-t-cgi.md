---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '686343'
original_report_id: '686343'
title: '[██████████] — Directory traversal via `/aerosol-bin/███████/display_directory_████_t.cgi`'
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2019-09-02T13:07:41.992Z'
disclosed_at: '2020-05-14T18:03:22.211Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- path-traversal
---

# [██████████] — Directory traversal via `/aerosol-bin/███████/display_directory_████_t.cgi`

## Metadata

- HackerOne Report ID: 686343
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2020-05-14T18:03:22.211Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description

On the domain `https://█████████`, there is a vulnerable endpoint that lets an attacker preview and browse the whole server including all the server's critical directories such as `etc` , `var`, `cache` etc. located in the root directory of this Linux web server.

This vulnerable endpoint is found on many pages across this web app including:

https://www.██████████/aerosol-bin/██████/█████.html_t.cgi?date=20070301

## Proof of concept

Please visit the following URLs for the POC:

1. https://www.█████████/aerosol-bin/████/display_directory_███_t.cgi?DIR=/etc

███

2. https://www.████████/aerosol-bin/████████/display_directory_████████_t.cgi?DIR=/var

█████

3. https://www.███/aerosol-bin/█████/display_directory_████_t.cgi?DIR=/var/lib

██████

## Fix

To fix this issue, the `DIR` parameter must be properly validated to show only data in the directories that is supposed to be public and must not go above public folders (public_html) in any case.

## Impact

This vulnerability can reveal all the information about the web server including any libraries installed, any sensitive directories, potentially allowing an attacker to leverage this to compromise the web server.

Thanks,
Usama

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
