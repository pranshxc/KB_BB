---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1114347'
original_report_id: '1114347'
title: Account takeover due to misconfiguration
weakness: Use of a Key Past its Expiration Date
team_handle: mattermost
created_at: '2021-03-02T05:46:13.703Z'
disclosed_at: '2021-09-17T05:19:55.583Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 116
asset_identifier: mattermost/mattermost-server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-a-key-past-its-expiration-date
---

# Account takeover due to misconfiguration

## Metadata

- HackerOne Report ID: 1114347
- Weakness: Use of a Key Past its Expiration Date
- Program: mattermost
- Disclosed At: 2021-09-17T05:19:55.583Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

HI team, i hope you are good :)

Its a very simple logical flaw that results in this

So suppose we are victim@gmail.com , now login into the website then

1. go to account settings and then change mail address to victim111@gmail.com
2. a link will be sent to victim111@gmail.com, now the user realizes that he have lost access to victim111@gmail.com due to some reasons 
3. so he will probably change mail to the another mail address for e.g victim999@gmail.com which he owns and has access to
4. but it is found that even after verifying victim999@gmail.com, the old link which was sent to victim111@gmail.com is active, so user/attacker having access to that mail can verify it and takeover acc


In a nutshell : 

It is mandatory for a web app to invalidate the tokens in time to secure its user 

In this case, suppose while changing mail address the user mistakenly typed wrong mail address, so the link will be sent to that mail address. 

So the user probably don't want the user of that mail address to verify it, so he will quickly change his mail address to one he owns and verify it

what he doesn't know is that even after verification(change of major state), the old link is still active 

the flaw :

user changes mail to attacker@gmail.com -> user realizes that he mistyped the mail -> so he again changes to mail he owns and verifies it -> old link sent to attacker@gmail.com is still active even after new mail has been verified

## Impact

An attacker can takeover acc due to misconfiguration, not invalidation of tokens at major state change, in time

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
