---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1962951'
original_report_id: '1962951'
title: Regression on dest parameter sanitization doesn't check scheme/websafe destinations
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: reddit
created_at: '2023-04-27T01:00:35.532Z'
disclosed_at: '2023-06-03T14:15:34.096Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 85
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Regression on dest parameter sanitization doesn't check scheme/websafe destinations

## Metadata

- HackerOne Report ID: 1962951
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: reddit
- Disclosed At: 2023-06-03T14:15:34.096Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team, I get Xss via javascript:alert() url on login page parameter dest=

###Payload Url Xss : 
```javascript:alert(document.domain);```

##XSS Javascript URL
###Steps and reproduction :

- Using a browser, navigate to: https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F
- Copy and modify the "dest" parameters so that the URL redirects to dest=javascript:alert(document.domain);
- Send this in a new browser window and after login you will get a pop up (Xss Triggered).

##Proof of Concept (PoC) :
https://www.reddit.com/login/?dest=javascript:alert(document.domain);


{F2316733}


Reference :
https://brightsec.com/blog/open-redirect-vulnerabilities/
https://hackerone.com/reports/1930763

## Impact

When an attacker manages to perform a redirect in JavaScript, many dangerous vulnerabilities may occur. As Open Redirects are mostly used in phishing scams, people are not aware of the fact that Open Redirects can also be part of more complex attack chains where multiple vulnerabilities are exploited. And JavaScript-based Open Redirect is a key part of that chain. For example, redirecting the user to javascript: something() ends up being a dangerous Cross-Site Scripting injection.
and the attacker can steal the victim's cookies

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
