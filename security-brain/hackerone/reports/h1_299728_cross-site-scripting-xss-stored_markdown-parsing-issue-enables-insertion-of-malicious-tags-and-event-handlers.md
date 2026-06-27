---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '299728'
original_report_id: '299728'
title: Markdown parsing issue enables insertion of malicious tags and event handlers
weakness: Cross-site Scripting (XSS) - Stored
team_handle: security
created_at: '2017-12-20T22:09:47.391Z'
disclosed_at: '2018-01-29T16:37:43.067Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 181
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Markdown parsing issue enables insertion of malicious tags and event handlers

## Metadata

- HackerOne Report ID: 299728
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: security
- Disclosed At: 2018-01-29T16:37:43.067Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When markdown is being presented as HTML, there seems to be a strange interaction between _ and @ that lets an attacker insert malicious tags.

# Proof of Concept :
```
</http:<marquee>hello
```

is rendered converted to the following HTML:

```
<p><a title="/http:<marquee" href="/http:%3Cmarquee" target="_blank">/http:<marquee>hello</p>
</marquee></a></p>
```
As you can see, the output includes a </http:<marquee tag that I can add arbitrary attributes (including event handlers).

## Impact

When markdown is being presented as HTML, there seems to be a strange interaction between _ and @ that lets an attacker insert malicious tags.

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
