---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148897'
original_report_id: '148897'
title: '[Thirdparty] Stored XSS in chat module - nextcloud server 9.0.51 installed
  in ubuntu 14.0.4 LTS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-07-02T18:29:25.357Z'
disclosed_at: '2016-11-02T16:08:07.264Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [Thirdparty] Stored XSS in chat module - nextcloud server 9.0.51 installed in ubuntu 14.0.4 LTS

## Metadata

- HackerOne Report ID: 148897
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-11-02T16:08:07.264Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found stored XSS vulnerability in nextcloud server's chat module

Nextcloud Server version - 9.0.51
OS - Ubuntu 14.0.4
Browser - Internet Explorer 11

Steps:
1) Login as non-admin user(attacker) and change full name containing XSS payload - elamaran\'>\"><script>alert(document.domain)</script>
2) Login as admin/non-admin(victim) and go to chat module
3) Click "Show information" of the attacker
4) Then the stored XSS payload in attacker's name will get execute in nextcloud domain

POC Video URL - https://youtu.be/UU60IthJWxI

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
