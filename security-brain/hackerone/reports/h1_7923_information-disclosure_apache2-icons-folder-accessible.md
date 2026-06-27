---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7923'
original_report_id: '7923'
title: Apache2 /icons/ folder accessible
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-17T20:30:57.758Z'
disclosed_at: '2014-05-18T03:34:06.382Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Apache2 /icons/ folder accessible

## Metadata

- HackerOne Report ID: 7923
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-05-18T03:34:06.382Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Apache2 icons folder is accessible from http://www.localize.io/icons/. This is not by definition dangerous, but removing the directory can help obfuscate the server version you're running, which may prevent targeted attacks against your web server.

To remove the directory you should look for `Alias "icons" [...]` somewhere in the Apache2 config files and comment out the line.

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
