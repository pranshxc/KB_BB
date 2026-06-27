---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57356'
original_report_id: '57356'
title: DOM based cookie bomb
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2015-04-19T15:20:33.933Z'
disclosed_at: '2017-04-11T03:24:51.732Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DOM based cookie bomb

## Metadata

- HackerOne Report ID: 57356
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2017-04-11T03:24:51.732Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report an issue that allows attackers to plant a "cookie bomb" on a victim's browser, so that the victim will be unable to access any Twitter services.

##PoC
1. Go to http://innerht.ml/pocs/twitter-dom-based-cookie-bomb/
2. Click on the "DoS" link
3. Wait for a moment
4. Now Twitter will be unaccessible

Video demonstration
https://vimeo.com/125377697 (password: c4)

##Details
Let's examine the very first script block on https://twitter.com:
```javascript
function d(a) {
...
        var b = document.referrer || "none",
            d = "ev_redir_" + encodeURIComponent(a) + "=" + b + "; path=/";
        document.cookie = d;
...
}
...
window.location.hash != "" && d(window.location.hash.substr(1).toLowerCase())
```
In short, it sets a cookie with hash as the name and referrer as the value. The problems are that there is no length limitation setting the cookie and referrer is not properly escaped (i.e. the ";" character). Thus, the attacker can craft a long enough cookie to *.twitter.com and manipulate the referrer value to add additional cookie attributes to make the attack persistent. All requests to Twitter will then result in HTTP 431, causing a DoS on the client side.

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
