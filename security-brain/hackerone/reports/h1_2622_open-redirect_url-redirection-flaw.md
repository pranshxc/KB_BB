---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2622'
original_report_id: '2622'
title: URL redirection flaw
weakness: Open Redirect
team_handle: slack
created_at: '2014-03-01T22:03:05.186Z'
disclosed_at: '2014-08-30T07:20:16.157Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- open-redirect
---

# URL redirection flaw

## Metadata

- HackerOne Report ID: 2622
- Weakness: Open Redirect
- Program: slack
- Disclosed At: 2014-08-30T07:20:16.157Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An open redirect is an application that takes a parameter and redirects a user to the parameter value without any validation. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it.

Steps to reproduce:

1) Go to this URL:

https://slack.com/checkcookie?redir=http://www.likelo.com

Proper checks should be there on the redir parameter that should only allow to redirect on slack.com URL.

Please have a look.

Best regards,
Anand

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
