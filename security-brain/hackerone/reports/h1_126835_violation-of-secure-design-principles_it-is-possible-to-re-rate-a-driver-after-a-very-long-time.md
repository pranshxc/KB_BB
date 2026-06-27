---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126835'
original_report_id: '126835'
title: It is possible to re-rate a driver after a very long time
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-03-30T04:31:32.429Z'
disclosed_at: '2016-04-25T17:19:37.868Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# It is possible to re-rate a driver after a very long time

## Metadata

- HackerOne Report ID: 126835
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-04-25T17:19:37.868Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi

It is not possible to edit your rating but there is a way to bypass that restriction 


Steps:

1- login to your uber account https://riders.uber.com

2- View your trips https://riders.uber.com/trips

3- choose one of your trips 

4- click on resend 

5- check your email

6- you will find a button in email to rate your driver

7- rate it to 4 or 3 (something different than the original rating)

8- you will get a message indicating that you successfully changed it

9- go back to https://riders.uber.com/trips

10- your find that rating changed or may be not changed 

11- you will need to click on filter trips and choose filter by credit card or city

12- you will find that your rating is changed.


Note: I tested it on a previous trip since 2015 and i rated the driver 5 stars but i changed it to 4 starts in 2016

here is the tripe:  https://riders.uber.com/trips/2801e5cc-e798-485d-9ca6-d47e8c107568

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
