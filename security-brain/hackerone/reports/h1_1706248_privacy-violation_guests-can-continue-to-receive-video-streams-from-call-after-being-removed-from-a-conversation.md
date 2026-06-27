---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1706248'
original_report_id: '1706248'
title: Guests can continue to receive video streams from call after being removed
  from a conversation
weakness: Privacy Violation
team_handle: nextcloud
created_at: '2022-09-20T15:46:19.992Z'
disclosed_at: '2022-12-31T09:35:12.717Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: nextcloud/spreed
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Guests can continue to receive video streams from call after being removed from a conversation

## Metadata

- HackerOne Report ID: 1706248
- Weakness: Privacy Violation
- Program: nextcloud
- Disclosed At: 2022-12-31T09:35:12.717Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

If the HPB is used and a guest is removed from a conversation while said guest is in a call the guest will no longer appear in the participant list and the call will appear as ended for the other participants. However, for the guest the call UI is still shown. If other participants start a call the guest will automatically establish connections with them (so she will be able to hear and see the other participants), but from the point of view of the rest of the participants the guest is not in the call and she is not shown in their UI.

This can be reproduced only for guests and when the HPB is used. It could be related to https://github.com/nextcloud/spreed/issues/7962

## Steps To Reproduce:

- Setup the HPB
- Create a public conversation
- In a private window, open that public conversation as a guest
- Start a call
- In the original window, delete the guest
- Start a call again

### Expected result

The guest was kicked out from the call and she can not see nor hear the participants joining after that

### Actual result

The guest was, according to the system messages for other participants, kicked out from the call, but the call UI is still shown for her and connections will be established to participants joining after that (and those new participants will not be aware of the guest being still in the call)

## Impact

An attacker would be able to spy on calls in a public conversation after being removed from that conversation, provided that she was removed while being in the call.

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
