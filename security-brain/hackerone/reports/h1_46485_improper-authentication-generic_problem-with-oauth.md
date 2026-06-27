---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46485'
original_report_id: '46485'
title: Problem with OAuth
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-02-04T19:03:25.578Z'
disclosed_at: '2015-11-14T16:50:09.783Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Problem with OAuth

## Metadata

- HackerOne Report ID: 46485
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-11-14T16:50:09.783Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There are many website that tracks the unfollowers and all like:
http://unfollowerstats.com
[Steps]:
1. Login with ur twitter account, i.e. abcd@mail.com
2. Open http://unfollowerstats.com, This will ask you to login with twitter:
3. you will get a link like this:
https://api.twitter.com/oauth/authenticate?oauth_token=xpXP21WOzwvsocu7yjQBafl8BKRtKdeH

4.
Open Another browser and login with some other user i.e. : xyz@mail.com
5.
Open this  oAuth link(https://api.twitter.com/oauth/authenticate?oauth_token=xpXP21WOzwvsocu7yjQBafl8BKRtKdeH) on the other browser
6. 
Authorize this OAuth with user xyz@mail.com

7. Go to the first browser, and refresh the page and continue to authorize. You will be logged into http://unfollowerstats.com with xyz@mail.com user


-- Tested with 2 such websites

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
