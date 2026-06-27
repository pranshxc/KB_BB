---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1145563'
original_report_id: '1145563'
title: Tab nabbing in Hackerone inbox.
weakness: Open Redirect
team_handle: security
created_at: '2021-04-02T18:43:20.107Z'
disclosed_at: '2021-08-09T20:20:24.922Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Tab nabbing in Hackerone inbox.

## Metadata

- HackerOne Report ID: 1145563
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2021-08-09T20:20:24.922Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Tab nabbing vulnerability occurs When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change its location using the ``window.opener`` property and from this a lot of phishing attacks could happen. This scenario occurs on hackerone.com/bugs. 
**Attack Scenario:**
 The attacker will create any website with any content which include this script tag
````html
<script>
if (window.opener) window.opener.parent.location.replace('http://phishing.com');
if (window.parent != window) window.parent.location.replace('http://phishing.com');
</script>
````
**Steps To Reproduce:**
1. submit a report to any program and write in the description your phishing website.
2. Open your inbox and click on your phishing website will open in a new tab.
3. Open the console and write ``window.opener.location='http://google.com'``
4. Return to HackerOne inbox and you will find it redirected to Google.

## Impact

* Due to the redirection is done in the background and most people aren't aware of this type of attack unlike the open redirection, Most people will fall into it and will enter their credentials leading to account takeover.

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
