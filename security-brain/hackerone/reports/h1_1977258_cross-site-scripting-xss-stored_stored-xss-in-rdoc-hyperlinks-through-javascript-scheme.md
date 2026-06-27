---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1977258'
original_report_id: '1977258'
title: Stored XSS in RDoc hyperlinks through javascript scheme
weakness: Cross-site Scripting (XSS) - Stored
team_handle: ruby
created_at: '2023-05-08T16:17:56.349Z'
disclosed_at: '2023-07-18T08:42:21.772Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in RDoc hyperlinks through javascript scheme

## Metadata

- HackerOne Report ID: 1977258
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: ruby
- Disclosed At: 2023-07-18T08:42:21.772Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

I found that it is possible to bypass the XSS filtering made in a series of patches to solve #1187156 report.  The #1187156 wasn't sent by me, I found the 'hyperlinks' fixes from investigating the git log.

PoC
----

Create the file with the following link:
```
x[javascript:alert(1)]
```
The output html file will contain:
```html
<a href="javascript:alert(1)">x</a>
```

## Impact

A cross-site scripting (XSS) vulnerability allows attackers to execute arbitrary web scripts or HTML via a crafted payload.

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
