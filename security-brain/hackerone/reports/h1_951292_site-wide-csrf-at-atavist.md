---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '951292'
original_report_id: '951292'
title: Site-wide CSRF at Atavist
team_handle: automattic
created_at: '2020-08-04T22:54:00.096Z'
disclosed_at: '2020-11-18T14:21:01.478Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
---

# Site-wide CSRF at Atavist

## Metadata

- HackerOne Report ID: 951292
- Weakness: 
- Program: automattic
- Disclosed At: 2020-11-18T14:21:01.478Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
I have a Atavist Magazine account. And there are no CSRF tokens on account settings.

For example ;
- When changing email (there is a user ID but they are sequential) : {F936597}

- Deleting credit card : {F936618}

- Cancelling subscription : https://magazine.atavist.com/cms/ajax/cancel_subscription.php?product_id=com.theatavist.atavist.subscription.membership - this endpoint sends an email with `We'll Miss You` title, but it doesn't cancel the subscription. (this is not related to CSRF, there is a CSRF but the endpoint is weird :-D)

I didn't want to create report for each endpoint, because this is a site-wide issue. I think you can add a header for root fix.

## Impact

Site-wide CSRF 

Thanks,
Bugra

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
