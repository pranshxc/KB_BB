---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123278'
original_report_id: '123278'
title: Possible XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2016-03-15T11:59:06.766Z'
disclosed_at: '2016-04-21T23:03:49.025Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Possible XSS

## Metadata

- HackerOne Report ID: 123278
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2016-04-21T23:03:49.025Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I opened this report as soon as I have read https://mathiasbynens.github.io/rel-noopener/

It doesn't necessarly affect HackerOne, nor have i given it enough time to get a working dom manipulation.
But since Markdown allows creating **target** attributes to anchor tags, it may be possible to get this executed. even if it doesn't, I think you shouldn't let users set the target=_blank attribute to their links. I reported this because I know (and have read similar reportes where) hackerone cares about even the slightest possiblites of this kinds of bugs existing

Markdown can create them using:
```
[link](url){:target="_blank"}
```

Thanks,
Paulos

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
