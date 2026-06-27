---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '603764'
original_report_id: '603764'
title: DOM Based XSS via postMessage at https://inventory.upserve.com/login/
weakness: Cross-site Scripting (XSS) - DOM
team_handle: upserve
created_at: '2019-06-08T02:00:23.696Z'
disclosed_at: '2019-06-25T13:56:46.607Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 163
asset_identifier: inventory.upserve.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM Based XSS via postMessage at https://inventory.upserve.com/login/

## Metadata

- HackerOne Report ID: 603764
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: upserve
- Disclosed At: 2019-06-25T13:56:46.607Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description
DOM based XSS is possible at https://inventory.upserve.com/login/ due to insecure origin checking when receiving a postMessage.

#POC
1. Visit https://hq.upserve.com.████████/upserve_xss.html
2. Click link
3. View alert on https://inventory.upserve.com

#Vulnerable Code
```javascript
window.addEventListener("message", function(e) {
  if (~e.origin.indexOf("https://hq.upserve.com")) {
    if (e.data && typeof e.data == "object") {
      try {
        if (e.data["exec"]) {
          eval(e.data["exec"]);
        }
      } catch (err) {
        console.log(err);
      }
    } else {
      console.log("Non-object passed");
    }
  } else {
    console.log("Incorrect origin: " + e.origin.toString());
    return;
  }
});
```
The origin check simply determines if "https://hq.upserve.com" is anywhere in the origin so an origin like "https://hq.upserve.com.mydomain.com" will pass this check just fine.

## Impact

Due to the page being a login page, login credentials could be logged and stolen when a victim goes to login.

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
