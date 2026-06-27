---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49499'
original_report_id: '49499'
title: Generating Unlimited Free Travel Gift Invites | IDOR
weakness: Information Disclosure
team_handle: airbnb
created_at: '2015-02-27T17:43:23.007Z'
disclosed_at: '2015-04-04T17:14:22.465Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Generating Unlimited Free Travel Gift Invites | IDOR

## Metadata

- HackerOne Report ID: 49499
- Weakness: Information Disclosure
- Program: airbnb
- Disclosed At: 2015-04-04T17:14:22.465Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

After registration you can invite your friends to get some offer on there first trip. Notice that this system is flawed and attacker can generate as many invites he wants without going through the system at all.

Original Invite link:

http://www.airbnb.com/c/spent1?euid=ed736125-704e-f1ec-bb76-4ca60026141d&ri=14052412&s=30

Now i tweaked euid and ri. They can take any number as input and still generated valid gift card.

**https://www.airbnb.com/c/fun?euid=2&ri=14052213&s=30**

Also we can spoof user name as well by modifying part after c. 

See poc for full demonstration: https://drive.google.com/file/d/0B0ZK8lhjLLHwcDVCdjNodmd0Qk0/view?usp=sharing

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
