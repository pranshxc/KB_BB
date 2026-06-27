---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178611'
original_report_id: '178611'
title: Reflected XSS on Zones > Invocation Code
weakness: Cross-site Scripting (XSS) - Generic
team_handle: revive_adserver
created_at: '2016-10-28T15:02:11.443Z'
disclosed_at: '2017-08-02T05:58:41.884Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on Zones > Invocation Code

## Metadata

- HackerOne Report ID: 178611
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: revive_adserver
- Disclosed At: 2017-08-02T05:58:41.884Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**"Cricetinae"** :)

This report is similar to my earlier report: #170156.

### Short Description
The **Close text** parameter in *Inventory > Zone > Invocation Code* is vulnerable to Cross-Site Scripting vulnerability.

### Steps to Reproduce
1. Logon or Work as an agent.
2. Navigate to Inventory > Zones > Invocation Code. Create Websites & Zones records if empty.
3. Enter  `[Close]something'/><script>alert(1);</script><span class='1` for **Close text**.
4. Note the javascript alert box triggered from the payload entered above.
Chrome's default XSS Protection blocks simple XSS payloads. Please use firefox for reproduction or disable Chrome's security.

### Vulnerability Details
Cross-Site Scripting issue let's one to run a javascript of choice. It helps most of the client side risks including but not limited to phishing, temporary deface, browser key-logger and others. Exploitation frameworks like BeEF eases the offensive attack.

### Attack Vector
Though this may be treated as a Self-XSS, the place where the issue is affecting is sensitive. If the user who is going to set up the Revive Adserver, follows an untrusted malicious guide which contains specially crafted XSS payload, can help in gaining access to the database by tricking him to enter the credential in attacker's site by redirecting or any other way.

###Test Environment Details
**Version**: Latest as on Oct 28: revive-adserver-4.0.0 downloaded from official website
**Setup type**: local
**Browser**: Firefox 47.0
**OS**: Mac OS X

Cheers,
Pavan

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
