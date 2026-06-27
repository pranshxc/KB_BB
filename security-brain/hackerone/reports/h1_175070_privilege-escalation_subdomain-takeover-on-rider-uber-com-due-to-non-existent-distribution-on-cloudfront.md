---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175070'
original_report_id: '175070'
title: Subdomain takeover on rider.uber.com due to non-existent distribution on Cloudfront
weakness: Privilege Escalation
team_handle: uber
created_at: '2016-10-11T05:28:13.120Z'
disclosed_at: '2016-12-12T23:48:13.024Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover on rider.uber.com due to non-existent distribution on Cloudfront

## Metadata

- HackerOne Report ID: 175070
- Weakness: Privilege Escalation
- Program: uber
- Disclosed At: 2016-12-12T23:48:13.024Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

3 hours ago, rider.uber.com was responding like this:
{F127137}

This happened on both HTTP and HTTPS. Now, as our blog post from last week says:
https://labs.detectify.com/2016/10/05/the-story-of-ev-ssl-aws-and-trailing-dot-domains/

This means that there's a high chance this domain does not have any distribution at all, and that anyone can now claim it.

I've done this as a PoC now, I haven't placed anything on the apex level, howevel if you use this URL:
http://rider.uber.com/login-poc

There's a PoC there:
{F127139}

You should immediately remove the DNS RR, or point it elsewhere, or tell me and I'll remove the Alternate CNAME again on my PoC-distribution.

Regards,
Frans

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
