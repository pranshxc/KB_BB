---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '52042'
original_report_id: '52042'
title: HTTP Response Splitting (CRLF injection) in report_story
team_handle: x
created_at: '2015-03-15T07:49:31.208Z'
disclosed_at: '2015-04-21T17:59:23.057Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
tags:
- hackerone
---

# HTTP Response Splitting (CRLF injection) in report_story

## Metadata

- HackerOne Report ID: 52042
- Weakness: 
- Program: x
- Disclosed At: 2015-04-21T17:59:23.057Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I would like to report a HTTP Response Splitting vulnerability in https://twitter.com/i/safety/report_story that allows attackers to inject arbitrary headers and contents in the response. 

## PoC:
https://twitter.com/i/safety/report_story?next_view=report_story_start&source=reporttweet&reported_user_id=1&reporter_user_id=1&is_media=true&is_promoted=true&reported_tweet_id=%E5%98%8A%E5%98%8DSet-Cookie:%20test

## Details:
The page will set cookie for the parameter *reported_tweet_id*. However, it doesn't validate strictly if it is a number. Although there is a protection against CRLF injection by detecting the presence of any *NewLine* character (0x0a), it can be bypassed with characters encoded in UTF-8 as the the page will try to convert them back to the original Unicode form and extract the last byte. For example, *%E5%98%8A* => *U+560A* => *0A*.

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
