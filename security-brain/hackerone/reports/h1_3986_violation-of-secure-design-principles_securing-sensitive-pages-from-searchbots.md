---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3986'
original_report_id: '3986'
title: Securing sensitive pages from SearchBots
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-03-14T10:03:32.070Z'
disclosed_at: '2014-04-20T15:13:00.462Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# Securing sensitive pages from SearchBots

## Metadata

- HackerOne Report ID: 3986
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-04-20T15:13:00.462Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I reported the issue earlier (Report #3662) .But instead of asking more information,you just closed the bug.Well,you said you never seen google indexing authentication tokens.
okCupid,is a client of hackerone.com.Let's see whats google doing with their tokens:

Search with the following dork:
site:www.okcupid.com/settings?userid_token=
And see the results cache.Can you see,both users email address and tokens are being indexed by search engines?
This is what going to happen with hackerone too.As those pages does not have noindex,nofollow tags.

Ok,lets show you another example.A cached page of Facebook Support Centre.

http://webcache.googleusercontent.com/search?q=cache:ikhWiVtVF50J:www.facebook.com/support/case%3Feid%3DAREP3f8aORMfZcbVfPE9BKUgbk0dNVASVI2RkPSYyIyyxwpoS5a8pQwEuEGItQSTgfg_knkrsm6UMRAiXk2_JrLw-XhkBlDoNipvIpL8QSONNA+&cd=1&hl=en&ct=clnk&gl=in

Go to the address.Notice whats written on the search box,just right side of the facebook logo.

"Hi Samrita, What do you need help with?"
Now,can you answer me,how the hell is google indexing such a page,which requires users authentication.Yah! You are right.Google is indexing browsers cache for search results.After I reported the bug to facebook,they added noindex and nofollow tags to all sensitive pages.
And yet you are telling its not a bug ?
Well may luck help you and your secret reports.

Thanks

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
