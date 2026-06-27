---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190016'
original_report_id: '190016'
title: '[network.informatica.com] The login form XSS via the referer value'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-12-10T00:47:35.155Z'
disclosed_at: '2017-05-22T04:08:13.461Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [network.informatica.com] The login form XSS via the referer value

## Metadata

- HackerOne Report ID: 190016
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-05-22T04:08:13.461Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The **referer** parameter value https://network.informatica.com/login!input.jspa?referer=%ref% is inserted into the Javascript code

```javascript
if (pageURL.indexOf("login!input.jspa?referer=") > -1 || pageURL.indexOf("login.jspa?referer=") > -1) {
	finalPageURL='%ref%';
}
```
and used in further redirection without validation:

```javascript
InfaAutoLogin.authenticateUser(response.id, finalPageURL, {
	callback:function(responseMap) {
		if(responseMap['status'] === 'success') {
			document.location = responseMap['location'];
		}
		else {
			sessionStorage.setItem('autoLoginType', responseMap['statusMsg']);
		}
	}
});
```

This means an attacker can put JS links there, which will cause script execution in the victim's browser:

1. Log into your Informatica Network account
2. Go to https://network.informatica.com/login!input.jspa?referer=javascript:alert(document.domain)

{F142238}

Tested with latest Firefox and Chrome.

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
