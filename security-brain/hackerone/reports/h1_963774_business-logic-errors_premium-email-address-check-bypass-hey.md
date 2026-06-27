---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '963774'
original_report_id: '963774'
title: Premium Email Address Check Bypass - Hey
weakness: Business Logic Errors
team_handle: basecamp
created_at: '2020-08-20T20:24:01.818Z'
disclosed_at: '2020-12-15T15:21:37.941Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: '*.basecamphq.com'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- business-logic-errors
---

# Premium Email Address Check Bypass - Hey

## Metadata

- HackerOne Report ID: 963774
- Weakness: Business Logic Errors
- Program: basecamp
- Disclosed At: 2020-12-15T15:21:37.941Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello, I reported a bug to support@hey.com a couple weeks ago, not realizing that I was a member of the private bug bounty program. It was fixed quickly (Less than 1 hour) which was awesome to see. Being that this was reported through a seperate channel, and it is for Hey, I'm not even sure it would eligible here. Either way, it was a pretty neat bug becuase of its simplicity and clear impact (loss of revenue). 

Anyways, here it is:

There appears to be a bypass for the premium email address sign up. 

When signing up for Hey, I tried to obtain jp@hey.com, which prompted a Premium alert box that stated it would cost $999 per year. Since that wouldn't work for me, I tried 'jp  @hey.com' (two spaces), this worked without prompting me to accept that it was a premium email address. 

It appears that the spaces are registered as characters, so it's not considered a premium domain (at 4 chars), but the spaces are stripped at a later step and I am given a two character premium email address for the same cost as a non-premium email address.

Now, it appears I can lock this email address in for $99 per year just like a typical email address on the Hey platform.

## Impact

At the time, the impact was that an premium account (less than 4 chars) could be registered for the non-premium price of $99, which is substantially cheaper than the $999 price tag.

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
