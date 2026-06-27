---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150083'
original_report_id: '150083'
title: Cross Site Scripting(XSS) on IRCCloud Badges Page (using Parameter Pollution)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: irccloud
created_at: '2016-07-08T19:55:20.685Z'
disclosed_at: '2016-07-08T23:50:49.161Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross Site Scripting(XSS) on IRCCloud Badges Page (using Parameter Pollution)

## Metadata

- HackerOne Report ID: 150083
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: irccloud
- Disclosed At: 2016-07-08T23:50:49.161Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I. Vulnerability
---------------------
IRCCloud is affected by Cross Site Scripting vulnerability in its badges page. (www.irccloud.com/badges)

II. Description
---------------------
IRCCloud is open to parameter pollution attacks ie. a parameter passed more than once with different values results in varying different results.
This bug is used to leverage an XSS in the badges page.

####POC link:
```
www.irccloud.com/badges?hostname=hostname" type="text/javascript"> /*&hostname=*/alert('XSS\n-Rohit Dua'); //
```
If  you visit the link a javascript pops up showing the message 'XSS - Rohit Dua'. (screenshot_irccloud.png)

Even after parameter pollution, the attack is ineffective due to strong XSS filters(possibly firewall)
The _filter evasion_ is possible due a certain combination of javascript comments in the url that combine and comment out the unneeded part.

#####[Attached]
POC source code screenshot
POC alert box screenshot

Please verify and fix the same.

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
