---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1241483'
original_report_id: '1241483'
title: Insufficient Session Expiration
weakness: Insufficient Session Expiration
team_handle: urbancompany
created_at: '2021-06-22T19:11:51.389Z'
disclosed_at: '2021-06-23T11:44:47.830Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: www.urbancompany.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Insufficient Session Expiration

## Metadata

- HackerOne Report ID: 1241483
- Weakness: Insufficient Session Expiration
- Program: urbancompany
- Disclosed At: 2021-06-23T11:44:47.830Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Name of Vulnerability:** Insufficient Session Expiration
**Areas affected:** https://www.urbancompany.com/
**User Details:** Name-Vibhushan & Number-██████
**Summary:** Insufficient Session Expiration is when a website permits an attacker to reuse old session credentials or session IDs for authorization.

**Description:** Session timeout represents the event occurring when a user does not perform any action on a website during an interval (defined by a web server). The event, on the server-side, changes the status of the user session to ‘invalid’ (ie. “not used anymore”) and instructs the webserver to destroy it (deleting all data contained in it).
## Steps To Reproduce:

(Add details for how we can reproduce the issue through manual testing only)

  1.Login to your UrbanCompany account using your mobile number with the OTP received.
  2. After login export the cookie details using a browser extension called Cookie editor.
  3. Now log out of your account and delete the cookie details from the login page.
  4. After deletion, paste the cookie details which we copied earlier and import them.
  5. Now when the page is refreshed, it automatically logs in without the user credential.


## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

I have attached the video POC for your reference.

## Impact

The attacker can reuse the same cookies to login again without the user credentials.

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
