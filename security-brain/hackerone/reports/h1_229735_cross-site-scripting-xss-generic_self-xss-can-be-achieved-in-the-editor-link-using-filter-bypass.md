---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229735'
original_report_id: '229735'
title: Self-XSS can be achieved in the editor link using filter bypass
weakness: Cross-site Scripting (XSS) - Generic
team_handle: weblate
created_at: '2017-05-18T21:48:06.989Z'
disclosed_at: '2017-06-02T10:04:08.827Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self-XSS can be achieved in the editor link using filter bypass

## Metadata

- HackerOne Report ID: 229735
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: weblate
- Disclosed At: 2017-06-02T10:04:08.827Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
I saw the fixed issue in the https://hackerone.com/reports/223692 and i think i found another filter bypass. I noticed that we actually can use special keywords like %(branch)s, %(file)s and %(line)s.
So XSS can be achieved in this way:
`%(branch)s:alert(1);//https://`
if the branch will be named `javascript`, the payload will be executed upon pressing the source code link of the file inside it.

##Steps to reproduce
1. Create some branch and name it javascript
2. Put some source files.
3. Click the link on source file. The `%(branch)s` will be replaced by branch name (`javascript`) and popup will be fired.

##Suggested fix
I recommend you to additionally sanitize string by disallowing special symbolst before first `:` occurence (if exist)

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
