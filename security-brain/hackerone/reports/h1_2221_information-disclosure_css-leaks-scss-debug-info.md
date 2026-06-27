---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2221'
original_report_id: '2221'
title: CSS leaks SCSS debug info
weakness: Information Disclosure
team_handle: security
created_at: '2014-02-23T13:23:11.998Z'
disclosed_at: '2014-02-28T16:46:22.053Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# CSS leaks SCSS debug info

## Metadata

- HackerOne Report ID: 2221
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2014-02-28T16:46:22.053Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Download CSS style sheet referenced from the HTML and do:

grep -oP "file.:.*?scss" application-facbdb64a504bb08ec272860320e1941.css | sort | uniq

As you can see it exposes information about the file system, source CSS files and software used.

See enclosed file for a dump of the output of the command above.

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
