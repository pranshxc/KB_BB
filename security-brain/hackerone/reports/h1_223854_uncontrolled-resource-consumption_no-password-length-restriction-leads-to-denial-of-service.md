---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223854'
original_report_id: '223854'
title: No Password Length Restriction leads to Denial of Service
weakness: Uncontrolled Resource Consumption
team_handle: weblate
created_at: '2017-04-25T18:04:39.122Z'
disclosed_at: '2017-05-17T14:08:18.279Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# No Password Length Restriction leads to Denial of Service

## Metadata

- HackerOne Report ID: 223854
- Weakness: Uncontrolled Resource Consumption
- Program: weblate
- Disclosed At: 2017-05-17T14:08:18.279Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Weblate,

I am trying to register for an account when I came across a page where the password was required to be set up. The url is https://demo.weblate.org/accounts/password where the password was to be created after one provides his or her initial details.

There is no limit to the length of the password that can be created for this site. Hence, I tried with a big payload and everytime server responded me with a 500 internal server error. But when I registered with Antara007! password, it was accepted gleefully. Password length is something that might sound quite insignificant but is quite important.

You need to decrease password length :There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for Denial Of Service attack.

Normally all sites have a password minimum to maximum length like 72 characters limit or 48 limit to prevent Denial Of Service attack. in my sql but in weblate registration page there are no limitation. Let me know if you need any more details.

I am attaching some screenshots so that it can be understood properly.

Thanks,
Dipmalya Pyne.

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
