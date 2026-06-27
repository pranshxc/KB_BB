---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137503'
original_report_id: '137503'
title: Inadequate access controls in "Vote" functionality???
weakness: Privilege Escalation
team_handle: security
created_at: '2016-05-10T14:52:20.183Z'
disclosed_at: '2016-05-12T01:44:01.289Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- privilege-escalation
---

# Inadequate access controls in "Vote" functionality???

## Metadata

- HackerOne Report ID: 137503
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2016-05-12T01:44:01.289Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
First of all let me congratulate you for including pornhub in the list of bug bounty programs, me and my colleagues will have a lot of fun with it hahahahahah. Awesome...

Anyways, I stumbled upon something whilst testing hackerone's main site. I don't know if it's a feature that it's going to be implemented soon or if it's something internal, I also have no idea if there are any risks involved in this, I'm confident you'll be accurate in your evaluation.

I started just for fun removing every "disabled" from every control on the web page and changing every "false" for a "true" on every json request, just to see what popped up, I've still have to cover the whole page and try everything to see that there are no client-side only reliant validations on the web page and/or info disclosure, but suddenly on the "Hacktivity" page this "vote buttons" appeared, and to my suprise, when I clicked one of them to go through as a request and assign a "vote id". I of course deleted my vote afterwards, I have no idea what I'm affecting.

Anyways, the endpoint seems to be in https://hackerone.com/reports/[Report_ID]/votes, which accepts the POST method and https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID] which accepts the DELETE method.

The fix would be fairily easy, implement server-side controls in order to prevent unauthorized users from using this feature.

Please let me know if this is something you would be interested in and we'll work together to fix it if necessary. Otherwise, please just mark it as informational.

I'm also including screenshots with both requests and responses.

Kind Regards,
Apok.

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
