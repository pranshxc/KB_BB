---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125503'
original_report_id: '125503'
title: Stored Cross Site Scripting [SELF] in partners.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-23T19:31:10.385Z'
disclosed_at: '2016-06-13T22:00:42.988Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored Cross Site Scripting [SELF] in partners.uber.com

## Metadata

- HackerOne Report ID: 125503
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-06-13T22:00:42.988Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey Uber Team, 

although you are excluding self stored XSS i am reporting this one because it could be exploited by someone with more skills then i have :-) :

1. Login to your profile and change the address to : “#><img src=x onerror=prompt(1);>
2. Go to https://partners.uber.com/fuel_cards/enroll 
3. The JS will pop up 

best

Patrik

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
