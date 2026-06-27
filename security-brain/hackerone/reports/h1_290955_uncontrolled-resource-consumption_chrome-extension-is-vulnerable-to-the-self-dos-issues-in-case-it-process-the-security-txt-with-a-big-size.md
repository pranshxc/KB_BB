---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '290955'
original_report_id: '290955'
title: Chrome Extension is vulnerable to the self-DOS issues in case it process the
  security.txt with a big size
weakness: Uncontrolled Resource Consumption
team_handle: ed
created_at: '2017-11-16T18:27:13.862Z'
disclosed_at: '2017-12-18T20:21:01.933Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: https://github.com/securitytxt/chrome-extension
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Chrome Extension is vulnerable to the self-DOS issues in case it process the security.txt with a big size

## Metadata

- HackerOne Report ID: 290955
- Weakness: Uncontrolled Resource Consumption
- Program: ed
- Disclosed At: 2017-12-18T20:21:01.933Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. Before all, thanks for the invite:) Here is keyword: `frog`
I discovered the self-DOS issue, which affects Chrome extension.

##Impact
I marked the impact as low, because it will affect only the browser tab, and will not impact other browser tabs. The issue happens due to processing the large files using AJAX call in the `getSecuritytxt` function.

##Steps to reproduce
1. Create security.txt with the size of 1-2 GB on your host.
2. Navigate to this site in the Chrome Browser (at this time you may notice traffic and CPU utilization increasing due to pre-flight check of the security.txt)
3. Click on the extension. Depending on the Chrome version, amount of RAM and CPU, you can experience one of (or all together):
 * Extension hang
 * Tab hang
 * Tab crash

##Suggested fix
Since we are making AJAX calls to the untrusted hosts, end extension is working for the every site we opened in the tab, we should get rid from such kind of issues. I suggest to implement `timeout` on the AJAX calls using
```
xhr.timeout = 15000; //some value in milliseconds
xhr.ontimeout = function (e) {
//handling timeout
}; 
```
I will link the Github PR in the comment below:)

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
