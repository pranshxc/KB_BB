---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '491753'
original_report_id: '491753'
title: DMARC RECORD MISSING
team_handle: brave
created_at: '2019-02-06T05:55:05.627Z'
disclosed_at: '2019-02-13T18:59:01.401Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
---

# DMARC RECORD MISSING

## Metadata

- HackerOne Report ID: 491753
- Weakness: 
- Program: brave
- Disclosed At: 2019-02-13T18:59:01.401Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

VULNERABILITY TYPE- DMARC RECORD MISSING.
HOW TO REPRODUCE(POC-ATTACHED IMAGE):-
1.GO TO- https://mxtoolbox.com
2.ENTER THE WEBSITE(brave.org).CLICK GO.
3.YOU WILL SEE THE FAULT(No DMARC Record found)
4.In the new page that loads change MXLookup to DMARCLookup
I HAVE ALREADY INFORMEDD THEM.THEY TOLD TO OPEN THE ISSUE IN HackerOne.(POC-ATTACHED IMAGE)

## Impact

Spammers can forge the "From" address on email messages to make messages appear to come from someone in your domain. If spammers use your domain to send spam or junk email, your domain quality is negatively affected. People who get the forged emails can mark them as spam or junk, which can impact authentic messages sent from your domain.

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
