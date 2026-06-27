---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '357576'
original_report_id: '357576'
title: Exposing hackerone users personally identifiable information by abusing sandbox
  with swag reward enabled
weakness: Information Disclosure
team_handle: security
created_at: '2018-05-25T17:13:56.730Z'
disclosed_at: '2018-06-07T01:19:43.684Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 18
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Exposing hackerone users personally identifiable information by abusing sandbox with swag reward enabled

## Metadata

- HackerOne Report ID: 357576
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-06-07T01:19:43.684Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi HackerOne Team,

**Summary:**

I have found a critical bug but this will require a bit user interaction, __BUT__ please take note that once exploited, a hackerone user's __PII - personally identifiable information__ can be exposed. I have found this bug by using the __sandbox__ with swag reward enabled .

---

Let me explain first on how this work, basically when the program reward a swag to a hacker, all the hacker swag information here: `https://hackerone.com/settings/swags` will be send to the program owner for proper shipping etc. and can be seen on this end point: `https://hackerone.com/<program_handle>/swag`

__Now i have found a way to use that to expose a Co-hackers PII listed below:__

- __Complete Name__
- __Street__
- __City__
- __State/Province__
- __Postal Code__
- __Country__
- __Phone Number__

The question is how ? , please see below steps.

### Steps To Reproduce

  1. Create a sandbox program and enable the swag rewarding `On`
  2. Now add any team member, base on my experience most hackers are interested to collaborate when you add them to the sandbox.
  3. New team member will most likely play with the sandbox like __Creating test report__, closing reports, rewarding etc.
  4. __NOW THIS IS THE BUG__, when the hackers invited to the sandbox, and then they created a test report, the program owner can reward a swag and then expose their __PII__, because the sandbox program owner can see all of the swag information here: `https://hackerone.com/<program_handle>/swag`

---
### LIVE EXPLOITATION
---

I invited a co-hacker to my sandbox, his hackerone username is https://hackerone.com/█████████ , he joined and play with the sandbox, __WITHOUT KNOWING__ that when he submitted a test report, I already exposed his PII because i rewarded his submitted report a swag, please see below information belonging to him.

 __Complete Name:__ `██████████`
__Street:__ `████`
__City:__ `███████`
__State/Province:__ `███`
__Postal Code:__ `████`
__Country:__ `██████████`
__Phone Number:__ `███`

The other information on the screenshot is for Name: [John Doe](https://hackerone.com/demo-hacker) and those information is belonging to the demo-member.

This bug can be used to expose any target of your choice :)

{F301676} 

### Mitigation:

Hackers swag information (PII) should not send to the __Sandbox or Non-approved program owner__ since this is a testing only and live production hacker information should not be able to disclosed!.

## Impact

Information disclosure, exposing hackerone users personally identifiable information.

Let me know if anything else is needed, please ask question if you are having trouble understanding my report, I'd be glad to provide as much as information if needed. 

Regards
Japz

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
