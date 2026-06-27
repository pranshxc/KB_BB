---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1554888'
original_report_id: '1554888'
title: Site information's Display Name section vulnerable for XSS attacks and HTML
  Injections.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2022-04-29T19:56:51.592Z'
disclosed_at: '2022-05-16T13:59:43.887Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: my.pressable.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Site information's Display Name section vulnerable for XSS attacks and HTML Injections.

## Metadata

- HackerOne Report ID: 1554888
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2022-05-16T13:59:43.887Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi, 

Greetings. I have found that site information's Display Name section on the try.pressable.com is vulnerable for potential  XSS attacks and HTML Injections.

## Steps To Reproduce:
1. Visit https://try.pressable.com
2. Create a new site.
3. On the  Display Name section, put the XSS / HTML Injection payloads.
4. XSS will be triggered/ Injected HTML will be reflected.

XSS Payload:  "><img src=x onerror=javascript:alert(document.cookie)>

HTML Payload: 
<form action="/action_page.php">
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname"><br><br>
<label for="lname">Last name:</label>
<input type="text" id="lname" name="lname"><br><br>
<input type="submit" value="Submit">
</form>

## Supporting Material/References:
POC Video attached

## Impact

Due to these vulnerabilities, attacker can easily divert victims to their malicious site and able to get credentials of victims.

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
