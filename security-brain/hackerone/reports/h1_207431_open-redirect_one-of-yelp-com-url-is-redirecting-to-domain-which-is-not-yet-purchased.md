---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '207431'
original_report_id: '207431'
title: One of yelp.com url is redirecting to domain which is not yet purchased
weakness: Open Redirect
team_handle: yelp
created_at: '2017-02-19T03:01:25.479Z'
disclosed_at: '2017-11-09T20:00:28.164Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- open-redirect
---

# One of yelp.com url is redirecting to domain which is not yet purchased

## Metadata

- HackerOne Report ID: 207431
- Weakness: Open Redirect
- Program: yelp
- Disclosed At: 2017-11-09T20:00:28.164Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

One of yelp.com url is redirecting to domain which is not yet purchased, so anyone would buy that domain and host any stuff which yelp.com does not support.

A malicious user can take advantage of this and send the link to users, and people will it is secured domain as link originates from yelp.com which runs on https.

Real Proof:
https://www.yelp.com/biz_redir?url=http%3A%2F%2Fwww.taj-tandoorrestaurant.com%2F&src_bizid=ZOdW1uEoRbaA0JFU4alHIg&cachebuster=1455812254&s=05ce6972e019a426a5447be0258b8f6aa981ff1b340d76f61daaa763f4752691

I also found the behavior of above url weird.

I would like you to follow below steps

1.Copy above url and paste it in firefox browser
2.Refer screenshot 1 (it will show you are getting redirected to www.taj-tandoorrestaurant.com but once the page loads it shows www1.taj-tandoorrestaurant.com (refer screenshot 2).
3.Again paste the same url in same browser 2nd time it opens some other domains like 
http://go.offersprizes.win/?utm_term=6387662821350405046&clickverify=1&utm_content=fdc2c69a9cafac9c919596a191959ca583bbcdb9cbbfbc8c818586b1808283b5a7b8bbb98ebebd8db0b3b1b6b6b6b6b0aaa2aca8adae9cac92939091a79794a7deebdaddeeefec99909685e1e6d63d#
www.indiannews.com-secure.org

Please look into this thanks.

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
