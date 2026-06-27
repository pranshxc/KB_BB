---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49663'
original_report_id: '49663'
title: URGENT - Subdomain Takeover on status.vimeo.com due to unclaimed domain pointing
  to statuspage.io
weakness: Cross-Site Request Forgery (CSRF)
team_handle: vimeo
created_at: '2015-02-28T18:36:46.860Z'
disclosed_at: '2015-04-18T09:57:10.447Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# URGENT - Subdomain Takeover on status.vimeo.com due to unclaimed domain pointing to statuspage.io

## Metadata

- HackerOne Report ID: 49663
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: vimeo
- Disclosed At: 2015-04-18T09:57:10.447Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

**Brief**
This is an urgent issue and I hope you will act on it likewise.
Your subdomain status.vimeo.com is pointing to hosted.statuspage.io, but no statuspage was connected to it. This means that anyone can claim the subdomain by setting up a statuspage.io site and using "status.vimeo.com" as the name!

*You should immediately remove the DNS-entry for statu.vimeo.com pointing to statuspage.io.*

Since I have complete control over the subdomain I can do whatever I want on it. Creating a login form that would fool anyone, since it's present on a vimeo.com domain, abuse same origin bugs, get/set vimeo cookies, you name it!

**PoC**
PoC-link:
http://status.vimeo.com

**Remediation**
Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

Best,
Mathias

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
