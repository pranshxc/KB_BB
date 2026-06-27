---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125130'
original_report_id: '125130'
title: HTML Escaping Error in the 404 Page on developer.uber.com/docs/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-22T20:50:41.409Z'
disclosed_at: '2016-04-06T21:09:27.231Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Escaping Error in the 404 Page on developer.uber.com/docs/

## Metadata

- HackerOne Report ID: 125130
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-04-06T21:09:27.231Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is a non-exploitable HTML escaping error in the 404 page on developer.uber.com. When loading ```https://developer.uber.com/docs/test'test```, the following HTML is rendered: 

``` html
<a href="/docs/test" test'="" require-login="">logging in</a>
```

Note that the injected ```'``` is rendered in the HTML as a closing ```"``` that closes the href= section. Sadly, I have been unable to find any way of exploiting this because when I inject an ```=``` (in order to inject ```onmouseover=alert(0)```), it is rendered as ```%3d``` which prevents me from obtaining javascript execution. Injecting a ```>``` to close the tag also does not work. 

So I'll admit that this is not a high priority vulnerability, but I still believe that it should be fixed since it allows for the user to inject limited content into a ```<a href```. 

Thanks,
David Dworken

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
