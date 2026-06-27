---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83604'
original_report_id: '83604'
title: Html injection on khanacademy
weakness: Command Injection - Generic
team_handle: khanacademy
created_at: '2015-08-20T08:05:27.991Z'
disclosed_at: '2015-12-14T03:48:53.466Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# Html injection on khanacademy

## Metadata

- HackerOne Report ID: 83604
- Weakness: Command Injection - Generic
- Program: khanacademy
- Disclosed At: 2015-12-14T03:48:53.466Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There's an HTML Injection Vulnerability exists in khanacademy .
 Affected parameters "linkSuccess="


Steps to reproduce:
1. first open your account on khanacademy.
2.enter the link in the url box.
   http://khanacademy.org/settings/account?linkSuccess=
3.set any text after "=" (eg.  http://khanacademy.org/settings/account?linkSuccess=hello world)
4.hit enter .
5 you see......

i have attach a poc video in this report.

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
