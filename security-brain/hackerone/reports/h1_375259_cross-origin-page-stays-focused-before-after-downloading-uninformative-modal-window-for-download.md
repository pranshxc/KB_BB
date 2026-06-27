---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '375259'
original_report_id: '375259'
title: Cross-origin page stays focused before/after downloading + uninformative modal
  window for download
team_handle: brave
created_at: '2018-07-02T10:25:35.389Z'
disclosed_at: '2018-10-04T00:51:45.174Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/brave/browser-laptop
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
---

# Cross-origin page stays focused before/after downloading + uninformative modal window for download

## Metadata

- HackerOne Report ID: 375259
- Weakness: 
- Program: brave
- Disclosed At: 2018-10-04T00:51:45.174Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

1. Open `twitter.com` using `window.open`
2. Wait some time (to finish page rendering)
3. Change location of the opened page to any downloading
4. Download modal appears above the `twitter.com`

The problem is that a user doesn't see what page exactly initiates downloading and what resource(URL) will be downloaded. 
It's possible to find out the origin of the downloaded file only after clicking "Save".

> FF has a similar modal window for downloads; However, FF shows URL of the resource before downloading. Brave doesn't do that.

> Safari+Chrome allow downloads without confirmation, so this behavior is normal for them.

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

Minimal PoC:
``` html
<script>
  function f() {
    w = window.open(`https://twitter.com`);
    setTimeout(() => {
      w.location.replace('./hello.jar')
    }, 3000)
  }
</script>

<h1>
  <a href="#" onclick="f()">Twitter</a>
</h1>
```

## Supporting Material/References:

[Live PoC](https://brave-download-modal-viabodpsch.now.sh).

PoC + screencast attached.

## Impact

This bug is related to UX and low severe. 
However, it makes #374106 much more available, because it allows downloading a malicious `.jar` from a "trusted resource".

> Note that both #374106 and this report are related to downloads.

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
