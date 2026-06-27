---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21110'
original_report_id: '21110'
title: Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: mavenlink
created_at: '2014-07-22T22:05:46.019Z'
disclosed_at: '2014-08-21T17:13:49.708Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking

## Metadata

- HackerOne Report ID: 21110
- Weakness: UI Redressing (Clickjacking)
- Program: mavenlink
- Disclosed At: 2014-08-21T17:13:49.708Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

You have no implementation of Clickjacking attacks on your mobile version. I have set up a user agent switcher and tried to support my claim with regards to the mobile website.

For proof of concept: <iframe src="https://m.mavenlink.com/#/workspaces/new"></iframe>

For mitigation, you may want to add the HTTP header XFRAMEOPTIONS and set it to DENY.

Attached below is a screenshot. Thanks!

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
