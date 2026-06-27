---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105887'
original_report_id: '105887'
title: Know whether private program for company exist or not
weakness: Information Disclosure
team_handle: security
created_at: '2015-12-18T07:14:51.928Z'
disclosed_at: '2016-01-15T15:40:58.692Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- information-disclosure
---

# Know whether private program for company exist or not

## Metadata

- HackerOne Report ID: 105887
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-01-15T15:40:58.692Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI,

There are some company which are hosting private BB on HackerOne which are not visible unless they invite you. However, you can check if any company is hosting private BB on HackerOne or not if you can guess the username they use.

Generally most company chooses the same name as their company name like yahoo.

Now for eg, &#x2588;&#x2588;&#x2588;&#x2588; hosts such private program on HackerOne. But if someone had to find out if they hosts such program on HackerOne, they just need to browse to 

https://hackerone.com/<redacted>/thanks.json

Now since company name is &#x2588;&#x2588;&#x2588;&#x2588;, a user can easily guess that, username would be same.

The problem with above url is, it will display blank screen for a user. But this is indication that the program is exist on HackerOne which is private.
If the username is not valid for eg I will change the name to &#x2588;&#x2588;&#x2588;&#x2588;
 https://hackerone.com/<redacted>/thanks.json

It will display me page not found error.

So this indicates that, such program doesnt exist.

So the conclusion is

Blank screen- program exist privately
page not found error- program doesnt exists

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
