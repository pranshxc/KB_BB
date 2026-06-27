---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142569'
original_report_id: '142569'
title: 'Infinite Upvoting/Downvoting: Lockout Bypass, Plus: Exposed API Documentation'
team_handle: urbandictionary
created_at: '2016-06-01T21:47:50.034Z'
disclosed_at: '2016-07-24T17:50:31.521Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
---

# Infinite Upvoting/Downvoting: Lockout Bypass, Plus: Exposed API Documentation

## Metadata

- HackerOne Report ID: 142569
- Weakness: 
- Program: urbandictionary
- Disclosed At: 2016-07-24T17:50:31.521Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By sending an extra parameter (kind=1) in the upvote/downvote API request, a user can vote as many times as he wants without any IP address restriction:

http://api.urbandictionary.com/v0/vote?kind=1&direction=up&defid=94413

Seems harmless enough, but your site does depend on the accuracy of the definitions. So it could be a real problem if this was discovered by a bad hacker who wanted to cause harm to your site. He could write a program to systematically bring bad definitions or spam to the top of every word result.

This strange extra parameter was discovered because your Swagger API documentation is publicly accessible here: http://api.urbandictionary.com/docs/index.html

So I would also recommend hiding that. 

I didn't find anything else too bad about your API, just some neat things like:
http://api.urbandictionary.com/v0/words_of_the_day?per_page=90000000&page=1&api_key=ab71d33b15d36506acf1e379b0ed07ee

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
