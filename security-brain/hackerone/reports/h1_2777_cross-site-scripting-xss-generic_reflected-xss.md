---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2777'
original_report_id: '2777'
title: Reflected Xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-03-03T09:18:31.827Z'
disclosed_at: '2014-05-19T08:28:09.846Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Xss

## Metadata

- HackerOne Report ID: 2777
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2014-05-19T08:28:09.846Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. go to https://auth.slack.com/generate/
2. input username and password, and submit the request. 
3. In the next step application asks for the password you just created like the application says "We're almost done. Just need to test that you remember your password. Enter it again for me". Enter the password again(you created in previous step), submit and intercept the request using burp intruder.
4. Modify the 'u' param to a xss payload like u=<img src=x onerror=alert(1)>
5. Submit the request and check the response, the application does not properly escape the special char and hence xss got executed.

For better reproduction use Firefox

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
