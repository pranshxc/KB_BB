---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1036995'
original_report_id: '1036995'
title: HTML injection in review content
weakness: Command Injection - Generic
team_handle: judgeme
created_at: '2020-11-17T19:30:39.849Z'
disclosed_at: '2021-12-17T17:44:06.122Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# HTML injection in review content

## Metadata

- HackerOne Report ID: 1036995
- Weakness: Command Injection - Generic
- Program: judgeme
- Disclosed At: 2021-12-17T17:44:06.122Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Judge Security Team, 

I found a HTML Injection in review parameter at the https://judgeme-pentest.myshopify.com/products/pentest and at the judge.me

###Steps

1. Go to https://judgeme-pentest.myshopify.com/products/pentest
2. Click on "Write Review"
3. fill in the fields normally. 

{F1083621}

4.  Now, go to your profile review in the judge.me
5. Edit your Review
6. In Review body, enter this payload: ``` <a href=https://google.com/>CLICK HERE</a>```
7. Save and go to  https://judgeme-pentest.myshopify.com/products/pentest 

{F1083622}

8. Boyaah. 

{F1083623}

## Impact

the attacker can insert HTML codes on the page

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
