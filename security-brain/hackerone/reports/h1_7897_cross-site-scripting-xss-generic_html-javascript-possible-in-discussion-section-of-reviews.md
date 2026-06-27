---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7897'
original_report_id: '7897'
title: HTML/Javascript possible in "Discussion" section of reviews
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T19:26:50.988Z'
disclosed_at: '2014-04-19T11:20:56.092Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML/Javascript possible in "Discussion" section of reviews

## Metadata

- HackerOne Report ID: 7897
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-19T11:20:56.092Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It's possible to enter HTML code and/or execute javascript code in the "Discussion" section for review.

To reproduce:

- Enter a new phrase in a project.
- Login as a different user and provide a new translation for the phrase.
- Switch back to the user that created the project and check the review phrase.
- In the discussion section, enter a new message containing HTML/Javascript.
- Open the link the is shown there and observe that HTML is not filtered and that javascript can be executed.

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
