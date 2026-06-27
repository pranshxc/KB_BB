---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222667'
original_report_id: '222667'
title: Possible SSRF in email server settings(SMTP mode)
weakness: Server-Side Request Forgery (SSRF)
team_handle: nextcloud
created_at: '2017-04-21T04:40:14.878Z'
disclosed_at: '2017-05-15T14:28:12.484Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Possible SSRF in email server settings(SMTP mode)

## Metadata

- HackerOne Report ID: 222667
- Weakness: Server-Side Request Forgery (SSRF)
- Program: nextcloud
- Disclosed At: 2017-05-15T14:28:12.484Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:
vul address `https://demo.nextcloud.com/xxx/settings/admin/additional`,when you change `smtp server address` ,you will get some different hints.

Reproduce steps:

1.Go to `https://demo.nextcloud.com/xxx/settings/admin/additional`,choose `SMTP` mode

2.Set server address to "172.17.1.0`,then you will get screenshot(nextcloud1.png),it means not on the same network segment

3.Set server address to "172.17.0.0`,then you will get screenshot(nextcloud2.png),it means the address not exists or doesn't open any port to access

4.Set server address to "172.17.0.1` and port to empty,then the test email will send successfully!
it means this host exists and opens a smtp port

5.Set server address to "172.17.0.1` and port to `22`,then you will get screenshot(nextcloud3.png),it means the address exists,but can not access to the port

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
