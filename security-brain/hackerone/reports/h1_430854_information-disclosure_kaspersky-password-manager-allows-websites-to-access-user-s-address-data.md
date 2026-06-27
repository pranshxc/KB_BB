---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '430854'
original_report_id: '430854'
title: Kaspersky Password Manager allows websites to access user's address data
weakness: Information Disclosure
team_handle: kaspersky
created_at: '2018-10-30T13:30:18.432Z'
disclosed_at: '2019-11-24T08:59:07.600Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
tags:
- hackerone
- information-disclosure
---

# Kaspersky Password Manager allows websites to access user's address data

## Metadata

- HackerOne Report ID: 430854
- Weakness: Information Disclosure
- Program: kaspersky
- Disclosed At: 2019-11-24T08:59:07.600Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

*Note*: According to https://www.securityweek.com/kaspersky-adds-password-manager-bug-bounty-program and some other sources, Kaspersky Password Manager is in scope for this program. The program description doesn't reflect this however.

**Summary**

It is possible for websites to read out addresses that the user stores in Kaspersky Password Manager.

**Description**
Kaspersky Password Manager injects its user interface into untrusted web pages, there are no protections in place. This makes it easy for websites to instrument the user interface, e.g. to fill in addresses without the user's consent or knowledge.

**Environment**
- Scope: Application
- Product name: Kaspersky Password Manager, browser extensions installed
- Product version: 9.0.1.447
- OS name and version (incl SP): Windows 10 Version 1803
- Attack type: Information Disclosure
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
1. Make sure to unlock Kaspersky Password Manager and to add an address. The actual address part should be a single line (filling in fails for multiline values with my PoC which could certainly be addressed if necessary).
2. Download the attached extract_address.html and open it via any web server (localhost will do).
3. Go to http://.../extract_address.html with your browser (I tried Firefox 62 but this should work in Chrome as well) and wait a few seconds.

An alert message will pop up telling your name and address. This information could be sent to a third party without you noticing anything.

## Impact

This allows to deanonymize and to track users, the address being a particularly valuable piece of information. Privacy conscious users will still be recognized reliably, even if clearing cookies and using proxy servers. In addition, advertisers will certainly love the possibility of telling exactly where the person lives - makes for some great targeting.

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
