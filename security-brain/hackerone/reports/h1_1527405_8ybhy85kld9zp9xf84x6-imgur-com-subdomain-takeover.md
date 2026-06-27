---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1527405'
original_report_id: '1527405'
title: 8ybhy85kld9zp9xf84x6.imgur.com Subdomain Takeover
team_handle: imgur
created_at: '2022-03-31T21:52:51.964Z'
disclosed_at: '2022-06-03T17:45:44.292Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# 8ybhy85kld9zp9xf84x6.imgur.com Subdomain Takeover

## Metadata

- HackerOne Report ID: 1527405
- Weakness: 
- Program: imgur
- Disclosed At: 2022-06-03T17:45:44.292Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gents,
+ While testing ** Imgur ** I found an unclaimed subdomain which is; “8ybhy85kld9zp9xf84x6.imgur.com”, and I was able to claim it!
+ But actually I didn't upload or host a simple file like `mr_baka.html`, because I need to upgrade the account to be able to use this custom domain!
+ Anyway, you can verify that I was able to claim this subdomain by visiting https://8ybhy85kld9zp9xf84x6.imgur.com and clicking [Manage domain settings here.](https://mrbaka.squarespace.com/config#/settings/domains), which should lead you to my account; https://mrbaka.squarespace.com" .

### Before claiming:
+ {F1675230}

### After:
+ {F1675231}

## Impact

Subdomain Takeover may lead to below consequences:

- Phishing / Spear Phishing
- Malware distribution
- XSS
- Authentication bypass and more
- Credential stealing

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
