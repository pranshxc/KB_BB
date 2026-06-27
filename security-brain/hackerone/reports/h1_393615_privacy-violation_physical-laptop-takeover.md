---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '393615'
original_report_id: '393615'
title: Physical Laptop Takeover
weakness: Privacy Violation
team_handle: ed
created_at: '2018-08-12T08:11:13.442Z'
disclosed_at: '2018-08-12T08:19:12.741Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 343
asset_identifier: Personal machine
asset_type: HARDWARE
max_severity: none
tags:
- hackerone
- privacy-violation
---

# Physical Laptop Takeover

## Metadata

- HackerOne Report ID: 393615
- Weakness: Privacy Violation
- Program: ed
- Disclosed At: 2018-08-12T08:19:12.741Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

At 6:16PM of August 11th of 2018, during H1-702, right before the sand storm beat the shit out of the rooftop party, we managed to perform a critical attack on Ed's infrastructure.
{F332214}

## Report Summary

During our analysis and reconnaissance of how Ed program worked during the h1-702 event, we realized there was a critical flaw on how the program was setup. 

## Report Description

During the process, we realized that the program manager had tendency to leave secrets open in the wild. While analyzing this, we decided to look into hardware hacking. So as we looked around, we found that the owner of the program left their computer open. What was worse is that it allowed us to to use this to exploit this and get root access into multiple services. 

{F332215}

After we had access to the laptop, we decided to start the first exploiting for PoC by taking a screenshot of our team. This helps to prove that we could do anything we wanted.

## Impact

Access to internal documentations, Ed program statistics and internal details.

##MOST IMPORTANT IMPACT

Shame Ed on the company Slack

{F332216}

**_The Triage send their regards!_**

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
