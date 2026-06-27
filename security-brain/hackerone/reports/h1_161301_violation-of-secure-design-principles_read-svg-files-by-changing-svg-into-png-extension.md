---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161301'
original_report_id: '161301'
title: READ .svg files by changing .svg into .png extension
weakness: Violation of Secure Design Principles
team_handle: instacart
created_at: '2016-08-19T12:21:17.289Z'
disclosed_at: '2017-03-29T14:38:33.681Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# READ .svg files by changing .svg into .png extension

## Metadata

- HackerOne Report ID: 161301
- Weakness: Violation of Secure Design Principles
- Program: instacart
- Disclosed At: 2017-03-29T14:38:33.681Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good Day,
Instacart

In list and recipe we could see that we can upload a picture . It won't accept `.svg` files but by changing it to `.png`.
###Steps to Reproduce
1. Create a list and recipe under accounts
2. Upload a picture. We will upload an `svg` but with a `png` extension. I've attached an `svg` file please open it and save it as `file.png`
3. Now upload the photo and you will then now see that the svg we have made is reflected in the background photo area.

Regards,
TOM

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
