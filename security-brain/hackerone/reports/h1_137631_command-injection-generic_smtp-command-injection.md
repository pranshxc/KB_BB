---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137631'
original_report_id: '137631'
title: SMTP command injection
weakness: Command Injection - Generic
team_handle: ruby
created_at: '2016-05-10T19:39:06.912Z'
disclosed_at: '2016-06-30T07:28:29.785Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- command-injection-generic
---

# SMTP command injection

## Metadata

- HackerOne Report ID: 137631
- Weakness: Command Injection - Generic
- Program: ruby
- Disclosed At: 2016-06-30T07:28:29.785Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Net::SMTP is vulnerable to RCPT TO/MAIL FROM injection due to lack of input validation and conformance to the SMTP protocol.

Publicly disclosed already: http://www.mbsd.jp/Whitepaper/smtpi.pdf

People are wrongly assigning this to the mail gem (http://rubysec.com/advisories/OSVDB-131677/) and thinking it's fixed, when in fact the underlying vuln remains in Net::SMTP.

Discussed as an issue with the `mail` library here: https://github.com/rubysec/ruby-advisory-db/issues/215. And mentioned that it's likely an issue with net-smtp not doing input validation, per RFC spec: https://github.com/rubysec/ruby-advisory-db/issues/215#issuecomment-163906956

The mail gem *should* do input validation too, of course. But its responsibility is creating internet messages, and it would validate addresses against that spec. Its responsibility is not SMTP protocol compliance. Net::SMTP is.

Addressing this in Ruby in a timely manner will help resolve the considerable confusion that's emerged due to the lack of response to a publicly disclosed vulnerability.

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
