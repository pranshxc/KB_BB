---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411920'
original_report_id: '411920'
title: Leaking Username and Password in the URLs via Virustotal, can leads to account
  takeover
weakness: Information Exposure Through Sent Data
team_handle: chaturbate
created_at: '2018-09-20T19:04:52.919Z'
disclosed_at: '2018-09-21T21:17:30.192Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-sent-data
---

# Leaking Username and Password in the URLs via Virustotal, can leads to account takeover

## Metadata

- HackerOne Report ID: 411920
- Weakness: Information Exposure Through Sent Data
- Program: chaturbate
- Disclosed At: 2018-09-21T21:17:30.192Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Dear @chaturbate team

**Vulnerability Type**
> Critical Information Leakage in URLs via Virustotal.

**Vulnerability Severity**
High. 

**Description**
During my regular testing, went to https://www.virustotal.com/#%2Fdomain%2Fchaturbate.com
After reviewing all URLs more and more, I got 2 Interesting and Critical Endpoints like this
1) https://chaturbate.com/accounts/autologin/?username=aman4aman&password=Sha1$f5b91$0d6c2c053145a088373344d6fa08e97ce31312c6&next=/accounts/stopemails/
2) https://chaturbate.com/accounts/autologin/?username=haydos1995&password=Sha1$b1d15$90623ee4d02216eb06947fea9770187dd1a1398c&next=/accounts/stopemails/
3) https://chaturbate.com/accounts/autologin/?username=haydos1995&password=Sha1$b1d15$90623ee4d02216eb06947fea9770187dd1a1398c&next=/b/haydos1995

Above URLs are leaking Sensitive Crediantals like Username and Password with Sha1. 
This Information helps attackers to get username and password by decryption of sha1.

Password always should be stripped from URLs.

## Impact

Account Takeover using username and decrypted password.

**Remediation**
> Remove Sensitive URLs before leaking username and password. Password should be not send in clear format in the urls. Critical Information like password should not send via URL without stripping.

Thank You.

Happy to Help.

Best Regards,
@smit

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
