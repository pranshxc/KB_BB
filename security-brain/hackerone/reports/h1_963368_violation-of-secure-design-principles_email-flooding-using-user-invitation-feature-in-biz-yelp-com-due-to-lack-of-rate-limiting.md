---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '963368'
original_report_id: '963368'
title: Email flooding using user invitation feature in biz.yelp.com due to lack of
  rate limiting
weakness: Violation of Secure Design Principles
team_handle: yelp
created_at: '2020-08-20T15:43:37.909Z'
disclosed_at: '2020-09-29T20:00:45.417Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: biz.yelp.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email flooding using user invitation feature in biz.yelp.com due to lack of rate limiting

## Metadata

- HackerOne Report ID: 963368
- Weakness: Violation of Secure Design Principles
- Program: yelp
- Disclosed At: 2020-09-29T20:00:45.417Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
Hello everyone,

The feature to invite users to manage your business has no rate limiting or captcha implemented. Therefore, a malicious user can use this to mail bomb any email's inbox with invitation requests. 

## Platform(s) Affected:
biz.yelp.com

## Steps To Reproduce:
This is a pretty straight forward issue, an attacker can invite users to manage the business using the following url: /settings/user_management/invite_user through a POST request. The request body consists of  csrftok=TOKEN&title=PRIVELEDGE&email=EMAIL_ADDRESS&biz_selection=LOCATIONS. The attacker can intercept the request and repeat it many times, bombarding someones inbox.

  1. Login into biz.yelp.com, and navigate to Account Settings > User management or go to https://biz.yelp.com/settings/user_management
  2. Fire up burp
  3. Click Invite user, fill email and click send invite
  4. Intercept the POST request to https://biz.yelp.com/settings/user_management/invite_user, send to intruder
  5. Send the request multiple times using intruder, the server sends 303 to redirect us back to invite page

## Supporting Material/References:
Attached screenshots below

PS. This is my first time bug hunting and my first report so go easy on me :-)

## Impact

Mass Email Flooding
Use up system resources for sending emails, possibly DoS or even DDoS

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
