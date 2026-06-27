---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '327674'
original_report_id: '327674'
title: Invitation reminder emails contain insecure links
weakness: Cryptographic Issues - Generic
team_handle: slack
created_at: '2018-03-20T08:18:16.412Z'
disclosed_at: '2019-06-29T12:55:54.689Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cryptographic-issues-generic
---

# Invitation reminder emails contain insecure links

## Metadata

- HackerOne Report ID: 327674
- Weakness: Cryptographic Issues - Generic
- Program: slack
- Disclosed At: 2019-06-29T12:55:54.689Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If one gets invited to a slack channel and does not act upon the invitation a while later a reminder email is sent.

The links in these reminders are http links. Excerpt from the mail:
----------------------
Don’t miss out — come join the conversation!

Join Now
http://click.email.slack-core.com/?qs=[id removed]
----------------------

This poses an unnecessary risk that the connections can be intercepted and redirected by an attacker.

This is particularly surprising and unnecessary as:
1. The links directly redirect to an https URL.
2. The initial invitation mail contains no such indirect link, it directly links to https.

## Impact

Attackers that are in the same network as a person receiving an invitation reminder mail can do a man in the middle attack and redirect the victim to a forget fake slack webpage.

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
