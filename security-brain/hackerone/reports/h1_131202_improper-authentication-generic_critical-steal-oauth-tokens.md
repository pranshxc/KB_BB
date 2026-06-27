---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131202'
original_report_id: '131202'
title: '[Critical] - Steal OAuth Tokens'
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2016-04-15T21:03:27.349Z'
disclosed_at: '2016-07-11T18:03:59.776Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- improper-authentication-generic
---

# [Critical] - Steal OAuth Tokens

## Metadata

- HackerOne Report ID: 131202
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2016-07-11T18:03:59.776Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This bug is caused because of the same mis-configuration as #128119. Only this time Microsoft Outlook auth is vulnerable instead of Facebook. this time I will try to be as clear as possible. after sign up of Twitter, Twitter asks users to import contacts (and it only requires on authorization) - or simply going to https://twitter.com/who_to_follow/import will do that.

I believe you have configured your oauth redirect_uri as twitter.com in your app settings. Meaning Microsoft will accept:
- http://twitter.com as valid
- http://anything.twitter.com as valid
- https://twitter.com as valid
- https://anything.twitter.com/path/?anything as valid

So the forumla of a valid redirect_uri for twitter app is http(s?)://*.twitter.com/*

Okay, so now we make an open redirect. 

https://cards.twitter.com/cards/18ce53y6aap/yyms redirects to http://test.com and qualifies to bypass http(s?)://*.twitter.com/* and we will add ```%2523``` behind it like https://cards.twitter.com/cards/18ce53y6aap/yyms%2523 for microsoft to decode and send as a Hash %2523 -> %23 -> # with our stolen access_token.

We can then obtain this token using ```location.hash``` and all the user had to do is a single click (if already authorized - lots of people have)

To make things more clear, here is *unlisted* YouTube video to demonstrate how this works: https://youtu.be/apwbVpa2r6Y (also attached)

Thanks,
Paulos

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
