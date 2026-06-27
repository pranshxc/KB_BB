---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77319'
original_report_id: '77319'
title: Full path disclosure at https://keybase.io/_/api/1.0/invitation_request.json
weakness: Information Disclosure
team_handle: keybase
created_at: '2015-07-21T13:27:47.914Z'
disclosed_at: '2015-09-04T18:16:23.265Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full path disclosure at https://keybase.io/_/api/1.0/invitation_request.json

## Metadata

- HackerOne Report ID: 77319
- Weakness: Information Disclosure
- Program: keybase
- Disclosed At: 2015-09-04T18:16:23.265Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When we send a POST-request to https://keybase.io/_/api/1.0/invitation_request.json with multiple __full_name__ parameters, for example:

> email=test@testmail.com&full_name=1&full_name=2

we get an error response, which contains infromation about the server paths and code:

> TypeError: Object 1,2 has no method &#39;replace&#39;<br> &nbsp;at Object.exports.faves.faves.full_name [as check] (/home/keybase/src/keybase/keybase/lib/checkers.iced:379:13)<br> &nbsp;at InvitationRequestHandler.exports.Handler.Handler.get_input (/home/keybase/src/keybase/keybase/lib/websrv_base.iced:129:20)<br>
etc.

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
