---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83251'
original_report_id: '83251'
title: 'owncloud.com: Content Sniffing not disabled'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-08-18T20:01:11.259Z'
disclosed_at: '2015-11-12T10:32:50.289Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# owncloud.com: Content Sniffing not disabled

## Metadata

- HackerOne Report ID: 83251
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2015-11-12T10:32:50.289Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL :- https://owncloud.com

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
