---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2018615'
original_report_id: '2018615'
title: HTML injection on newsroom.snap.com/* via search?q=1
weakness: Code Injection
team_handle: snapchat
created_at: '2023-06-08T20:23:08.284Z'
disclosed_at: '2023-08-14T16:46:05.200Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: web.snapchat.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# HTML injection on newsroom.snap.com/* via search?q=1

## Metadata

- HackerOne Report ID: 2018615
- Weakness: Code Injection
- Program: snapchat
- Disclosed At: 2023-08-14T16:46:05.200Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi security team members,

Hope you are well!

I found an unauthenticated HTML injection in the browser of NewRooms section: https://newsroom.snap.com/[code_country]/*. It is possible to inject any HTML code from the "?q=" parameter of the following endpoints newsroom.snap.com/[code_country]/search?q= since the text input in the search engine is not sanitized at all.

The steps to reproduce the attack are:

1. Inject any HTML code into the URL: https://newsroom.snap.com/es-ES/search?q=%3Ca%20style=%22position:absolute;margin:50px;%20background-color:%20yellow;%20z-index:1000;top:50px;padding:100px;font-weight:bold;font-size:45px;color:red;%22%20href=%22https://evil.com%22%3EClick%20here%20for%20win%201000%E2%82%AC!%3C/a%3E

2. In this PoC example, an attacker would send this seemingly legitimate URL to victims pretending that Snapchat is offering money as an excuse. In reality, these users would access the attacker's website (https://evil.com/) if they click on the <a></a> element.

## Impact

An attacker can inject as much HTML code as desired and edit the style of the website to cause a Defacement in order to deceive users through Phishing, links to other websites controlled by the attacker through scams,... . There are many scenarios .

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
