---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1085336'
original_report_id: '1085336'
title: CSRF when unlocking lenses leads to lenses being forcefully installed without
  user interaction
weakness: Cross-Site Request Forgery (CSRF)
team_handle: snapchat
created_at: '2021-01-23T14:19:13.358Z'
disclosed_at: '2021-07-29T22:33:23.649Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: com.snapchat.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF when unlocking lenses leads to lenses being forcefully installed without user interaction

## Metadata

- HackerOne Report ID: 1085336
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: snapchat
- Disclosed At: 2021-07-29T22:33:23.649Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The url below allows a user to unlock a particular lens. Once they have opened the URL on their phone, Snapchat opens up and prompts the user to unlock this lens.
```
https://www.snapchat.com/unlock/?type=SNAPCODE&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

By changing the value of  `type` in the URL above, from `SNAPCODE` to `SNAPCODE_NO_PROMPT`, we can bypass the prompt mentioned earlier, and instead forcefully unlock the lens and make them use it, hence why this is a CSRF:
```
https://www.snapchat.com/unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

This issue also happens to Snapchat's deeplink on Android:
```
snapchat://unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```


I do not have an iOS device but I am certain that this issue also occurs on the iOS version of Snapchat.

## Impact

A Snapchat lens developer can abuse this bug and increase the number of people who use their lens by making people opening the URL to the lens and replacing `SNAPCODE` with `SNAPCODE_NO_PROMPT`.  This can cause false popularity for that lens as it is being unlocked without the user wanting to do so. This would then lead to the user having to manually delete the lense that was automatically added.

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
