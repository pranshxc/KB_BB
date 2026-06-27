---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117480'
original_report_id: '117480'
title: Stored XSS via Angular Expression injection on developer.zendesk.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2016-02-19T18:25:48.676Z'
disclosed_at: '2016-06-01T21:15:09.461Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS via Angular Expression injection on developer.zendesk.com

## Metadata

- HackerOne Report ID: 117480
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-06-01T21:15:09.461Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

developer.zendesk.com is vulnerable to stored XSS via Angular template injection.

To replicate:
Browse to https://developer.zendesk.com
Sign up with an arbitrary email address and the following name: "{{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}"
Observe the popup. 

This is a stored vulnerability - every time that user views https://developer.zendesk.com/account it will hit them.

This is not self-xss - it's possible to exploit other users by using the intentional XSS on freetrial.zendesk.com to inject a cookie into other users' browsers, forcibly logging them into my account. 


Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When a web page is rendered, the framework will scan the page for template expressions, and execute any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack.

If possible, avoid using server-side code to dynamically embed user input into client-side templates. You can prevent angular from executing expressions in blocks of HTML by using the ng-non-bindable directive: https://docs.angularjs.org/api/ng/directive/ngNonBindable If this is not practical, consider filtering out { and } from user input. Upgrading to Angular 1.5 will prevent this particular sandbox escape from working, but is not a robust fix as Angular maintain that the sandbox isn't a security feature and can't be trusted - see https://sites.google.com/site/bughunteruniversity/nonvuln/angularjs-expression-sandbox-bypass

Please refer to http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html for further information on this technique.

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
