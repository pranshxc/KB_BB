---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173417'
original_report_id: '173417'
title: Possilbe Sub Domain takever at prestashop.algolia.com
team_handle: algolia
created_at: '2016-10-01T20:06:49.357Z'
disclosed_at: '2016-11-04T18:58:06.298Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# Possilbe Sub Domain takever at prestashop.algolia.com

## Metadata

- HackerOne Report ID: 173417
- Weakness: 
- Program: algolia
- Disclosed At: 2016-11-04T18:58:06.298Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey Sir

It looks like `prestashop.algolia.com` has a A record pointing to `178.62.8.144`

But when you visit `prestashop.algolia.com` you see a page hosted by "BC WebSolution" and I couldn't find any relation with Algolia

Now what's suspicious here is http://178.62.8.144/ also serves the content of  "BC WebSolution"

Maybe the IP is in no more control of Algolia and has been allocated someone else while the DNS record at Algolia.com still point to the old IP

If I am correct any vulnerability like XSS, File upload affecting the IP can be used in scope of `prestashop.algolia.com`

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
