---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '505424'
original_report_id: '505424'
title: Twitter ID exposure via error-based side-channel attack
weakness: Privacy Violation
team_handle: x
created_at: '2019-03-06T01:48:00.607Z'
disclosed_at: '2019-05-16T22:16:07.460Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 150
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Twitter ID exposure via error-based side-channel attack

## Metadata

- HackerOne Report ID: 505424
- Weakness: Privacy Violation
- Program: x
- Disclosed At: 2019-05-16T22:16:07.460Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Twitter ID Confirmator
===

## Summary
Recently I discovered a privacy-related vulnerability in Twitter. An attacker exploiting this vulnerability can identify a user when they visit a malicious website.

## Description
**Threat model:** The attacker knows the victim’s Twitter ID/username and aims at identifying them when visiting one of the controlled websites such as a blog or a news website. Another goal that the attacker could wish to achieve is to identify a user out of a group of potential target users. 

**Vulnerability**
I found out that a user-related content is being loaded when visiting the developer tools and that is https://developer.twitter.com/api/users/USER_ID/client-applications.json. If the USER_ID is different from the ID of a currently logged in user the error 403 will be returned with the following JSON output
```json
{"error":{"message":"You are not logged in as a user that has access to this developer.twitter.com resource.","sent":"2019-03-06T01:20:56+00:00","transactionId":"00d08f800009d7be"}}. 
```
Otherwise, a list of created apps will be displayed (the list will be empty if the user didn't create any app) and no error will be thrown.

It is possible to detect whether the file returned an error or not by a simple onload/onerror event handlers. The example code is shown in [#Steps-to-reproduce](#Steps-to-reproduce)


## Steps to reproduce
1. Visit any website
2. Execute the following javascript code while replacing `Your ID` with an ID you want to test for

```javascript
var id = 'Your ID'
var script = document.createElement('script');
script.src = `https://developer.twitter.com/api/users/${id}/client-applications.json`;

script.onload = () => console.log('ID match');
script.onerror = e => console.log('ID mismatch');
document.head.appendChild(script);
```

These steps have been implemented in the Proof of Concept: https://terjanq.github.io/Bug-Bounty/Twitter/confirming-username/poc.html

PoC in action: https://youtu.be/_S_ImYPvvhc

## Impact

An attacker can expose the identity of Twitter users when they visit a prepared for that purpose website.

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
