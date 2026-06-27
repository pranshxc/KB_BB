---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92740'
original_report_id: '92740'
title: SPF records not found
weakness: Violation of Secure Design Principles
team_handle: coinbase
created_at: '2015-10-07T10:03:52.049Z'
disclosed_at: '2015-10-14T08:27:59.867Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# SPF records not found

## Metadata

- HackerOne Report ID: 92740
- Weakness: Violation of Secure Design Principles
- Program: coinbase
- Disclosed At: 2015-10-14T08:27:59.867Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is no TXT record in DNS zone that defines Sender Policy Framework entry for domain api.coinbase.com.

These are the best practices and need to be configure in DNS records to protect your mail servers. using SPF records will help in spam filtering as SPF records does helps in verifying the source IP of the email by comparing with a DNS TXT record with a SPF content which will only allow authentic mail server to send emails with our domain. DKIM on the other hand will use cryptography keys for validating a domain name identity that is associated with a message by providing cryptography authentication mechanism( private key to the server and public key on the DKIM record ) checking message content with applied digital signatures. SPF and DKIM will manage validating your outbound SMTP traffic.
DMARC policies needs to be set up for ensuring inbound SMTP traffic as well. with DMARC, message sender must verify their authentication with SPF and/or DKIM as DMARC consider DKIM and SPF as a combined authentication method. If DMARC policies of SPF and/or DKIM authentication failed the receiver have clear instructions to follow
for example : to reject or junk/spam email if it does not pass DMARC policy( passed-SPF and passed-DKIM authentication).

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
