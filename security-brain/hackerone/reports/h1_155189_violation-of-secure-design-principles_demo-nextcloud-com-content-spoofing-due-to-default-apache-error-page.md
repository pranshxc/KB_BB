---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155189'
original_report_id: '155189'
title: 'demo.nextcloud.com: Content spoofing due to default Apache Error Page'
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-07-29T21:45:14.614Z'
disclosed_at: '2016-09-29T19:03:00.012Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# demo.nextcloud.com: Content spoofing due to default Apache Error Page

## Metadata

- HackerOne Report ID: 155189
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-09-29T19:03:00.012Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi ,I would like to report report a text injection and a miss-configuration of the 403 page which can be used in phishing.

POC:

https://demo.nextcloud.com//this%20website%20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------%20thanks%20for%20visiting%20our%20website,becase%20we%27re%20having%20some%20problems%20we%20have%20been%20moved%20to%20this%20site%20http:/www.malicious.com%20please%20note%20that%20our%20website%20is%20no%20longer%20exist%20Fix%20:

Just use a 403 page that don't include attacker text just as hackerone do 
or just as you do in your in other not found pages.

Thanks !

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
