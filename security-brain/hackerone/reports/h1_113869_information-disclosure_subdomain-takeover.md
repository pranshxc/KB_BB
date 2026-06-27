---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113869'
original_report_id: '113869'
title: Subdomain Takeover
weakness: Information Disclosure
team_handle: zomato
created_at: '2016-02-01T14:15:54.625Z'
disclosed_at: '2016-03-09T10:57:00.599Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Subdomain Takeover

## Metadata

- HackerOne Report ID: 113869
- Weakness: Information Disclosure
- Program: zomato
- Disclosed At: 2016-03-09T10:57:00.599Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Your Subdomain engineering.zomato.com is Pointing to Tumblr.com


You should immediately remove the DNS-entry for engineering.zomato.com is Pointing to Tumblr.com.. Any One Can Claim That Domain , Please Read The Advisory Below.

Remediation
Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

I Have Done NSLookup For POC :-

nslookup engineering.zomato.com
Server:		192.168.188.2
Address:	192.168.188.2#53

Non-authoritative answer:
engineering.zomato.com	canonical name = domains.tumblr.com.
Name:	domains.tumblr.com
Address: 66.6.42.22
Name:	domains.tumblr.com
Address: 66.6.43.22


Thanks!

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
