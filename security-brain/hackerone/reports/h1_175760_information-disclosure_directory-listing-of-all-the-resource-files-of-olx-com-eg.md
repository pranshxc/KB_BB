---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175760'
original_report_id: '175760'
title: Directory Listing of all the resource files of olx.com.eg
weakness: Information Disclosure
team_handle: olx
created_at: '2016-10-14T13:20:51.848Z'
disclosed_at: '2017-01-12T19:04:42.503Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Directory Listing of all the resource files of olx.com.eg

## Metadata

- HackerOne Report ID: 175760
- Weakness: Information Disclosure
- Program: olx
- Disclosed At: 2017-01-12T19:04:42.503Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By looking in the css of " olx.com.eg " i found that the logo src is linking to an external website
 https://olxegstatic-a.akamaihd.net/bd498cb-868/packed/img/2fc685b4081782d863b0c0c452ee54197b.png
this was so normal until i simply changed the url to just
https://olxegstatic-a.akamaihd.net/
I found then a full xml file that contains all the files hosted in this (cdn i believe) including important files like the ".htaccess" and the ability to easily download it and open all the content inside it
This vulnerability is dangerous because of it giving access to all the files on the cdn or this hosting platform
On the other hand , no html or php files were found which is great

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
