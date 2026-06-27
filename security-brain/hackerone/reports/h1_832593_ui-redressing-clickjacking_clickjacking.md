---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '832593'
original_report_id: '832593'
title: Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: kubernetes
created_at: '2020-03-27T05:32:29.745Z'
disclosed_at: '2020-07-23T17:58:16.705Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking

## Metadata

- HackerOne Report ID: 832593
- Weakness: UI Redressing (Clickjacking)
- Program: kubernetes
- Disclosed At: 2020-07-23T17:58:16.705Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

## Summary:
Clickjacking is an attack that tricks a user into clicking a webpage element which is invisible or disguised as another element
##Description:
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
##Steps to Reproduce:
1. Go to https://kubernetes.io/
2. Generate a HTML code for testing 

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="https://kubernetes.io/" height="550px" width="700px"></iframe>
</body>
</html>

Note :- Mostly clickjacking is work on login pages but site dosent have any login page but attacker can steal user credential by manipulating user

## Impact

The hacker selected the UI Redressing (Clickjacking) weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers

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
