---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12506'
original_report_id: '12506'
title: Content Sniffing not disabled
weakness: Violation of Secure Design Principles
team_handle: secret
created_at: '2014-05-19T08:12:50.880Z'
disclosed_at: '2014-07-08T10:00:29.014Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Sniffing not disabled

## Metadata

- HackerOne Report ID: 12506
- Weakness: Violation of Secure Design Principles
- Program: secret
- Disclosed At: 2014-07-08T10:00:29.014Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL :- https://www.secret.ly/

Issue description :-
There was no "X-Content-Type-Options" HTTP header with the value nosniff set in the response. The lack of this header causes that certain browsers, try to determine the content type and encoding of the response even when these properties are defined correctly. This can make the web application vulnerable against Cross-Site Scripting (XSS) attacks. E.g. the Internet Explorer and Safari treat responses with the content type text/plain as HTML, if they contain HTML tags.

Issue remediation :-
Set the following HTTP header at least in all responses which contain user input:
X-Content-Type-Options: nosniff

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
