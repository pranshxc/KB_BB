---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222036'
original_report_id: '222036'
title: Missing SSL can leak job token
weakness: Cleartext Transmission of Sensitive Information
team_handle: wordpress
created_at: '2017-04-18T23:36:48.264Z'
disclosed_at: '2017-11-01T18:33:56.324Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Missing SSL can leak job token

## Metadata

- HackerOne Report ID: 222036
- Weakness: Cleartext Transmission of Sensitive Information
- Program: wordpress
- Disclosed At: 2017-11-01T18:33:56.324Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Description:

The Web app jobs.wordpress.net transmits sensitive data in cleartext in a communication channel that can be sniffed by unauthorized actors.

Attack Scenario:

Attacker simply monitors network traffic (like an open wireless network), and steals the user’s session cookie. Attacker then replays this cookie and hijacks the user’s session, accessing the user’s private data.

This could leak Job token, leak user information and jobs created by users. 

Thanks,
Diogo Real

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
