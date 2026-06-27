---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181816'
original_report_id: '181816'
title: '[marketplace.informatica.com] Persistent XSS through document title'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-11-12T19:57:22.548Z'
disclosed_at: '2017-02-02T04:29:44.457Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [marketplace.informatica.com] Persistent XSS through document title

## Metadata

- HackerOne Report ID: 181816
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-02-02T04:29:44.457Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Document titles are not properly escaped before being printed on https://marketplace.informatica.com/docs/ . By including a payload in a document title, an attacker can create a document with a persistent XSS vector which executes for anyone viewing the document page.

Proof of concept
===
The following steps are accompanied by screenshots attached to this report.

1. Log into https://marketplace.informatica.com/ and go to your profile page. Select New -> Document.
2. Choose a location for your new document - "Your Documents" will work just fine.
3. Enter some text in the document body and insert the following XSS vector in the document title: `";alert("XSS in "+document.domain);//`
4. Hit "Publish" on the bottom of the page.
5. Visiting the document page causes the XSS payload to execute.

This test was performed using Mozilla Firefox 49.0.2 and was also confirmed in Google Chrome 54.0.2840.87. The exploit should work in any browser, as the persistent payload cannot be distinguished from a legitimate script from the server.

Recommended solution
===
Make sure to correctly output encode the document title before printing it to a javascript scope of the document page.

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
