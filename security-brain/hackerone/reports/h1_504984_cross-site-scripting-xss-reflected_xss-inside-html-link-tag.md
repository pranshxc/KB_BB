---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504984'
original_report_id: '504984'
title: XSS inside HTML Link Tag
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-03-05T00:33:38.155Z'
disclosed_at: '2019-04-12T09:54:22.304Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS inside HTML Link Tag

## Metadata

- HackerOne Report ID: 504984
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-04-12T09:54:22.304Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, i discovered XSS in `sharjah.dubizzle.com`. XSS is reflected inside HTML Link tag `<link>` so it need some condition to trigger the payload.

### Step to Reproduce
- Visit `https://sharjah.dubizzle.com/property-for-sale/land" accesskey="X" onclick=alert(1337) codelatte="/2018/10/10/commercial-land-for-sale-in-al-sajja-12/` (you can copy and paste).
- XSS is reflected inside HTML Link tag {F435656}
- Press `ALT + SHIFT + X` in keyboard to trigger XSS payload.
- Alert will showing up. {F435655}

### Reference
https://portswigger.net/blog/xss-in-hidden-input-fields

**PS: Sorry, maybe there are some irreverent words. It's semi-google-translate. Hopefully you understand that.**

## Impact

XSS can use to steal cookies, password or to run arbitrary code on victim's browser.

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
