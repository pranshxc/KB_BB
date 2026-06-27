---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118684'
original_report_id: '118684'
title: Abusing HOF rankings in limited circumstances
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-02-25T05:17:19.874Z'
disclosed_at: '2016-04-21T22:43:46.657Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Abusing HOF rankings in limited circumstances

## Metadata

- HackerOne Report ID: 118684
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-21T22:43:46.657Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

HI,

I think you will close this as NA but i think you should resolve this bug at some point. 


As we know submitting duplicate report of valid report earns you +2 point and also gives you HOF(known bug).

So you will appear in team's HOF as https://hackerone.com/security/thanks with 2 points

Now how this can be abused  further to enhance your reputation points which will ultimately yields you higher ranking in HOF

So if you have points in HOF with points
 _Greater than 0 and less than 5_

here how we can abuse it further
Pre-Requistes
1.you are in HOF of some team with points greater than 0 and less than 5

Steps
1. submit a valid report
2.team closes the report as NA. at this point your main reputations will go -5. but in HOF it will become 0 as it cant go in negatives.
3.you send more info
4.Team reopens the bug.
5. now in HOF, instead of restoring your old points(which is less than 5), it will give +5 point
6. So even if they close the report to informative later, you got +5 points without resolving any of your report!

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
