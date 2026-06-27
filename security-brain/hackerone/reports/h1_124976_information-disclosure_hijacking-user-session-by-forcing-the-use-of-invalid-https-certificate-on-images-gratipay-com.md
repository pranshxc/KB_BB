---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124976'
original_report_id: '124976'
title: Hijacking user session by forcing the use of  invalid HTTPs Certificate on
  images.gratipay.com
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-03-22T15:29:48.050Z'
disclosed_at: '2016-04-01T16:34:06.349Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Hijacking user session by forcing the use of  invalid HTTPs Certificate on images.gratipay.com

## Metadata

- HackerOne Report ID: 124976
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-04-01T16:34:06.349Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found that the domain images.gratipay.com is just a reverse proxy for gratipay.com and **HTTPS** works throughtout the site flawlessly except in one case, that it when we try to open user's profile:

POC: https://images.gratipay.com/~asdlfz/

Https Warning Page: http://i.imgur.com/XHsXJEvr.png?1


**Risks**

Any user browsing the page is under direct man-in-middle attack, as Https is being not implemented properly, The session data can be easily decrepted via any end point.

For new user's it might result like first impression of the site is an invalid https certificate and plus the warning Chrome gives is way more horrifying:

>Attackers might be trying to steal your information from images.gratipay.com (for example, passwords, messages, or credit cards).

The user might never dare to open even gratipay.com ever.


**Fix**
Add a valid Certificate across `images.gratipay.com` or remove the domain at all.

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
