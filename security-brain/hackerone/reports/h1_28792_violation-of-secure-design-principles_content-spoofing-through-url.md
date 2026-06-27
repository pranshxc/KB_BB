---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28792'
original_report_id: '28792'
title: Content Spoofing through URL
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2014-09-20T20:35:23.124Z'
disclosed_at: '2014-09-20T20:45:52.506Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing through URL

## Metadata

- HackerOne Report ID: 28792
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2014-09-20T20:45:52.506Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello
I hope this is upto the level you guys think of accepting reports.
Specified content can be injected into the webpage as text using the URL

Consider this
https://secure.phabricator.com/diffusion/PHU/browse/master/In%20order%20to%20complete%20the%20sign%20up%20procedure%20please%20visit%20the%20following%20link/www.google.com/%3C----Google-----%3E

This can be misused in a number of ways
Attacker injecting text can redirect users to malicious sites
Attacker injecting text can prompt users with false messages like to logout or change their passwords

You must have an argument that URLs are displayed in address bars but many browsers do not perform that action especially mobile browsers

Please pay attention to this report.

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
