---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1092678'
original_report_id: '1092678'
title: Self stored Xss + Login Csrf
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2021-02-02T06:49:38.364Z'
disclosed_at: '2021-06-30T20:45:12.512Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Self stored Xss + Login Csrf

## Metadata

- HackerOne Report ID: 1092678
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-06-30T20:45:12.512Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
User can set username between 8-20 alphanumeric characters, but with the help of inspect element attacker can manipulate ```██████=``` & can insert a  xss payload resulting in self stored xss & with the help of  login csrf  attacker can force the victim into attacker's account causing successful execution of javascript.

█████████

Payload used = ```"><img src onerror=confirm(document.cookie)>```

## Impact

Able to execute javascript in victim's browser

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit [Sign in](███████) and sign in
2. Click on Change username -->  Open inspect element --> change max length of new username and confirm username to ```100```
3. Now enter the payload in``` new username```  and  ```confirm username``` field & click on submit --> Sign out
4.  Enter the credentials to sign in --> Intercept request using burp --> Action --> Engagement Tools --> Generate Csrf poc --> Copy html.
5. Open notepad & paste --> save as .html file
6. Open the html file in any browser to confirm the vulnerability.

Poc attached :-

███████

## Suggested Mitigation/Remediation Actions
Sanitization of input must be done

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
