---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1429148'
original_report_id: '1429148'
title: Subdomain Takeover at https://new.rubyonrails.org/
weakness: Privilege Escalation
team_handle: rails
created_at: '2021-12-16T21:21:48.544Z'
disclosed_at: '2022-03-03T21:12:32.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover at https://new.rubyonrails.org/

## Metadata

- HackerOne Report ID: 1429148
- Weakness: Privilege Escalation
- Program: rails
- Disclosed At: 2022-03-03T21:12:32.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Disclaimer

I know it's OOS but the issue is pretty serious because of the attractive domain name "new.rubyonrails.org" basically anyone could have put malware there.

## Summary
Hi!

I discovered that new.rubyonrails.org was pointing to an unclaimed Github Page, making it vulnerable to subdomain takeover.
I've managed to claim it in my Github-account and added a simple html file as POC:

{F1548667}

`https://new.rubyonrails.org`

## Mitigation
- Remove the DNS record

Best regards,
nagli

## Impact

Subdomain takeovers can be used for
- Cookies set to the root domain will be shared with this subdomain and can be obtained
- Stored XSS (arbitrary javascript code can be executed in a users browser)
- Phishing
- Hosting malicious content

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
