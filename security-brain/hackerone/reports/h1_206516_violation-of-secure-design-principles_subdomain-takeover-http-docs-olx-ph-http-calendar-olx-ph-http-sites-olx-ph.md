---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '206516'
original_report_id: '206516'
title: Subdomain Takeover (http://docs.olx.ph/ , http://calendar.olx.ph/, http://sites.olx.ph/)
weakness: Violation of Secure Design Principles
team_handle: olx
created_at: '2017-02-15T03:14:35.946Z'
disclosed_at: '2017-03-03T09:44:25.633Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- violation-of-secure-design-principles
---

# Subdomain Takeover (http://docs.olx.ph/ , http://calendar.olx.ph/, http://sites.olx.ph/)

## Metadata

- HackerOne Report ID: 206516
- Weakness: Violation of Secure Design Principles
- Program: olx
- Disclosed At: 2017-03-03T09:44:25.633Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello There,

I found Sub-Domain Takeover in olx.ph , Kindly take a look sir.
These subdomains http://docs.olx.ph/ , http://calendar.olx.ph/, http://sites.olx.ph/ is pointing towards 

docs.olx.ph is an alias for ghs.googlehosted.com.
ghs.googlehosted.com has address 216.58.201.179
ghs.googlehosted.com has IPv6 address 2a00:1450:400f:803::2013

calendar.olx.ph is an alias for ghs.googlehosted.com.
ghs.googlehosted.com has address 216.58.201.179
ghs.googlehosted.com has IPv6 address 2a00:1450:400f:803::2013

sites.olx.ph is an alias for ghs.googlehosted.com.
ghs.googlehosted.com has address 216.58.201.179
ghs.googlehosted.com has IPv6 address 2a00:1450:400f:803::2013

sites.olx.ph
{F160956}
calendar.olx.ph
{F160957}
docs.olx.ph
{F160958}

And it is unclaimed, When I open it 
it is showing like this

docs.olx.ph
{F160959}
sites.olx.ph
{F160960}
calendar.olx.ph
{F160961}

Impact :
An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.

I Recommend removing the Cname and DNS connecting to it.
You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm

Regards,
kntbyrn
 
POC Video Here {F160964}

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
