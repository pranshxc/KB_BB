---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198907'
original_report_id: '198907'
title: HTML Injection possible due to bad filter
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vkcom
created_at: '2017-01-17T03:11:25.656Z'
disclosed_at: '2017-02-10T12:01:31.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection possible due to bad filter

## Metadata

- HackerOne Report ID: 198907
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vkcom
- Disclosed At: 2017-02-10T12:01:31.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I have found an area where it may be possible to run certain HTML/JS scripts.

TO REPRODUCE:
1. Go to documents

2. Upload anything and edit it

3. On the edit page in tags, enter code without a closing bracket ex. <img src=x

4. Click enter

5. It will be parsed in that area, but after saving it, it won't parse.

POTENTIAL:
I'm still looking into this, as this could be a possible XSS vuln if I can find vectors without closing brackets that have harmful code.

WHY IT WORKS:
The reason this works is because your filter only looks for opening AND closing brackets, when it is possible to run code without closing the brackets.

Thanks,
Kicker

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
