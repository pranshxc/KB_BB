---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703759'
original_report_id: '703759'
title: SSO through odnoklassniki uses http rather than https
weakness: Cleartext Transmission of Sensitive Information
team_handle: bumble
created_at: '2019-09-29T12:46:28.768Z'
disclosed_at: '2019-12-21T12:12:34.824Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# SSO through odnoklassniki uses http rather than https

## Metadata

- HackerOne Report ID: 703759
- Weakness: Cleartext Transmission of Sensitive Information
- Program: bumble
- Disclosed At: 2019-12-21T12:12:34.824Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SUMMARY
When using single-sign on through odnoklassniki, the user is sent to an http (non-https) URL, allowing an attacker (under some conditions) to log in to the victim's Badoo account by stealing odnoklassniki credentials, as well as to execute a CSRF-attack on the log-in form.

RECOMMENDATION
Let https://badoo.com/ok/authorize.phtml?rt=060285&js_use_scheme=https redirect to https://www.odnoklassniki.ru rather than the http version.

STEPS TO REPRODUCE
1) The victim navigates to https://badoo.com/nl/signin/ and selects 'odnoklassniki'
2) The victim is forwarded to http://www.odnoklassniki.ru/oauth/authorize?response_type=code&display=popup&client_id=126351872&scope=VALUABLE_ACCESS%3BGET_EMAIL&state=<state>&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml

Impact 1:
3) The attacker intercepts the http traffic and presents the victim a fake odnoklassniki log-in page
4) The attacker intercepts the odnoklassniki credentials entered by the victim
5) The attacker uses the intercepted odnoklassniki credentials to log in to the victim's Badoo account

Impact 2:
3) The attacker intercepts the URL at http://www.odnoklassniki.ru/ to which the victim is forwarded (which notably includes the state variable, which is connected to the victim's session)
4) The attacker browses to this URL and enters its own odnoklassniki credentials
5) The attacker intercepts the URL returning to https://badoo.com/external/redirector.phtml (including its parameters) and invites the victim to visit this URL
6) The attacker is now logged in to Badoo on the victim's device

## Impact

Impact 1:
The attacker can log in to the victim's Badoo account by stealing odnoklassniki credentials, under the following conditions:

* The attacker can modify traffic between the user and badoo.com (e.g. the user is connected to a rogue access point)
* The victim is willing to enter his odnoklassniki credentials on a http version of the site

Impact 2:
The attacker can execute a CSRF attack on the log-in form (i.e. the attacker log himself in to badoo.com on the victim's browser), under the following conditions:

* The attacker can intercept traffic between the user and badoo.com (e.g. the attacker is connected to the same unprotected wifi network)
* The attacker succeeds in causing the victim to browse to a URL provided by the attacker.

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
