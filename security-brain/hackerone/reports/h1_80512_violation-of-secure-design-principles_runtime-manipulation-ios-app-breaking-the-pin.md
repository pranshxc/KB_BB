---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '80512'
original_report_id: '80512'
title: Runtime manipulation iOS app breaking the PIN
weakness: Violation of Secure Design Principles
team_handle: coinbase
created_at: '2015-08-04T15:45:48.156Z'
disclosed_at: '2016-11-16T19:01:00.581Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Runtime manipulation iOS app breaking the PIN

## Metadata

- HackerOne Report ID: 80512
- Weakness: Violation of Secure Design Principles
- Program: coinbase
- Disclosed At: 2016-11-16T19:01:00.581Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I was able to bypass your pin protection by doing runtime manipulation in iOS app

1.Installed the snoop it in device
2.By going snoop it tool settings choose the coinbase app
3.I already set the the pin in coinbase app
4.Open the coinbase app it is asking for PIN
5.Now browsing the snoopit controlled window from the browser 
6.Go to the Objective C-Classes in snoop it window
7.By directly invoking the userAutheticated method from the coinbase.CBPINViewController I was able to break the PIN protection
8. userAuthenticated method is not taking any arguments just invoking this method bypassed the scree

Please see the POC video
https://www.dropbox.com/s/acvr4g7lv63tti5/runtime%20manipulation%20coinbase.mov?dl=0

You can prevent run time manipulation by do not attaching a debugger to app process
you see here how to prevent

http://resources.infosecinstitute.com/ios-application-security-part-23-defending-runtime-analysis-manipulation/

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
