---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '301812'
original_report_id: '301812'
title: Bitmoji source code is accessible
weakness: Information Exposure Through Directory Listing
team_handle: snapchat
created_at: '2018-01-02T17:02:30.560Z'
disclosed_at: '2021-07-31T00:20:32.738Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 84
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Bitmoji source code is accessible

## Metadata

- HackerOne Report ID: 301812
- Weakness: Information Exposure Through Directory Listing
- Program: snapchat
- Disclosed At: 2021-07-31T00:20:32.738Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi team,

I'm starting my research on snapchat by scanning all sub-domains on all the domains in-scope: snapchat.com, bitmoji.com, etc.

Let's look at one of the urls, [https://rendering-service.prod.us-east.bitstrips.com/](https://rendering-service.prod.us-east.bitstrips.com/)

When I request `GET https://rendering-service.prod.us-east.bitstrips.com/`
The response is  `403 Forbidden`

After searching, I've found [/WEB-INF/](https://rendering-service.prod.us-east.bitstrips.com/WEB-INF/) & [/META-INF/](https://rendering-service.prod.us-east.bitstrips.com/META-INF/) directories, which are accessibles and allow directory listing. 

Inside `/WEB-INF/` we have all the .class files of bitmoji, we can download all the files.

Then by using a java decompiler such as `procyon-decompiler` we reverse the .class files to make those readable. 

best,
hermès.

## Impact

Source code leaked

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
