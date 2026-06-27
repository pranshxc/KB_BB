---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '75727'
original_report_id: '75727'
title: Stored Cross site scripting In developer.zendesk.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2015-07-15T23:23:44.424Z'
disclosed_at: '2015-09-02T21:37:18.018Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored Cross site scripting In developer.zendesk.com

## Metadata

- HackerOne Report ID: 75727
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2015-09-02T21:37:18.018Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Here is the steps to produce
1. go to https://developer.zendesk.com/account and under account information put payload in 
organization filed payload : "><img src="x" onerror=alert(document.domain)>
2. and then save the setting and after that again refresh browser and go to the account information and in the organization filed start typing the payload like "> (note dont paste) here the form is autocomplete enabled so 
its request a call to https://developer.zendesk.com/autocomplete.json?name="> 
so as we are previously added "><img src="x" onerror=alert(document.domain)> to organization its saved and its search all organization saved previously so the payload executed 
screenshot attached

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
