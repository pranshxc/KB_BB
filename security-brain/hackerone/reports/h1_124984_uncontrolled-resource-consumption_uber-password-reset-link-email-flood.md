---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124984'
original_report_id: '124984'
title: Uber password reset link EMAIL FLOOD
weakness: Uncontrolled Resource Consumption
team_handle: uber
created_at: '2016-03-27T19:15:02.391Z'
disclosed_at: '2016-06-13T22:13:35.019Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Uber password reset link EMAIL FLOOD

## Metadata

- HackerOne Report ID: 124984
- Weakness: Uncontrolled Resource Consumption
- Program: uber
- Disclosed At: 2016-06-13T22:13:35.019Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Step to reproduce Uber password reset link EMAIL FLOOD  POC Video https://youtu.be/PPJkO_Eo6Mw

1. Used OWSAP ZAP Proxy 
2. Generated the forgotten password Link of my account (anish2good@yahoo.co.in)
3. Used ZAP to replay the packet
4. The Number of replay resulting into number of password link email which causing the USER Inbox to flood with UBER SCAM 
5. Attaching the POC as Video  https://youtu.be/PPJkO_Eo6Mw

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
