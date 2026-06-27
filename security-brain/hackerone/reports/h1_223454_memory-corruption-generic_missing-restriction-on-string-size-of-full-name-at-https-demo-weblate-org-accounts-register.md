---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223454'
original_report_id: '223454'
title: Missing restriction on string size of Full Name at https://demo.weblate.org/accounts/register/
weakness: Memory Corruption - Generic
team_handle: weblate
created_at: '2017-04-24T14:01:33.917Z'
disclosed_at: '2017-05-18T02:55:15.105Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- memory-corruption-generic
---

# Missing restriction on string size of Full Name at https://demo.weblate.org/accounts/register/

## Metadata

- HackerOne Report ID: 223454
- Weakness: Memory Corruption - Generic
- Program: weblate
- Disclosed At: 2017-05-18T02:55:15.105Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there

#Vulnerability Title:
>During my regular testing, I have found that there was no restriction on the amount of text that can be inserted into a user's Full name field.
 
#Security Impact:
>When the text size was large enough the service  resulting in a momentary outage in our non-production environment (not high-availability). An internal reproduction showed isolated disruption but no outage in our production environment.

#Mitigation:
>To mitigate, please restrict limit of user input field of Full name like you have already enforced on the fields E-mail and User name. 

If you need more info, be free to ask.


Happy to help.

Regards,
@smit

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
