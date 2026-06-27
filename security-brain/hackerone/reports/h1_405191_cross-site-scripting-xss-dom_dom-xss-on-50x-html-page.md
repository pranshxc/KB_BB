---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '405191'
original_report_id: '405191'
title: DOM XSS on 50x.html page
weakness: Cross-site Scripting (XSS) - DOM
team_handle: duckduckgo
created_at: '2018-09-04T13:00:34.756Z'
disclosed_at: '2018-10-16T18:09:59.634Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on 50x.html page

## Metadata

- HackerOne Report ID: 405191
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: duckduckgo
- Disclosed At: 2018-10-16T18:09:59.634Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

The is a DOM XSS vulnerability on https://duckduckgo.com/50x.html, it seems like the sink is DIV.innerHTML and the source is location.search.
The PoC url is: https://duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain);%3E

The code that is causing this XSS is located in:
https://duckduckgo.com/lib/l110.js
Line 26, Column 60903

Below is the part of the vulnerable code:
`b5.createElement("div"));
cg = (m.exec(b7) || ["", ""])[1].toLowerCase();
b4 = R[cg] || R._default;
ce.innerHTML =  b4[1]  + b7.replace(aB, "<$1></$2>") + b4[2];
cb = b4[0];
while (cb--) {
	ce=ce.lastChild
}
if(!bI.support.leadingWhitespace&&b2.test(b7))`

Screenshot:
{F342240}

## Impact

The attacker can execute JS code.

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
