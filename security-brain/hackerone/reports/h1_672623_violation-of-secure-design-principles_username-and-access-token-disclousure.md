---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '672623'
original_report_id: '672623'
title: Username and Access Token Disclousure
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2019-08-13T19:37:00.040Z'
disclosed_at: '2020-03-01T11:22:19.644Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: it.twsweb.Nextcloud
asset_type: APPLE_STORE_APP_ID
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# Username and Access Token Disclousure

## Metadata

- HackerOne Report ID: 672623
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2020-03-01T11:22:19.644Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Versions
=====================
Nextcloud Server Version: 16.0.3.0
it.tsweb.Nextcloud (iOS App) Version: 2.23.7

Description
=====================
While logging in to an owncloud instance the iOS client sends the Username and password to the ressource
`/login?redirect_url=/login/flow/grant`
and recieves an token by the ressource /login/flow in the process. This happens in the form of an HTTP 303 redierect Location [Picture 1].
`/login/flow/grant?clientIdentifier=&stateToken=ji76VUQooqEHFwIPyUUHkAqGaazB8XJ5DHQiJK6vk5aBLfhS1XMf2flTMPVxgFm3`

This Token is from now on used to authenticate every request made by the App to the owncloud instance [Picture 4].
This happens in the form of an Basic-Authentication header, where username and password are encodet in an Base-64 String [Picture 3].

Additionally the iOS client automaticaly registers some user specific parameters at `push-notifications.nextcloud.com` without notifying the user. While this process the client also sends the Basic-Authentication header of the owncloud instance to the third Party server [Picture 2].

## Impact

This leads to an massive user information disclousure which affects all iOS users of the nextcloud App (i have not tested Android) to the third party `push-notifications.nextcloud.com`.
The owner of the domain and the operator of the server recieve a high ammount of valid Usernames an access tokens of every owncloud instance with iOS users.

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
