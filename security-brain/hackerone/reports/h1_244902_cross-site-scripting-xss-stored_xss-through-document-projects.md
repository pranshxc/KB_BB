---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244902'
original_report_id: '244902'
title: XSS through document projects
weakness: Cross-site Scripting (XSS) - Stored
team_handle: khanacademy
created_at: '2017-06-30T23:10:37.540Z'
disclosed_at: '2018-03-30T22:55:10.407Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS through document projects

## Metadata

- HackerOne Report ID: 244902
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: khanacademy
- Disclosed At: 2018-03-30T22:55:10.407Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, I'm Ethan Luis McDonough ([@elmt2](https://www.khanacademy.org/profile/elmt2/) on Khan Academy), and I found a way to inject scripts into document projects.  Since KA document projects output HTML, I can edit the PUT request that updates projects (https://www.khanacademy.org/api/internal/scratchpads/ID) and inject JavaScript code inside an `<img>` tag's `onload` attribute.  Here's a demo that completely redirects a learner from KA to another site: https://www.khanacademy.org/physics/woah/4740384569491456.  

**Note**: the stored script does not run in Firefox because document projects don't seem to be working on that browser (at least on my machine).

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
