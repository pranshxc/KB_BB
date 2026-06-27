---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145612'
original_report_id: '145612'
title: No captcha on newsletter.nextcloudcom leaves vulnerable to email spammers
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-18T02:52:58.927Z'
disclosed_at: '2016-06-19T12:16:42.597Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# No captcha on newsletter.nextcloudcom leaves vulnerable to email spammers

## Metadata

- HackerOne Report ID: 145612
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-06-19T12:16:42.597Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The lack of a captcah or verificationcodeX (it's empty) in your phplist configuration allows attackers to use this mail for to send as much spam as they like to victims. I did not reach an email sending limit when I had tested this.

PoC images below:

Burp suite automated requests: https://gyazo.com/2b171479a41086057db0f4f2b3f30eea
Result in inbox: https://i.gyazo.com/347f5cd8c94a5715db72f959640ec7a1.png

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
