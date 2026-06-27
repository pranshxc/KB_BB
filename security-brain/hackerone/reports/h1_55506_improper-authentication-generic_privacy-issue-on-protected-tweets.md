---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55506'
original_report_id: '55506'
title: Privacy Issue on protected tweets
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-04-09T17:04:37.854Z'
disclosed_at: '2015-05-14T11:22:43.875Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Privacy Issue on protected tweets

## Metadata

- HackerOne Report ID: 55506
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-05-14T11:22:43.875Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Twitter Security Team, 

###Problem:
Here is a privacy issue that break your privacy for protected tweets.

###Details:
I have two accounts on twitter @dia2diab and @Dia2diabTest , from the first one i changed the settings of Tweet privacy to be "Protect my Tweets" and now if you access one of my tweets like this one here twitter.com/dia2diab/status/585987812643708928 Or here mobile.twitter.com/dia2diab/status/585987812643708928 from a private window you will find that "@dia2diab's Tweets are protected.". great !!

Now, i don't wanna @Dia2diabTest to see anything from my tweets, so i decided to block him, i think now this user can't see my tweets by anyway [i blocked him & i made my tweets private].

The amazing thing when i access this url mobile.twitter.com/dia2diab/status/585987812643708928 with my logged in session with the second user i found that i can see the tweet.

This is break your privacy rules there support.twitter.com/articles/14016

###Fixing:
You must need to protect your users privacy.

@dia2diab

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
