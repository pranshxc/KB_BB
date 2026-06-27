---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1892317'
original_report_id: '1892317'
title: XSS Reflected
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2023-03-04T23:05:17.249Z'
disclosed_at: '2023-09-08T17:19:43.676Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected

## Metadata

- HackerOne Report ID: 1892317
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-09-08T17:19:43.676Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,

It was found a xss reflected in your web asset.

Reflected Cross-site Scripting (XSS) occur when an attacker injects browser executable code within a single HTTP response.When a web application is vulnerable to this type of attack, it will pass unvalidated input sent through requests back to the client.

## Steps To Reproduce:

  1. Access the url `https://███.aspx/%22%20onmouseover=%22prompt(1)%22%20x=%22`
  2. See the popup in the screen

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]


███

## Impact

## Impact
* An attacker that can control the code executed in a victim browser can usually fully compromise this victim. This includes :
* Perform any action within the application that the user can perform.
* Modify any information that the user is able to modify.
* Steal user cookies
* Redirect to phishing site
* Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
* Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
* Run Arbitrary javascript code into victim's browser

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Access the url `https://███████.aspx/%22%20onmouseover=%22prompt(1)%22%20x=%22`
  2. See the popup in the screen

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
