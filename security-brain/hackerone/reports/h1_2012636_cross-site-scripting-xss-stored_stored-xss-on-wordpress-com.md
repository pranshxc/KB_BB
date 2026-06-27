---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2012636'
original_report_id: '2012636'
title: Stored XSS on wordpress.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2023-06-05T00:56:43.308Z'
disclosed_at: '2023-06-26T15:49:29.173Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 59
asset_identifier: wordpress.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on wordpress.com

## Metadata

- HackerOne Report ID: 2012636
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2023-06-26T15:49:29.173Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello team,
I found a Stored XSS vulnerability in WordPress.com via app.crowdsignal.com. It is similar to report #1987172.

## Platform(s) Affected:
wordpress.com

1 .Go to https://app.crowdsignal.com/dashboard and create a poll.
2. Enter the following payload as an answer: "style="position:fixed;top:0;left:0;border:999em solid green;" onmouseover="alert(document.cookie)"
3. Go to "Share Your Poll" and copy the link.
4. Navigate to https://wordpress.com/posts and add a new post.
5. Include the copied link in the post.
6. Save the post.
7. Open the page and click on "View Results."
8. The XSS vulnerability will be triggered.

████

## Impact

The attacker can use this issue to execute malicious script code in the victim user browser also redirect the victim user to malicious sites

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
