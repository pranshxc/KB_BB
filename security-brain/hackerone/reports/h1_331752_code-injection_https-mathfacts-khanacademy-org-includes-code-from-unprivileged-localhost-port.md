---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '331752'
original_report_id: '331752'
title: https://mathfacts.khanacademy.org/ includes code from unprivileged localhost
  port
weakness: Code Injection
team_handle: khanacademy
created_at: '2018-04-01T08:37:08.083Z'
disclosed_at: '2019-05-25T13:57:49.939Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- code-injection
---

# https://mathfacts.khanacademy.org/ includes code from unprivileged localhost port

## Metadata

- HackerOne Report ID: 331752
- Weakness: Code Injection
- Program: khanacademy
- Disclosed At: 2019-05-25T13:57:49.939Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The webpage
* https://mathfacts.khanacademy.org/
contains an invalid javascript include at the bottom of the page:
    <script src="http://localhost:8021/webpack-dev-server.js"></script>

This is probably some unintended leftover from the development.

In normal situations this will only cause the browser to be unable to connect. But it can actually become a security risk. The port in question (8021) is an unprivileged port, which means on standard operating systems it's possible for every user on the system to run a service on this port.

If you imagine a Desktop computer that is usable by multiple users. One user can run a local service in his account opening this port, thus serving whatever javascript he wants and thus arbitrarily change the appearance of the served webpage for any other user on the same computer.

## Impact

An attacker with user privileges can manipulate the webpage https://mathfacts.khanacademy.org/ for all users using the same computer.

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
