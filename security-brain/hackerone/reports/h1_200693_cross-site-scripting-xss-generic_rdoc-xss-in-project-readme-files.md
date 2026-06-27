---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200693'
original_report_id: '200693'
title: '[RDoc] XSS in project README files'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gitlab
created_at: '2017-01-24T07:48:07.729Z'
disclosed_at: '2017-02-15T05:28:38.786Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [RDoc] XSS in project README files

## Metadata

- HackerOne Report ID: 200693
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gitlab
- Disclosed At: 2017-02-15T05:28:38.786Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While experimenting with parser bypass techniques, I discovered that RDoc markup could be used to inject a stored JavaScript payload into a project `README.rdoc` file.

Please note that this issue is separate to my earlier report #200565 (XSS with AsciiDoc markup), marked as duplicate.

## Steps to Reproduce

1. Create a new GitLab project
2. Initialise the project by creating a `README` file
3. Set the file title to `README.rdoc`
4. Paste the below Payload into the file
5. Commit the file to the project and click on the "XSS" link

## Proof of Concept Payload
`XSS[JaVaScriPt:alert(1)] <-- click to test`

Thanks!

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
