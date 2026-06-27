---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5199'
original_report_id: '5199'
title: Improper Validation of the Referrer header leading to Open URL Redirection
weakness: Open Redirect
team_handle: coinbase
created_at: '2014-03-29T23:54:06.996Z'
disclosed_at: '2014-04-29T21:42:33.343Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- open-redirect
---

# Improper Validation of the Referrer header leading to Open URL Redirection

## Metadata

- HackerOne Report ID: 5199
- Weakness: Open Redirect
- Program: coinbase
- Disclosed At: 2014-04-29T21:42:33.343Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Using a proxy tool such as Burp, set the Target as https://coinbase.com.
Then, send the following request:

GET /cdn-cgi/l/chk_jschl HTTP/1.1
Host: coinbase.com
Referer: http://attacker.com
Content-Length: 2

Notice the attacker's domain in the Referrer header. This value is not being validated on the server side and as a result, the user is redirected to http://www.attacker.com

Attack Scenario:
1. An attacker hosts his own website www.attacker.com.
2. He has a link on this website https://coinbase.com/cdn-cgi/l/chk_jschl.
3. The attacker tricks a legitimate coinbase user to click on this link.
4. When the user clicks on the link, he gets redirected to the attacker controlled website.
5. Now, if the coinbase user is authenticated to the coinbase website in the same browser, all the cookies from the browser are sent to the attacker controlled website.
6. The attacker now has access to the user's session cookies which he can use to impersonate the coinbase user and take complete control over the user's account.

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
