---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18691'
original_report_id: '18691'
title: XSS in editor by any user
weakness: Cross-site Scripting (XSS) - Generic
team_handle: phabricator
created_at: '2014-07-01T16:57:02.513Z'
disclosed_at: '2014-08-13T12:59:52.123Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in editor by any user

## Metadata

- HackerOne Report ID: 18691
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: phabricator
- Disclosed At: 2014-08-13T12:59:52.123Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Steps 

+ Open any editor in phabricator where memes can be used (literally anywhere :P)
+ Enter the following and save it & **BOOM**

```
{meme, src= http://dummy//onerror=eval(prompt(1))// }
```

# Why ?

+ Nested parsing is causing the src value to be treated as a link which is automatically made link by fabricator. So, a whole mess-up of syntax happening there.
+ ```\\``` are being used as space separators since those replaced.

# Fix ?

+ May be to avoid nested parsing, it messes up things. But the choice is yours since you have more knowledge of the application needs

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
