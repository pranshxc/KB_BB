---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38189'
original_report_id: '38189'
title: xss in /browse/contacts/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: openfolio
created_at: '2014-12-04T11:14:57.152Z'
disclosed_at: '2015-01-14T18:46:53.790Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in /browse/contacts/

## Metadata

- HackerOne Report ID: 38189
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: openfolio
- Disclosed At: 2015-01-14T18:46:53.790Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hey guys 

i just found an xss in openfolio

i just created an contact in google with  name as "><img src=x onerror=prompt(1)>  and gave an email as random 

url >> https://www.google.com/contacts/u/0/#contact/new


then i synced  openfolio with  google contacts 

then i went here >> https://openfolio.com/browse/contacts/

then i clicked on invite of  "><img src=x onerror=prompt(1)>  , i got the xss popup ~

POC >> http://postimg.org/image/6po3vo89l/

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
