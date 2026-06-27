---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145419'
original_report_id: '145419'
title: Email Spoofing
weakness: Phishing
team_handle: nextcloud
created_at: '2020-02-11T12:14:28.603Z'
disclosed_at: '2020-02-20T09:17:23.166Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- phishing
---

# Email Spoofing

## Metadata

- HackerOne Report ID: 145419
- Weakness: Phishing
- Program: nextcloud
- Disclosed At: 2020-02-20T09:17:23.166Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

An SPF/DMARC record is a type of Domain Name Service (DNS) record that identifies which mail servers are permitted to send email on behalf of your domain. The purpose of an SPF/DMARC record is to prevent spammers from sending messages on the behalf of your organization.

Remediation: Create a SPF record. And configure the DMARC policy so that only authorized and allowed mail server could send the mails on the behalf of the organization.

## Impact

Impact: The impact is, attacker can send the mail on the behalf of your organization and ask any kind of password or personal sensitive information from the victim.

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
