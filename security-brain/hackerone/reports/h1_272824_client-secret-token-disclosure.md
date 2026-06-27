---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272824'
original_report_id: '272824'
title: client_secret Token disclosure
team_handle: aspen
created_at: '2017-09-28T20:16:49.764Z'
disclosed_at: '2017-09-28T21:07:49.028Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: https://github.com/AspenWeb
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# client_secret Token disclosure

## Metadata

- HackerOne Report ID: 272824
- Weakness: 
- Program: aspen
- Disclosed At: 2017-09-28T21:07:49.028Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings, 

I think I've discovered a ```client_secret``` token disclosure. 

**_Proof of concept:_**

**1.** Go to https://github.com/AspenWeb/experimental-javascript-version/blob/master/www/blog/index.html


**2.** At the line 6, a client_secret token it's disclosed. 

```
request('https://api.github.com/repos/zetaweb/aspen/issues?client_id=f58e3c865648d1eae132&client_secret=b1e49a627a30e3d41568ecaf976436f4bfbbefba', function (error, response, body) {
```

Thanks for your attention and let me know if you need anything. 
Regards, Yumi

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
