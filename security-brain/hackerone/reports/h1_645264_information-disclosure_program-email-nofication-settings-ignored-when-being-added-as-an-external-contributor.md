---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '645264'
original_report_id: '645264'
title: Program Email Nofication settings ignored when being added as an external contributor
weakness: Information Disclosure
team_handle: security
created_at: '2019-07-16T15:52:36.845Z'
disclosed_at: '2019-08-07T23:01:26.824Z'
has_bounty: true
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

# Program Email Nofication settings ignored when being added as an external contributor

## Metadata

- HackerOne Report ID: 645264
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-08-07T23:01:26.824Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

When being added as an external contributor to a report, the report title are displayed in the email notification despite the program email notification settings being set to `No Content`

**Description:**

Hey team!

I noticed that programs have the ability to set their Email Notification settings, to `No Content`, which masks the report title:

{F530569}

This causes the hackers emails notifications to look like this:

███████

HOWEVER, if another hacker gets added as an external contributor to the report, the report title and activity are shown in the report:


{F530572}


### Steps To Reproduce

1. As a Program admin, navigate to `Program Settings`
2. Click `Program`
3. Click `Email Notifications`
4. Click `No Content`
5. Go to any report in your program and invite any hacker to the report.
6. Check the hackers email, they will see the report title in the invitation email


Hope that helps!

## Impact

Information Disclosure bypassing a program setting

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
