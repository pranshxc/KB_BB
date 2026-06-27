---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6017'
original_report_id: '6017'
title: Facebook Takeover using Slack using 302 from files.slack.com with access_token
weakness: Open Redirect
team_handle: slack
created_at: '2014-04-06T07:24:52.591Z'
disclosed_at: '2015-01-11T15:25:45.229Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- open-redirect
---

# Facebook Takeover using Slack using 302 from files.slack.com with access_token

## Metadata

- HackerOne Report ID: 6017
- Weakness: Open Redirect
- Program: slack
- Disclosed At: 2015-01-11T15:25:45.229Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I noticed that your Facebook application used in the "Import Photo" can be used to take over the Facebook account of the user being attacked.

It's multiple issues in one:
1. You have a 302 redirect from a *.slack.com domain. Hash-values will follow the redirect.
2. The Facebook application OAuth settings are too weak, and a files.slack.com-URL will be accepted as the redirect_uri. You should restrict these to a www.slack.com that then redirects to the subdomain, instead of allowing all *.slack.com-subdomains, or deny the files.slack.com as a OAuth redirect-subdomain.

So, the following URL will redirect the user to files.slack.com after authentication of the app (or if the user already has it approved, no client interaction is needed):

https://www.facebook.com/dialog/oauth?client_id=569627156411038&redirect_uri=https%3A%2F%2Ffiles.slack.com%2Ffiles-pri%2FT025M9QPZ-F0283NJ20%2Fhash.swf&response_type=token&scope=user_photos&sdk=joey

I have attached POC-images showing what happens and what the Token provides as it is today (you can modify the scope, the user needs to approve it, but it still looks legit coming from Slack).

Regards,
Frans

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
