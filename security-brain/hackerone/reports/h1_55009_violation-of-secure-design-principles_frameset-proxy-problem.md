---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55009'
original_report_id: '55009'
title: Frameset Proxy Problem
weakness: Violation of Secure Design Principles
team_handle: factlink
created_at: '2015-04-05T23:39:18.170Z'
disclosed_at: '2015-05-09T22:29:49.194Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Frameset Proxy Problem

## Metadata

- HackerOne Report ID: 55009
- Weakness: Violation of Secure Design Principles
- Program: factlink
- Disclosed At: 2015-05-09T22:29:49.194Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I was testing out the proxy pages (http://fct.li, http://staging.fct.li) and I found that if I create an HTML page with a frameset (not to be confused with iframe), then I would be able to get rid of the dialog (top right corner) that reads: "You're looking at this page through Factlink (visit original page)". So the page looks like its completely hosted by you guys.

Example (frameset):
http://fct.li/?url=http://zenzr.org/fl-frameset.html
http://staging.fct.li/?url=http://zenzr.org/fl-frameset.html

This is the source code for a frameset:
<frameset rows="100%,*" style="border:0; frameborder:0; framespacing:0;">
        <frame src="http://www.example.com/" style="border:0;" marginwidth="0" marginheight="0" noresize/>
</frameset>

A  hacker could easily create a phishing page and steal the user's credentials.

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
