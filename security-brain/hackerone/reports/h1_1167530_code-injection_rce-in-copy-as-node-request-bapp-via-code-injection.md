---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167530'
original_report_id: '1167530'
title: RCE in 'Copy as Node Request' BApp via code injection
weakness: Code Injection
team_handle: portswigger
created_at: '2021-04-18T03:45:36.252Z'
disclosed_at: '2021-04-22T00:35:37.097Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 49
asset_identifier: Burp Suite Extension (BApps)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: none
tags:
- hackerone
- code-injection
---

# RCE in 'Copy as Node Request' BApp via code injection

## Metadata

- HackerOne Report ID: 1167530
- Weakness: Code Injection
- Program: portswigger
- Disclosed At: 2021-04-22T00:35:37.097Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description
`Copy as Node Request` is a burp suite extension that allows users to copy requests as Node.js code.
Due to improper sanitization of cookie,  it's possible to inject arbitrary Node.js code in copied text, which may lead remote code execution with a significant amount of user interaction.

## Root cause
This extension has a function named `escapeQuotes`.
While this function escapes double quotes, it doesn't escape single quotes.
https://github.com/PortSwigger/copy-as-node-request/blob/b34456463310836e93365541189626909adc70bb/src/burp/BurpExtender.java#L165-L167
As the cookie field of generated codes use single quote, it's possible to escape string literal and inject arbitrary Node.js codes.
https://github.com/PortSwigger/copy-as-node-request/blob/b34456463310836e93365541189626909adc70bb/src/burp/BurpExtender.java#L123-L125

## Step to reproduce
1. Install [Copy as Node Request extension](https://portswigger.net/bappstore/e170472f83ef4da1bca5897203b6b33d).
2. Open https://example.com
3. Open DevTools and type `document.cookie = "test='/require('child_process').exec('calc.exe')//"`
4. Enable intercept and reload the browser tab.
5. Right click on intercepted request and click `Copy as Node.js Request`.
6. Execute copied text in Node.js.
7. `calc.exe` will be popped up.

{F1269399}

## Impact

Remote code execution via Node.js code injection with user interaction.

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
