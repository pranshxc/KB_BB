---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265987'
original_report_id: '265987'
title: Add another email address without verification
weakness: Improper Access Control - Generic
team_handle: weblate
created_at: '2017-09-05T09:45:13.811Z'
disclosed_at: '2017-10-05T12:24:43.391Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Add another email address without verification

## Metadata

- HackerOne Report ID: 265987
- Weakness: Improper Access Control - Generic
- Program: weblate
- Disclosed At: 2017-10-05T12:24:43.391Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Introduction
In the normal case, to link another email address to the Weblate account, users need to own the email address and click the verification link. However, I found an issue, that allows adding another email address without clicking on the verification link.

## Description and PoC:
* Create a new openSUSE ID. Pick up a new email. In this example, I choose `admin@weblate.org`.
{F218492}
Of course, you don't need to verify the email address for this openSUSE ID.

* Then backs to weblate.org, go to Your profile > Authentication `https://demo.weblate.org/accounts/profile/#auth`.
Add the above openSUSE account as a new association.
{F218493}

* That all, go to Account tab `https://demo.weblate.org/accounts/profile/#account`, you will see the new email in your account's email field.
{F218494}

## Mitigation
Weblate should only accept the association from verified openSUSE ID.

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
