---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '499030'
original_report_id: '499030'
title: 'DOM Based XSS in www.hackerone.com via PostMessage (bypass of #398054)'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: security
created_at: '2019-02-21T08:01:25.647Z'
disclosed_at: '2019-05-04T07:24:33.623Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 104
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM Based XSS in www.hackerone.com via PostMessage (bypass of #398054)

## Metadata

- HackerOne Report ID: 499030
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: security
- Disclosed At: 2019-05-04T07:24:33.623Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**

The security fix by Marketo to resolve the issue reported by @adac95 in #398054 can be bypassed by purchasing an .ma domain for €60.

**Description**

The issues described by @adac95 in #398054 remain insufficiently resolved because of an inadequate security check by Marketo in the following piece of JavaScript in `forms2.min.js`
```javascript
if (a.originalEvent && a.originalEvent.data && 0 === i.indexOf(a.originalEvent.origin)) {
    var b;
    try {
        b = j.parseJSON(a.originalEvent.data)
    } catch (c) {
        return
    }
    b.mktoReady ? f() : b.mktoResponse && e(b.mktoResponse)
}
```
Since the variable `i` resolves to `https://app-sj17.marketo.com/[...]`, an attacker can bypass this check by registering the Marcarian domain `app-sj17.ma` for €60. I have done so for the sake of a good POC,  but the registration process is slow. I will comment on this issue when the POC is live.

### Steps To Reproduce

0. Wait for the POC to be live (registration of my .ma domain is in progress)
1. Browse to my POC running on https://app-sj17.ma/marketo/post2.html (note that this is literally the POC written by @adac95)
2. Note the malicous redirect is still successfully executed;

## Impact

An attacker could be able to execute JavaScript in the context of the www.hackerone.com application, if the victim user makes use of a browser which does not support CSP. The attacker could also perform a limited phishing attack in Firefox or Microsoft Edge.

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
