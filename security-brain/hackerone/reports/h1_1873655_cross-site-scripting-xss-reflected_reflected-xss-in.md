---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1873655'
original_report_id: '1873655'
title: Reflected XSS in ██████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2023-02-14T12:27:40.329Z'
disclosed_at: '2023-03-24T17:30:54.641Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in ██████

## Metadata

- HackerOne Report ID: 1873655
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-03-24T17:30:54.641Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
XSS vulnerability found on one of `█████` subdomains. [ DoD scope]

After analyzing `https://████████/`(██████████), I found  `Admin/Notifications/PreviewLetterhead.aspx` page that have `emailbody` parameter in `GET` request.  `emailbody` parameter vulnerable to XSS vulnerability.

`https://███/` requires a valid user to access the contents, but the registration page is accessible to all visitors without any restrictions or credentials.

███████
- Email confirmation is not required during the registration process.
- There is no limit to the use of disposable email addresses.

A valid registered user can access the target page after login.
By modifying `emailbody` parameter  and set the payload to `emailbody=0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;` the alert box has been triggered.

To bypass WAF, the payload encoded using these method:
1. `0xd3adc0de<ScRiPt>alert('XSS Success!')</sCripT>`
2. HTML encode: `0xd3adc0de&lt;ScRiPt&gt;alert('XSS Success!')&lt;/sCripT&gt;`
3. URL encode: `0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;`

Payload:
`https://██████████/Admin/Notifications/PreviewLetterhead.aspx?emailbody=0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;`
███

----


**Bonus: Information leakage**
Some information is leaked on the registration page, I have no idea about the level of confidentiality but I think you should review them. Such as `Organization` and `Manager` field is interesting.
-  About `162 organization` listed on registration page.
█████████

- About `144366 manager` listed on registration page.
████


## References
https://owasp.org/www-community/attacks/xss/

## Impact

By exploiting this vulnerability an attacker can trick the users to execute XSS and steal user's cookies.
Launch advanced phishing attacks.
Execute browser-based attacks etc.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit the following URL 
`https://█████`

* Login into system using a valid user credential or if you haven't so go to registration page and take one. `https://██████/Disclaimer.aspx?user=new`

* After success login, change the URL to `https://█████/Admin/Notifications/PreviewLetterhead.aspx?emailbody=0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;` and you will receive `XSS Success!` alert box.

## Suggested Mitigation/Remediation Actions

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
