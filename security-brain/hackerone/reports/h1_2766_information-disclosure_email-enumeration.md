---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2766'
original_report_id: '2766'
title: Email enumeration
weakness: Information Disclosure
team_handle: slack
created_at: '2014-03-03T07:05:04.109Z'
disclosed_at: '2014-04-02T07:21:09.483Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Email enumeration

## Metadata

- HackerOne Report ID: 2766
- Weakness: Information Disclosure
- Program: slack
- Disclosed At: 2014-04-02T07:21:09.483Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Navigate to the page - https://slack.com/signin
Now, entering invalid email address returns an erroneous response.
However, if you enter a valid email address like admin@slack.com, it redirects you to a different page where it asks you to choose teams that belongs to admin@slack.com.
You can then click on any option which will in turn redirect to that particular team's page on the slack domain like <teamname>.slack.com.

The above vulnerability can be used to enumerate email address of the users of the application as well as learn more about teams associated with that email address.

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
