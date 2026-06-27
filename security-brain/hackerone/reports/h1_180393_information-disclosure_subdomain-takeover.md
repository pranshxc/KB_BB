---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '180393'
original_report_id: '180393'
title: Subdomain Takeover
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-11-05T16:41:06.898Z'
disclosed_at: '2017-05-05T06:03:15.111Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 75
tags:
- hackerone
- information-disclosure
---

# Subdomain Takeover

## Metadata

- HackerOne Report ID: 180393
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2017-05-05T06:03:15.111Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello,

Your Subdomain engineering.github.com/paragonie is Pointing to Tumblr.com

You should immediately remove the DNS-entry for engineering.zomato.com is Pointing to Tumblr.com.. Any One Can Claim That Domain , Please Read The Advisory Below.

Remediation
Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

I Have Done NSLookup For POC :-

nslookup github.com/paragonie
Server: 192.168.188.1
Address: 192.168.188.2#53

Non-authoritative answer:
engineering.zomato.com canonical name = domains.tumblr.com.
Name: domains.tumblr.com
Address: 66.6.42.22
Name: domains.tumblr.com
Address: 66.6.43.22

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
