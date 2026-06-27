---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134521'
original_report_id: '134521'
title: Uber for Business Allows Administrators to Change Uber Driver Ratings Due to
  Failure to Authenticate `fast-rating` Endpoint
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-04-26T01:44:28.289Z'
disclosed_at: '2016-07-26T00:36:42.942Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Uber for Business Allows Administrators to Change Uber Driver Ratings Due to Failure to Authenticate `fast-rating` Endpoint

## Metadata

- HackerOne Report ID: 134521
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:36:42.942Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

```business.uber.com``` allows administrators to request a copy of a receipt be emailed to them. This email contains a link to ```https://riders.uber.com/fast-rating`` which allows for the administrator to change the rating the user submitted for the Uber driver. 

Furthermore, the link that is supplied does not properly authenticate the user. Anyone who has the link can change the rating without logging in simply by changing the ```rating``` parameter at the end of the URL. 

Since I ultimately want to publicly disclose this without disclosing my ```trip_token``` and ```trip_uuid``` (which are contained in the link), I put the link in a text file here: [daviddworken.com/uberRating.txt](daviddworken.com/uberRating.txt). You can confirm that the user it not properly authenticated by opening the link and changing the rating yourself. 

Thanks,
David Dworken

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
