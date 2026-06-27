---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175366'
original_report_id: '175366'
title: 'Brave: Admin Panel Access'
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2016-10-12T11:27:09.688Z'
disclosed_at: '2017-08-10T05:11:23.792Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Brave: Admin Panel Access

## Metadata

- HackerOne Report ID: 175366
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2017-08-10T05:11:23.792Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

** Steps to reproduce**

While browsing through the https://blog.brave.com/admin, it is getting redirected to a admin login panel https://brave.ghost.io/ghost/signin/.

**Consequence**
An attacker can easily enumerate this admin panel with the url such as https://blog.brave.com/admin
and with brute force attack this can be bypassed, but I didn't do that. If a known ghost.io vulnerability exists there can be chances of even taking over the sub domain.

**Remediation**

 It's recommended to give custom directory names instead of easily guessable names such as "admin" for such sensitive directories.

Please find the attached screenshots.

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
