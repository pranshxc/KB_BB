---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181088'
original_report_id: '181088'
title: Window.opener bug at www.coinbase.com
team_handle: coinbase
created_at: '2016-11-09T15:39:09.614Z'
disclosed_at: '2016-11-28T18:17:31.756Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# Window.opener bug at www.coinbase.com

## Metadata

- HackerOne Report ID: 181088
- Weakness: 
- Program: coinbase
- Disclosed At: 2016-11-28T18:17:31.756Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Window.Opener Bug**

**Description:**

When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

**Browsers Verified In:**

  * Mozilla Firefox

**Steps To Reproduce:**

1. Visit https://www.coinbase.com/
2. In Image F133659, If you notice the links go through `https://www.coinbase.com/external_redirect` except "Bloomberg"

3. Since Bloomberg works on `http`, If you're in the same network you can manipulate the bloomberg page and inject a script which manipulates `window.opener`

`window.opener.location.replace("https://www.notcoinbase.com");`

I understand this is very trivial to exploit and does not have very big impact

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
