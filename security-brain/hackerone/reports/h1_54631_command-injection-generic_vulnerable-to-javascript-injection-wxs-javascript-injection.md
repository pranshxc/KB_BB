---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54631'
original_report_id: '54631'
title: Vulnerable to JavaScript injection. (WXS)  (Javascript injection)!
weakness: Command Injection - Generic
team_handle: snapchat
created_at: '2015-04-03T11:21:29.485Z'
disclosed_at: '2015-10-22T14:22:09.262Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: com.snapchat.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# Vulnerable to JavaScript injection. (WXS)  (Javascript injection)!

## Metadata

- HackerOne Report ID: 54631
- Weakness: Command Injection - Generic
- Program: snapchat
- Disclosed At: 2015-10-22T14:22:09.262Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable to JavaScript injection. (WXS)

Description:
Java script injected in activity: 
net.hockeyapp.android.UpdateActivity with injection String: document.getElementsByTagName('body')[0].setAttribute('style', 'background-color: red');

Recommended Solution:
Local HTML modifications via malware or other apps results in execution of malicious JavaScript in the presentation layer of the app. This may result in information theft.

Verify that JavaScript and Plugin support is disabled for any WebViews (usually the default).

Ensure that all UIWebView calls do not execute without proper input validation. Apply filters for dangerous JavaScript characters if possible, using a whitelist over blacklist character policy before rendering.

References:
Mobile Top 10 2014-M7(Client Side Injection) - OWASP
Adventures with Android WebViews (Javascript injection) - OWASP


Thanks,

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
