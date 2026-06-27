---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '215044'
original_report_id: '215044'
title: '[iOS] URL can be replaceState by blob URL in iOS Brave'
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2017-03-21T08:02:27.496Z'
disclosed_at: '2017-08-10T05:08:59.263Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# [iOS] URL can be replaceState by blob URL in iOS Brave

## Metadata

- HackerOne Report ID: 215044
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2017-08-10T05:08:59.263Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

URL can be replace by blob URL using function history.replaceState()

## Products affected: 

iOS brave version 1.3.1(17.02.14.11)

## Steps To Reproduce:

- Add a html named "blob.html" which link is "http://192.168.1.111/blob.html"

- And its source is:
```
<script>
history.replaceState('','','blob:http://192.168.1.111/xxxx')
</script>
```
- then visit this page,you will find that URL has been replace by blob URL successfully!

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
