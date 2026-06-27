---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56119'
original_report_id: '56119'
title: 'Privecy Issue : view "Protected users" followers and following'
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-04-13T12:03:21.545Z'
disclosed_at: '2015-05-15T20:52:30.298Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Privecy Issue : view "Protected users" followers and following

## Metadata

- HackerOne Report ID: 56119
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-05-15T20:52:30.298Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi
When Twitter user account change his privacy settings =>https://twitter.com/settings/security
and enable "Protect my Tweets " 
others users "Not in the Follow list" should Not be able to see the user's follower an following list 
but I just found out away to see any Protected users" follower an following only by visiting a link 

in this case here #53128  "which I still think you should fix it" you gave me this account  https://twitter.com/shpendktester1 and told me to view his Favorites it's a protected account 
users shouldn't be able to view his followers list or the following list 
so as the attacker I can view his following using this link 

https://twitter.com/shpendktester1/following/users?cursor_index=&cursor_offset=&include_available_features=1&include_entities=1&is_forward=true

notice that account user name in the link 
when you visit the link a file  named json.json well be downloaded view the file and ctrl+f lookup for  "data-screen-name"
so this user following these two accounts 
@shpendktester
@NicoleScherzy

to view his followers edit the link to : 

https://twitter.com/shpendktester1/followers/users?cursor_index=&cursor_offset=&include_available_features=1&include_entities=1&is_forward=true

when you visit the link a file  named json.json well be downloaded view the file and ctrl+f lookup for  "data-screen-name"
so this user followers  these three accounts 
@shpendk
@shpendktester
@lovely_loucks

thanks ,,

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
