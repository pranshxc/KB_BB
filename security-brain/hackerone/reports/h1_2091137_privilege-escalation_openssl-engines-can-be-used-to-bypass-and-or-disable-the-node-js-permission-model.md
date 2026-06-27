---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2091137'
original_report_id: '2091137'
title: OpenSSL engines can be used to bypass and/or disable the Node.js permission
  model
weakness: Privilege Escalation
team_handle: ibb
created_at: '2023-07-31T23:00:54.980Z'
disclosed_at: '2023-10-07T18:27:53.656Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# OpenSSL engines can be used to bypass and/or disable the Node.js permission model

## Metadata

- HackerOne Report ID: 2091137
- Weakness: Privilege Escalation
- Program: ibb
- Disclosed At: 2023-10-07T18:27:53.656Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Node.js 20 allows loading arbitrary OpenSSL engines even when the permission model is enabled, which can bypass and/or disable the permission model.

**Description:** The permission model implementation permits loading arbitrary native code, e.g., through `crypto.setEngine()`, even when native addons are disallowed, which is the default configuration. Not only can this code bypass the permission system, it can also disable the permission system entirely, effectively allowing JavaScript code to escalate its own privileges.

## Steps To Reproduce:

  1. Enable the permission model.
  2. Call, for example, `crypto.setEngine()` with a compatible OpenSSL engine.
  3. Arbitrary code execution occurs, unaffected by the permission model.

## Impact

The permission model is supposed to restrict the capabilities of running code. However, exploiting this vulnerability allows an attacker to easily bypass the permission model entirely. The OpenSSL engine can, for example, disable the permission model in the host process, and subsequently executed JavaScript code will be unaffected by the previously enabled permission model. This allows running JavaScript code to effectively elevate its own permissions.

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
