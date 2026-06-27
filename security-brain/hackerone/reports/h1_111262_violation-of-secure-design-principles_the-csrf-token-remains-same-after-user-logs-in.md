---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111262'
original_report_id: '111262'
title: The csrf token remains same after user logs in
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2016-01-17T15:23:57.058Z'
disclosed_at: '2016-02-25T21:13:44.298Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# The csrf token remains same after user logs in

## Metadata

- HackerOne Report ID: 111262
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2016-02-25T21:13:44.298Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

As the CSRF token doesn't change after login. Any other user that uses the same workstation is vulnerable. A safer way would be to use dynamic CSRF token or just change the token after login, so attacker doesnt get hold of this.

Details of the attacks scenario in a shared workstation environment

1.The attacker simply copies the authenticity token. This token is the only protection against the CSRF attack.

2.Any other user that uses the workstation after that is vulnerable to CSRF. The attacker simply needs to craft a link with the required GET or POST method as he already have the CSRF token and send it to the victim via email, chat etc.

3.The attacker can trick the victim in doing anything he wants without the user being aware of it.

In the most basic sense the attacker has an authenticity token of another user which he shouldn't have had in the first place.

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
