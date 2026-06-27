---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1241116'
original_report_id: '1241116'
title: hardcoded api secret & api key in com.reddit.frontpage
weakness: Improper Authentication - Generic
team_handle: reddit
created_at: '2021-06-22T12:54:48.455Z'
disclosed_at: '2021-10-21T19:47:40.687Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: com.reddit.frontpage
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# hardcoded api secret & api key in com.reddit.frontpage

## Metadata

- HackerOne Report ID: 1241116
- Weakness: Improper Authentication - Generic
- Program: reddit
- Disclosed At: 2021-10-21T19:47:40.687Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi security team,
in file Resources/Resources.arsc/res/values/strings.xml
i have found
<string name="twitter_consumer_key">███</string>
<string name="twitter_consumer_secret">███</string>

It shouldn't be disclosed to third parties it meant for deveoplers as per https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens

poc:-
curl --user "██████:███"  --data 'grant_type=client_credentials' 'https://api.twitter.
com/oauth2/token'

response:-
{"token_type":"bearer","access_token":"████"}

it meant to request successful as official docs say https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens

## Impact

leakage of twitter_consumer_key and twitter_consumer_secret to public it meant for deveoplers only

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
