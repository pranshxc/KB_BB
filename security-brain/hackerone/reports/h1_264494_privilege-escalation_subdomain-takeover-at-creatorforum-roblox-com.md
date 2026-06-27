---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264494'
original_report_id: '264494'
title: Subdomain Takeover at creatorforum.roblox.com
weakness: Privilege Escalation
team_handle: roblox
created_at: '2017-08-30T01:51:35.882Z'
disclosed_at: '2020-03-24T19:57:37.210Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 83
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover at creatorforum.roblox.com

## Metadata

- HackerOne Report ID: 264494
- Weakness: Privilege Escalation
- Program: roblox
- Disclosed At: 2020-03-24T19:57:37.210Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello.

A few days ago, I was looking at Roblox subdomains, and I noticed an unusual one called creatorforum.roblox.com. Upon further investigation, I visited it and saw that creatorforum.roblox.com's CNAME was a nonexistant Discourse website.
 I immediately reported to info@roblox.com, and eventually talked to Antek Baranski on the bugbounty@roblox.com email address. The issue has been fixed since reporting, but I was told to send a report here.

If I had a Discourse account, I could've taken over the CNAME for creatorforum.roblox.com and then it would've been a full subdomain takeover on that subdomain.

As mentioned earlier in the report, the issue has been resolved and as you can see the subdomain creatorforum.roblox.com no longer exists.


Thanks,
Jack

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
