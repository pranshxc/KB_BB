---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '732987'
original_report_id: '732987'
title: Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: owox
created_at: '2019-11-09T07:09:03.393Z'
disclosed_at: '2019-12-09T15:24:52.729Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS

## Metadata

- HackerOne Report ID: 732987
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: owox
- Disclosed At: 2019-12-09T15:24:52.729Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I have found an XSS at https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28/dashboard/?trial=activated
Because the input is not properly filtered, resulting in XSS being executed
Vulnerable area: 
-----
``6177527534dc114eb07fa829e4ce4d28``
The URL will now be: https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated

PoC
---
1, go to https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated
2, Log in and ``XSS`` will execute
██████████

Tested browser
---
Firefox 
Chrome

## Impact

This vulnerability is aimed at all victims and they do not need to be involved in the ``Project``. Just paste this URL and login, XSS will automatically execute.
Therefore, it will have a ``high impact``, because before XSS is executed, the application will ask the user to login.
+ The attacker can execute JS code.
████████
████████

Documents related to ``Impact``
---
https://portswigger.net/web-security/cross-site-scripting/reflected
https://portswigger.net/web-security/cross-site-scripting/exploiting

Recommendation
----
+ Revisit the entire application and validate the user input at server side.
+ Sanitize the data collected from input fields before further processing.
+ Filter out special and meta-characters from user input.

Best regards,
@dat

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
