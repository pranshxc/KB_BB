---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1512644'
original_report_id: '1512644'
title: Cross-site scripting (DOM-based)
weakness: Cross-site Scripting (XSS) - DOM
team_handle: oneweb
created_at: '2022-03-15T17:22:30.545Z'
disclosed_at: '2022-07-18T09:50:19.136Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Cross-site scripting (DOM-based)

## Metadata

- HackerOne Report ID: 1512644
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: oneweb
- Disclosed At: 2022-07-18T09:50:19.136Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Issue detail
The application may be vulnerable to DOM-based cross-site scripting. Data is read from window.location.hash and passed to $().
   The exploitability of this issue might depend on the specific version of jQuery that is being used. 

Issue background
DOM-based vulnerabilities arise when a client-side script reads data from a controllable part of the DOM ( https://oneweb.net/assets/scripts/app.min.js ) and processes this data in an unsafe way.
DOM-based cross-site scripting arises when a script writes controllable data into the HTML document in an unsafe way. An attacker may be able to use the vulnerability to construct a URL that, if visited by another application user, will cause JavaScript code supplied by the attacker to execute within the user's browser in the context of that user's session with the application.
The attacker-supplied code can perform a wide variety of actions, such as stealing the victim's session token or login credentials, performing arbitrary actions on the victim's behalf, and logging their keystrokes.
Users can be induced to visit the attacker's crafted URL in various ways, similar to the usual attack delivery vectors for reflected cross-site scripting vulnerabilities.
Burp Suite automatically identifies this issue using static code analysis, which may lead to false positives that are not actually exploitable. The relevant code and execution paths should be reviewed to determine whether this vulnerability is indeed present, or whether mitigations are in place that would prevent exploitation.

URL : https://oneweb.net/assets/scripts/app.min.js

## Impact

The most effective way to avoid DOM-based cross-site scripting vulnerabilities is not to dynamically write data from any untrusted source into the HTML document. If the desired functionality of the application means that this behavior is unavoidable, then defenses must be implemented within the client-side code to prevent malicious data from introducing script code into the document. In many cases, the relevant data can be validated on a whitelist basis, to allow only content that is known to be safe. In other cases, it will be necessary to sanitize or encode the data. This can be a complex task, and depending on the context that the data is to be inserted may need to involve a combination of JavaScript escaping, HTML encoding, and URL encoding, in the appropriate sequence.

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
