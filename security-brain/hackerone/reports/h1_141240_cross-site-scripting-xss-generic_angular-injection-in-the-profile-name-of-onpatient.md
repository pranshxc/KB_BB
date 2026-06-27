---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141240'
original_report_id: '141240'
title: Angular injection in the profile name of onpatient
weakness: Cross-site Scripting (XSS) - Generic
team_handle: drchrono
created_at: '2016-05-26T17:04:32.116Z'
disclosed_at: '2016-11-25T16:07:32.861Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Angular injection in the profile name of onpatient

## Metadata

- HackerOne Report ID: 141240
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: drchrono
- Disclosed At: 2016-11-25T16:07:32.861Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
You have an angular injection vulnerability in the profile name fields on the onpatient site. If you add a value [[5*5]] in the first name or last name field, the expression will be evaluated and when the page is rendered, the first and last name will be 25. Here I'm entering the values {F96238} and here is the result {F96242}

Interestingly, because these fields are rendered together, you can also chain them together with something like first name ```[[5*``` and last name ```5]]``` which will still be evaluated.

Now that said, I couldn't actually achieve XSS here because of the field length limitations. However, you should still fix this as:

1. Google states that sandboxing should not be considered a security measure and any injection should be treated as xss [Google bug hunter university](https://sites.google.com/site/bughunteruniversity/nonvuln/angularjs-expression-sandbox-bypass)

> In fact, we think that, even if perfect, the **AngularJS expression sandbox cannot be a security boundary**. Whether the sandbox existed or not, the attacker able to execute Angular expressions, can access the exposed scope and alter the state of the application in an unexpected way, and that's already a vulnerability.
>
>Therefore, **an expression injection flaw in the AngularJS template is no different than a regular code injection (XSS).** In short, if you're able to make AngularJS evaluate your {{31338-1}} expression to 31337, it's already a potential script execution flaw, equivalent to eval("31338-1") in non-AngularJS applications.

2. Right now it is not exploitable, but in the future if you change the field limitations, you may inadvertently expose yourself and users to XSS

3. There are numerous bypasses for angular, one may exist with these short fields which i'm not aware of [Existing disclosed angular escapes from Portswigger](http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html)

I recognize that onpatient isn't a multiple user platform per account, however, this field may be rendered elsewhere and depending on your setup, if admins can see the profile name and it too is not escaped, it could lead to a vulnerability.

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
