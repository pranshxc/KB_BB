---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9774'
original_report_id: '9774'
title: Stored XSS Found
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-04-25T16:26:45.261Z'
disclosed_at: '2014-06-01T06:26:54.111Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS Found

## Metadata

- HackerOne Report ID: 9774
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-06-01T06:26:54.111Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The type of XSS Vulnerability I found on your website is a stored xss. after i connect my github account   and add a new integration then i chose my repositories then on the right side of that is a textfield that has a placeholder of  Branches (optional). then i put the following code on that textfield "><img src=x onerror=alert(document.domain);>  then i click save integration button. then after that an alert box popup containing the domain of the site.

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
