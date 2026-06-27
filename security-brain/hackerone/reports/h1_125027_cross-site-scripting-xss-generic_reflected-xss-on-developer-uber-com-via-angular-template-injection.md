---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125027'
original_report_id: '125027'
title: Reflected XSS on developer.uber.com via Angular template injection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-22T17:35:37.948Z'
disclosed_at: '2016-04-04T22:24:46.843Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on developer.uber.com via Angular template injection

## Metadata

- HackerOne Report ID: 125027
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-04-04T22:24:46.843Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

developer.uber.com is vulnerable to reflected XSS via Angular template injection.

The following url demonstrates the root issue using a trivial payload: https://developer.uber.com/docs/deep-linking?q=wrtz{{7*7}}

If you view the rendered source of the resulting page, you'll find the string 'wrtz49', showing the input has been evaluated.

This URL uses an Angular sandbox escape to obtain arbitrary JavaScript execution and execute alert(1). It's designed to work in Internet Explorer 11, but the technique could probably be used to target other browsers given sufficient effort. I've attached a screenshot of the result.
`https://developer.uber.com/docs/deep-linking?q=wrtz{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}zzzz`


Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When a web page is rendered, the framework will scan the page for template expressions, and execute any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack. For further information on this technique, please refer to http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html

If possible, avoid using server-side code to dynamically embed user input into client-side templates. If this is not practical, consider using the ng-non-bindable directive or filtering out { and } from user input. Upgrading Angular may prevent this particular sandbox escape from working, but is not a robust fix as Angular maintain that the sandbox isn't a security feature and can't be trusted.

This vulnerability could be used to hijack developer accounts and associated apps.

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
