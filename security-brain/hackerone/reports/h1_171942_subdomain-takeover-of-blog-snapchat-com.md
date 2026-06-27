---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '171942'
original_report_id: '171942'
title: Subdomain takeover of blog.snapchat.com
team_handle: snapchat
created_at: '2016-09-25T20:08:34.689Z'
disclosed_at: '2016-10-05T18:41:02.256Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
---

# Subdomain takeover of blog.snapchat.com

## Metadata

- HackerOne Report ID: 171942
- Weakness: 
- Program: snapchat
- Disclosed At: 2016-10-05T18:41:02.256Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Overview
The ANAME for blog.snapchat.com, which redirects to snapchat-blog.com, was pointing to tumblr for Snapchat's blog.  This blog had been expired or had removed the CNAME claim.  Adding "snapchat-blog.com" to the custom domain setting on tumblr allowed takeover of this subdomain.

#Repro Steps
1) Visit http://blog.snapchat.com
Result: Blog registered by my account "jreynoldsdev" displays title "Hello Snapchat - Jake Reynolds"

#Suggested Fixes
The best fix would be for Snapchat's tumblr blog to reclaim this CNAME.  For resolution contact me and we can coordinate switching the domain name back under your control.

If you have any further questions please feel free to reach out.

Thanks,
Jake

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
