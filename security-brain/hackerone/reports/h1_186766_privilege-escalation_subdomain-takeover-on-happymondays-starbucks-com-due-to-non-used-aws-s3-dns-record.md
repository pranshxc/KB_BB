---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186766'
original_report_id: '186766'
title: Subdomain takeover on happymondays.starbucks.com due to non-used AWS S3 DNS
  record
weakness: Privilege Escalation
team_handle: starbucks
created_at: '2016-11-30T06:19:05.330Z'
disclosed_at: '2016-12-19T22:59:42.194Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 103
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover on happymondays.starbucks.com due to non-used AWS S3 DNS record

## Metadata

- HackerOne Report ID: 186766
- Weakness: Privilege Escalation
- Program: starbucks
- Disclosed At: 2016-12-19T22:59:42.194Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I discovered that happymondays.starbucks.com DNS CNAME record is pointing to S3 AWS bucket which doesn't exist. Here's the screenshot of vulnerable domain: {F138556}

As happymondays.starbucks.com was free to register on AWS S3 service and DNS-setup is already correct set-up: {F138557} 
I was able to claim the domain for PoC using the following set-up:  {F138558}
Also I have placed a two files located under root directory for validation: {F138559}
For mitigation you should immediately remove the DNS-entry for this domain. 

As you might consider, the impact of this are pretty significant. I now can publish whatever I want on this domain, even fetching httpOnly cookies. I would also be able to register SSL certificate for this domain through Let's Encrypt (it is only need meta/file verification to issue the certificate) That would end up with the ability to read secure cookies as well.

In addition, there's no way at all for a visitor of this page to validate that the content on this domain is not served by Starbucks, making it extremely easy to utilize this for targeting the organization by fake login forms / spear phishing using your own domain to plant the attack.

Cheers,
Danil

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
