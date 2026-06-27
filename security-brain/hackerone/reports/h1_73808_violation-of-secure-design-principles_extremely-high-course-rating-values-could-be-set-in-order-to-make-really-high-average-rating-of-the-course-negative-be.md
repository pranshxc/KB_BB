---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73808'
original_report_id: '73808'
title: Extremely high Course rating values could be set in order to make really high
  Average rating of the course. Negative values could be set to.
weakness: Violation of Secure Design Principles
team_handle: udemy
created_at: '2015-07-03T20:54:19.628Z'
disclosed_at: '2015-09-25T22:34:52.583Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Extremely high Course rating values could be set in order to make really high Average rating of the course. Negative values could be set to.

## Metadata

- HackerOne Report ID: 73808
- Weakness: Violation of Secure Design Principles
- Program: udemy
- Disclosed At: 2015-09-25T22:34:52.583Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Authenticated user can register for some course (paid or free). After registering and taking couple of lectures "Rate course" functional becomes active.  

Malicious user can fill the rating form and submit it. By intercepting request to the server's API (by using intercepting proxy tool) and modify rating value he can set enormously large values as rating. After experimenting following restrictions was found:
1) 2147483647   <-- Maximum rating value
2) -2147483648  <-- Minimal rating value

Example of setting such rating could be found on the SCREEN: Set_rating_1.jpg

After some time that rating will affect correct calculation of course's average rating:
PROF SCREEN: Result_of_wrong_rating_2.png

This issue could be used by attacker in order to trick user to buy bad quality content. 

p.s. In order to remove wrong rating value i've already deleted my review. Here is PROF SCREEN:
Delete_rating_3.jpg

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
