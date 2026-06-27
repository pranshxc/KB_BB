---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209521'
original_report_id: '209521'
title: Content Spoofing on link.greenhouse.io
weakness: Violation of Secure Design Principles
team_handle: greenhouse
created_at: '2017-02-28T07:13:21.051Z'
disclosed_at: '2017-07-27T14:35:27.535Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing on link.greenhouse.io

## Metadata

- HackerOne Report ID: 209521
- Weakness: Violation of Secure Design Principles
- Program: greenhouse
- Disclosed At: 2017-07-27T14:35:27.535Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

#Description:

Content spoofing, also referred to as content injection or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

#Steps To Reproduce:

1- Go to  http://link.greenhouse.io
2- Add %0D%0AContent-Type%3A text%2Fhtml%0D%0A%0D%0AIt has been changed by a new one https://www.Attacker.com so go to the new one since this one . after / in link .

#Impact:

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. 
spoofing a lot of users .

#Suggested fix:

just use a 404 page that don't include attacker text .

I hope you will fix this issue as soon as possible .
Thank you so much .

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
