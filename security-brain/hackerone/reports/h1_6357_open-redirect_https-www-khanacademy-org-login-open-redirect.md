---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6357'
original_report_id: '6357'
title: https://www.khanacademy.org/login open-redirect
weakness: Open Redirect
team_handle: khanacademy
created_at: '2014-04-07T22:05:45.300Z'
disclosed_at: '2014-04-09T20:54:49.612Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# https://www.khanacademy.org/login open-redirect

## Metadata

- HackerOne Report ID: 6357
- Weakness: Open Redirect
- Program: khanacademy
- Disclosed At: 2014-04-09T20:54:49.612Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found a bypass in the redirects :
`https://www.khanacademy.org/login?continue=http://www.olivierbeg.nl` won't work.
`https://www.khanacademy.org/login?continue=http:/www.olivierbeg.nl` will work :-)

Best regards,

Olivier Beg

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
