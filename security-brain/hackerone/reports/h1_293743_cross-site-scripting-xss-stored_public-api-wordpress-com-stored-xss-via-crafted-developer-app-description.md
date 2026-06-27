---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '293743'
original_report_id: '293743'
title: '[public-api.wordpress.com] Stored XSS via Crafted Developer App Description'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2017-11-29T15:38:11.655Z'
disclosed_at: '2017-12-01T13:35:43.503Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [public-api.wordpress.com] Stored XSS via Crafted Developer App Description

## Metadata

- HackerOne Report ID: 293743
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2017-12-01T13:35:43.503Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

An injection in the "App Description" field within the [WordPress Developers](https://developer.wordpress.com) platform can be used to store and reflect JavaScript in the `public-api.wordpress.com` context.

## Steps to reproduce

1) As the "adversary" user, please visit the WordPress.com [My Apps](https://developer.wordpress.com/apps/) page and select "Create New Application"

2) Populate the "Name" and "Website URL" fields with generic data, and set the Redirect URL to `https://google.com` for the purposes of this demonstration

3) Next, please copy the below proof of concept payload into the "Description" field, save your App, and take note of the client ID

4) Substitute the client ID into the following URL (which can be accessed by any user to reproduce this vulnerability)

```
https://public-api.wordpress.com/oauth2/authorize?client_id=YourID&redirect_uri=https://google.com&response_type=code&blog=
```

5) Finally, mouse over the `TESTLINK` text to execute the JavaScript payload.

### Proof of concept payload

```
'"><div id="test"><head><base href="javascript://"/></head><body><a href="/. /, /' onmouseover=confirm(document.domain); abc=abc">TESTLINK
```

### Supporting evidence

{F243076}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environments:

* Chrome OS 63.0.3239.50 (Official Build) beta (64-bit)
* Firefox 55.0.3 stable (32-bit) on Ubuntu 16.04.3 LTS

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability in a crafted API authorisation request that, if issued by another WordPress.com user, will cause arbitrary JavaScript code to execute within the target's browser in the context of their WordPress session.

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
