---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '180538'
original_report_id: '180538'
title: X.509 certificate validation fails on international vanity domains
weakness: Violation of Secure Design Principles
team_handle: yelp
created_at: '2016-11-06T20:31:40.455Z'
disclosed_at: '2017-02-06T22:49:20.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# X.509 certificate validation fails on international vanity domains

## Metadata

- HackerOne Report ID: 180538
- Weakness: Violation of Secure Design Principles
- Program: yelp
- Disclosed At: 2017-02-06T22:49:20.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This is not an vulnerability, more likely TLS/SSL related configuration issue with certificates noticed during bug bounty testing.

If you try to access any Finnish domain (such as my HackerOne test-profile http://tomitest.yelp.fi/), there will be an certificate related error presented to user. You can try with any other Finn URL's and you'll notice this affects all other too.

Most probably users are not able to access Finnish Yelp domain pages without some extra hassle/confusion. Basically *.com* works fine, but *.fi* doesn't. Anyways, since Yelp provides *.fi* domain if you're are an Finn (like me), I assume both should work for user profiles.

I've added two screenshots to aid this finding:
1. Certificate error presented by Google Chrome.
2. Link from my testpage (Yelp's localized profile page address via get your own url)

Cheers,
-Tomi

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
