---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243277'
original_report_id: '243277'
title: SSRF via webhook
weakness: Server-Side Request Forgery (SSRF)
team_handle: mixmax
created_at: '2017-06-26T16:39:25.035Z'
disclosed_at: '2017-07-18T18:20:49.659Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF via webhook

## Metadata

- HackerOne Report ID: 243277
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mixmax
- Disclosed At: 2017-07-18T18:20:49.659Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There exists an SSRF vulnerability with the account webhook feature, allowing an attacker to verify the existence of the EC2 metadata url and enumerate URL's.

POC:

1. Create a webhook at https://app.mixmax.com/dashboard/settings/rules with url `http://169.254.169.254/latest/meta-data/`.
2. Trigger this webhook by sending/receiving an email. Wait a few hours.
3. Note that an email is not sent saying the webhook failed. I tried for other internal urls such as 'http://localhost', but they sent a failure email, indicating that `http://169.254.169.254/latest/meta-data/` is open to the webhook.
4. In addition to verifying that this endpoint exists, an attacker could enumerate endpoints on this domain. For example, an attacker could enumerate MAC addresses at `http://169.254.169.254/latest/meta-data/network/interfaces/macs/xx:xx:...`.

Suggested fix:

Blacklist the AWS metadata url and any other sensitive internal urls.

Thanks.

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
