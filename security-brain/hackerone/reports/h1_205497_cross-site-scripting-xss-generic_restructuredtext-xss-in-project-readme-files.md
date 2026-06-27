---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205497'
original_report_id: '205497'
title: '[reStructuredText] XSS in project README files'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gitlab
created_at: '2017-02-11T12:42:35.162Z'
disclosed_at: '2017-02-15T05:29:36.447Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [reStructuredText] XSS in project README files

## Metadata

- HackerOne Report ID: 205497
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gitlab
- Disclosed At: 2017-02-15T05:29:36.447Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While experimenting with parser bypass techniques, I discovered that reStructuredText markup can be used to inject a stored JavaScript payload into a project `README.rst` file.

## Steps to Reproduce

1. Create a new GitLab project
2. Initialise the project by creating a `README` file
3. Set the file title to `README.rst`
4. Paste the below Payload into the file
5. Commit the file to the project and click on the link

## Proof of Concept Payload

```
`Security test link`__.

__ javascript:alert(document.domain)
```

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
