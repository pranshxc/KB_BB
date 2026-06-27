---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '475098'
original_report_id: '475098'
title: A profile page of a user can be denied from loading by appending .html to the
  username
weakness: Violation of Secure Design Principles
team_handle: gitlab
created_at: '2019-01-05T17:12:03.115Z'
disclosed_at: '2021-08-30T11:02:43.660Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# A profile page of a user can be denied from loading by appending .html to the username

## Metadata

- HackerOne Report ID: 475098
- Weakness: Violation of Secure Design Principles
- Program: gitlab
- Disclosed At: 2021-08-30T11:02:43.660Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** I was able to create a user with the username "dashboard.html". Once, the account is set up, when the user clicks on his profile, the actual dashboard will show up instead of his profile page. Same can be done for all the HTML pages in GitLab.



## Steps To Reproduce:


  1. Register a new user with "some_html_page_in_gitlab.html"
  1. After logging in. click on the profile tab, it will be redirected to the dashboard page.
  1. I even tried the username "profile.html", it is getting directed to the profile tab.

## Impact

The major impact here I can think of is that a user can hide his profile from the public just by having a clowny username.

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
