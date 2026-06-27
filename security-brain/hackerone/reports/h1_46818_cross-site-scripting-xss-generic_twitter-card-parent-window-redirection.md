---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46818'
original_report_id: '46818'
title: Twitter Card - Parent Window Redirection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-02-05T22:56:25.001Z'
disclosed_at: '2015-05-04T22:54:25.679Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Twitter Card - Parent Window Redirection

## Metadata

- HackerOne Report ID: 46818
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-05-04T22:54:25.679Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I was trying to find XSS on another website and I finally did.

After that I tried share this url on Twitter to show website owner, and noticed that I can run javascript on that iframe.


Javascript that I used on Twitter Card : 

<script>top.window.location.href="https://google.com.tr"</script>


You can watch PoC

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
