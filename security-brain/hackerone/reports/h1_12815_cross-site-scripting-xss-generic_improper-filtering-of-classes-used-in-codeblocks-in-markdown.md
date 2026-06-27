---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12815'
original_report_id: '12815'
title: Improper filtering of classes used in codeblocks in Markdown
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2014-05-22T13:55:53.964Z'
disclosed_at: '2014-07-08T10:00:25.793Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Improper filtering of classes used in codeblocks in Markdown

## Metadata

- HackerOne Report ID: 12815
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2014-07-08T10:00:25.793Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Redcarpet just uses the name of the language as the classname of the element. So if the classnames are of significance to the site, one can break the site using this. For instance, this report disables the topbar, and can trigger the user into opening a popup. Proof of concept:

```js-topbar
i eat the topbar
```
```js-share-link
i open a popup
```

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
