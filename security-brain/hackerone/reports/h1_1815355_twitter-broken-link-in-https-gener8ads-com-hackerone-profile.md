---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1815355'
original_report_id: '1815355'
title: Twitter Broken Link in https://gener8ads.com (Hackerone Profile)
team_handle: gener8
created_at: '2022-12-22T14:58:13.462Z'
disclosed_at: '2023-04-13T17:37:29.135Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.gener8ads.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Twitter Broken Link in https://gener8ads.com (Hackerone Profile)

## Metadata

- HackerOne Report ID: 1815355
- Weakness: 
- Program: gener8
- Disclosed At: 2023-04-13T17:37:29.135Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Gener8 has an unclaimed broken Twitter link on their Hackerone Profile which can be claimed by any malicious user. And then later the malicious user can exploit this issue to deceive new researchers to submit their legitimate findings to the wrong hands.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

 1.Visit Gener8 Profile On Hackerone. 
2.There you see that Gener8 has website and Twitter account are mentioned.
3.Click on the Twitter account, you will redirected to twitter account which i have been hijacked
4.Anyone could claim this username and broken link could be hijacked
5.So, I've impersonated your identity by forming a fake account named on that link. Here just for the PoC purpose, I've taken over that broken link by making an account with that username and added some context to show what impact can be made. Also, I'll surely release that username after your response.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

New researchers can be further deceived if they clicked on that hijacked link.
For Example a specific case might be: A malicious user can create a fake account on that broken redirection link and can deceive researchers arriving on that link. For example, the attacker can ask the researcher to submit his report to him first and if he approves, then only he can submit it to your official page. In this way, it can cause huge damage to your company if a report is critical in any case.
Here I've shown a sample impact by adding some info in that impersonated account.

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
