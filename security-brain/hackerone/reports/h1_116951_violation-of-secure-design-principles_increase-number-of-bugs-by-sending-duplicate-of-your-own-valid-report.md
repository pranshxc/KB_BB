---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116951'
original_report_id: '116951'
title: Increase number of bugs by sending duplicate of your own valid report
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-02-17T15:12:52.033Z'
disclosed_at: '2016-04-25T04:43:10.026Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Increase number of bugs by sending duplicate of your own valid report

## Metadata

- HackerOne Report ID: 116951
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-25T04:43:10.026Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI,

This report is a basically a design issue and something similar to report where someone can gain reputations by sending dup. Not very high severity bug and i know you all can always roll back the changes. also it lies more on team rather than a system. but it happened before with me (although bugs were different , team marked it dup for some reason) .so thought of reporting it

The difference here is, you don't increase your reputation but you can increase your number of bugs!

Steps
1. The obvious pre requisite here is, you have to send valid report to any team
2. Wait for it to get triaged. once it is triaged, it is almost certain that it will be resolved!
3.Send the same report again with little modification, may be by changing the title and description
4. Now most teams will mark this as duplicate of your own report!
5. But when the original report gets resolved, your reputation remains the same but number of bugs increases by 2(one for original and one for dup).

if you keep on submitting such bugs multiple times, you can boost your number of bugs which may create false impression (which will look good to others as profiles are public)

The obvious resolution would be , not to count dup report if its dup of your own report!

Regards
Ashish

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
