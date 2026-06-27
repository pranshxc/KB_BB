---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '249234'
original_report_id: '249234'
title: Posting to Twitter CSRF on php/post_twitter_authenticate.php
weakness: Cross-Site Request Forgery (CSRF)
team_handle: zomato
created_at: '2017-07-13T11:58:49.259Z'
disclosed_at: '2017-08-19T08:17:00.859Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Posting to Twitter CSRF on php/post_twitter_authenticate.php

## Metadata

- HackerOne Report ID: 249234
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: zomato
- Disclosed At: 2017-08-19T08:17:00.859Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi !

This time, i found a CSRF who can lead to arbitrary writing on twitter account of victim if they have added it to zomato :)

Coupled with a stored XSS, it could be very troublesome to you.

In the page, it seems there is no token check at all.

You can see in the video the CSRF working and here is the POC i used:

`https://www.zomato.com/php/post_twitter_authenticate.php?type=posttweet&message=Hello Zomato Team :)`

Cordially,

Kuromatae.

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
