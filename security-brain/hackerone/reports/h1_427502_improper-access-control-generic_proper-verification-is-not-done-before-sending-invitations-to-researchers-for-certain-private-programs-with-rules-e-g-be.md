---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '427502'
original_report_id: '427502'
title: Proper verification is not done before sending invitations to researchers for
  certain private programs with rules e.g. "Participants must be US-based"
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2018-10-23T20:27:34.452Z'
disclosed_at: '2018-11-07T21:28:17.188Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Proper verification is not done before sending invitations to researchers for certain private programs with rules e.g. "Participants must be US-based"

## Metadata

- HackerOne Report ID: 427502
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2018-11-07T21:28:17.188Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I would like to report something I just recently noticed upon receiving an automated invite from Hackerone for a private program. The program brief clearly states the following in program rules:

█████

This is where I believe the issue is. 

I live in ███ and according to the program rules I believe I should not be eligible to participate in this particular program since I am not based in the US however my observation is that currently there are no checks in place on Hackerone platform for this sort of validation and automated private invites are sent to random researchers who meet the criteria based on their reputation without validating if the researcher meets the "Locality and Jurisdiction" bar.

[+] Proof of concept:

Program that has the Locality/Jurisdiction rule in place:

█████████

Screenshot evidence of received email:

██████


Screenshot evidence that I was able to successfully accept the invite and now participating in the program successfully:

█████████


[+] Solution:

In this case, before sending an invitation to me, my profile should have been validated specially my location since this program has specific requirements regarding US based researchers only.

## Impact

Worst, This could cause "lawsuit" related issues/disputes between all parties and or any similar sort of a legal problem.

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
