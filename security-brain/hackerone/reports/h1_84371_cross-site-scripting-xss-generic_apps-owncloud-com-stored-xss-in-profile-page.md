---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '84371'
original_report_id: '84371'
title: 'apps.owncloud.com: Stored XSS in profile page'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2015-08-24T14:11:35.049Z'
disclosed_at: '2015-10-11T07:05:31.447Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# apps.owncloud.com: Stored XSS in profile page

## Metadata

- HackerOne Report ID: 84371
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2015-10-11T07:05:31.447Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Owncloud,

I've found  A XSS vulnerability on apps.owncloud.com

When I add a comment to add any comment field,My profile page shows my latest comment

When I add a comment starts with "><img src=x onerror=confirm(2)> the page show this comment 

so XSS alert occurs in profile page.

Even if a victim is not authenticated,vulnerability occurs on page

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
