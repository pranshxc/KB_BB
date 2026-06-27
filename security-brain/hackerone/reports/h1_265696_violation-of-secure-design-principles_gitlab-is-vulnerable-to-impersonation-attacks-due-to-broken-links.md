---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265696'
original_report_id: '265696'
title: Gitlab is vulnerable to impersonation attacks due to broken links
weakness: Violation of Secure Design Principles
team_handle: gitlab
created_at: '2017-09-03T23:00:49.687Z'
disclosed_at: '2017-09-06T16:43:13.597Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- violation-of-secure-design-principles
---

# Gitlab is vulnerable to impersonation attacks due to broken links

## Metadata

- HackerOne Report ID: 265696
- Weakness: Violation of Secure Design Principles
- Program: gitlab
- Disclosed At: 2017-09-06T16:43:13.597Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good afternoon team,

#Vulnerability

There's a lot of possible attacks that can be carried out with broken external links as noted in this github post by edoverflow. https://gist.github.com/EdOverflow/24e0bb929169eb948bb7f3d0a2d5528f.

In this particular example I'm impersonating Ricardo who redesigned gitlabhq back in 2011.

#POC

Go to https://about.gitlab.com/2011/11/22/whats-next/ and Ricardo is hyperlinked to his github account. Well somewhere between 2011 and 2017 he decided to delete his profile. 

Before - F218161

After - F218162

Ricardo is back with a malicious url that has been shortened using bit.ly. Shortening the link hides that it's malicious. 

In conclusion I have taken over an embedded link inside the Gitlab.com domain. Please let me know if you have any questions. I am happy to help and will continue to look for broken links!

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
