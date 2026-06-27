---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '317243'
original_report_id: '317243'
title: Window.opener fix bypass
team_handle: phabricator
created_at: '2018-02-17T23:18:23.078Z'
disclosed_at: '2018-02-18T04:52:08.972Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# Window.opener fix bypass

## Metadata

- HackerOne Report ID: 317243
- Weakness: 
- Program: phabricator
- Disclosed At: 2018-02-18T04:52:08.972Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description 
Due to a recent report(https://hackerone.com/reports/306414) a fix was deployed in order to resolve the tabnabbing issue. However by using a line break the fix can be bypassed.

## Steps to reproduce
1) Browse to your Phabricator instance and create a new document.
2) Now paste in the following content 
```
[[ //google.com | aaa ]] 
```
and see that there is indeed a rel="noreferer" tag added by clicking preview and then viewing the DOM tree.
3) Now replace the document with the following content:
```
[[ /
/google.com | aaa ]] 
```
and see that no tag is added.

## Impact

An attacker can abuse this functionality to perform phishing attacks against users

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
