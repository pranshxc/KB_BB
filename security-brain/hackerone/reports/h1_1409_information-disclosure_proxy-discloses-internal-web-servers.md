---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1409'
original_report_id: '1409'
title: Proxy discloses internal web servers
weakness: Information Disclosure
team_handle: factlink
created_at: '2014-02-13T20:05:27.920Z'
disclosed_at: '2014-04-08T08:37:00.766Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Proxy discloses internal web servers

## Metadata

- HackerOne Report ID: 1409
- Weakness: Information Disclosure
- Program: factlink
- Disclosed At: 2014-04-08T08:37:00.766Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

I found a bug that allows users of your proxy to retrieve pages from your internal web servers -- in this case, the `172.16.64.0/24` subnet. As an example, please see [this link](http://fct.li/?url=https://172.18.64.13). As you will see, it returns the HTML of your Chef server (which, I assume, cannot be accessed from the internet). I wasn't able to access any of your systems. That being said, I didn't really spent time on it.

Please note that once your proxy is also able to follow redirects, it should reject redirects to internal hosts as well.

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
