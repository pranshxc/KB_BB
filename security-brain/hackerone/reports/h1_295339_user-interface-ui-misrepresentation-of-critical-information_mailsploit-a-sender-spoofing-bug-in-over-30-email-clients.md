---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '295339'
original_report_id: '295339'
title: 'Mailsploit: a sender spoofing bug in over 30 email clients'
weakness: User Interface (UI) Misrepresentation of Critical Information
team_handle: ibb
created_at: '2017-12-05T11:38:04.408Z'
disclosed_at: '2019-09-19T20:34:46.811Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- user-interface-ui-misrepresentation-of-critical-information
---

# Mailsploit: a sender spoofing bug in over 30 email clients

## Metadata

- HackerOne Report ID: 295339
- Weakness: User Interface (UI) Misrepresentation of Critical Information
- Program: ibb
- Disclosed At: 2019-09-19T20:34:46.811Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Mailsploit is a collection of bugs in email clients that allow effective sender spoofing and code injection attacks. The spoofing is not detected by Mail Transfer Agents (MTA) aka email servers, therefore circumventing spoofing protection mechanisms such as DMARC (DKIM/SPF) or spam filters.

Bugs were found in over 30 applications, including prominent ones like Apple Mail (macOS, iOS and watchOS), Mozilla Thunderbird, various Microsoft email clients, Yahoo! Mail, ProtonMail and others.

In addition to the spoofing vulnerability, some of the tested applications also proved to be vulnerable to XSS and code injection attacks.

More informations are available on mailsploit.com

## Impact

It allows the attacker to display an arbitrary sender email address to the email recipient while bypassing spoofing protection mechanisms such as DMARC (DKIM/SPF) or spam filters.

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
