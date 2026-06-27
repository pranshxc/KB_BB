---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103432'
original_report_id: '103432'
title: URGENT - Subdomain Takeover in support.urbandictionary.com pointing to Zendesk
weakness: Code Injection
team_handle: urbandictionary
created_at: '2015-12-04T14:36:32.780Z'
disclosed_at: '2016-01-04T01:23:32.976Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- code-injection
---

# URGENT - Subdomain Takeover in support.urbandictionary.com pointing to Zendesk

## Metadata

- HackerOne Report ID: 103432
- Weakness: Code Injection
- Program: urbandictionary
- Disclosed At: 2016-01-04T01:23:32.976Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi. I found out that one of your subdomain which is http://support.urbandictionary.com/ can be taken over or is vulnerable to subdomain takeover. If youre gonna visit the site... you will see saying:

No help desk at support.urbandictionary.com

There is no help desk configured at this address. This means that the address is available and that you can claim it at http://www.zendesk.com/signup/

Which means that the subdomain can be claimed by anyone. Just easy, register and then set it up. Claimed. If claimed, hackers can do something bad about it especially to urbandictionary users.. Please fix Asap.. Thanks

For more info please read this:
http://labs.detectify.com/post/109964122636/hostile-subdomain-takeover-using

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
