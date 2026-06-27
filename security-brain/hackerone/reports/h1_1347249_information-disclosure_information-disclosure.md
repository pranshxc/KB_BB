---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1347249'
original_report_id: '1347249'
title: Information disclosure
weakness: Information Disclosure
team_handle: brave
created_at: '2021-09-21T18:56:44.226Z'
disclosed_at: '2021-09-21T23:35:38.889Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information disclosure

## Metadata

- HackerOne Report ID: 1347249
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2021-09-21T23:35:38.889Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Vulnerability tested on:- Brave	1.29.81 Chromium: 93.0.4577.82 (Official Build) (64-bit)
Vulnerability description:- For security measures and for privacy purposes, Brave has the ability to open a normal tab of the Brave when we navigate to: `chrome://wallet`, `chrome://history` etc. due to the reason that Tor should be blocking privileged URIs like `file:///`, `chrome://` etc. When we open local storage URIs or the Data URIs, it is blocking. So, we can say that TOR in Brave protects users from opening anything privileged in the browser.
But there is some weird case for: `chrome://downloads` and `brave://inspect/#devices`. Both can be dangerous when there is a UXSS present there because it can get to know about the data. The `brave://device-log/` looks interesting too, why do we see the device log of brave in the TOR Network in the Brave? 

Steps to reproduce:
1. Open Brave with TOR
2. Navigate to `brave://inspect/#devices`

Expected behavior?
--> When we are doing device debugging, it should have opened normal Brave and shouldn't open the privileged URI in the TOR session itself. Open `chrome://bookmarks` and `chrome://history`

Actual behavior?
--> It opens the debugging session inside the protected tor session.

Suggestions?
--> We should block `chrome://downloads`,  `brave://inspect/#devices`, `brave://device-log/` etc. and when somebody tries to navigate to those URIs, a normal Brave session should be started like we do for `chrome://history` as it keeps TOR away from personal information inside the brave URIs.

## Impact

Information disclosure.

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
