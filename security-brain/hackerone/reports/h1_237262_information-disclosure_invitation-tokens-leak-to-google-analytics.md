---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '237262'
original_report_id: '237262'
title: Invitation tokens leak to Google Analytics
weakness: Information Disclosure
team_handle: security
created_at: '2017-06-06T14:44:07.247Z'
disclosed_at: '2017-07-16T16:41:58.418Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Invitation tokens leak to Google Analytics

## Metadata

- HackerOne Report ID: 237262
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2017-07-16T16:41:58.418Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While testing i have noticed that , the hackerone invitation token gets exposed to google-anaytics.com

How?

Here look at the photo-
████████

We can see that the request payload is exposing the invitation token and its not filtered like this one-

███████

And this is what google does with their request payload-

███████

So that means h1 is giving away invitation tokens to third party apps and letting them store it.

If i missed something ask me before closing the report

And requesting you to check this report- #237201

That report is about exposing private programs with valid POC

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
