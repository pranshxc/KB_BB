---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '452973'
original_report_id: '452973'
title: Inline banner on Report page discloses whether organization runs a private
  program
weakness: Information Disclosure
team_handle: security
created_at: '2018-11-30T05:05:57.286Z'
disclosed_at: '2018-12-11T17:54:36.757Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
tags:
- hackerone
- information-disclosure
---

# Inline banner on Report page discloses whether organization runs a private program

## Metadata

- HackerOne Report ID: 452973
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-12-11T17:54:36.757Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team , @jobert
**Description:**

Your engineers have created inscription - `You are participating in a private program for ████████. Please do not publicly discuss the program until the program goes public.`

When a hacker creates a report in an external program with a private page, we will see this inscription, which makes it clear that the program has a private part.

When a hacker creates a report in an external program that does not have a private page , we will not see this inscription.

It's more of a logical mistake. To fix this, I think you need to give the inscription in all reports for all programmes
### Steps To Reproduce

1. Create publish report for any programs

2. If we are created report for ████████ , ██████████ , ... We will see the inscription -
`You are participating in a private program for`***name_program***`. Please do not publicly discuss the program until the program goes public.` Because they have a private part

█████████

3. if we are creted report for ████, ... We won't see the inscription . Because they have not a private part

██████████

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

disclosure of external programs with private

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
