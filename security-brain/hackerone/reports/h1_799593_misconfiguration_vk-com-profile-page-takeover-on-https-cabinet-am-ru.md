---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '799593'
original_report_id: '799593'
title: vk.com profile page takeover on https://cabinet.am.ru/
weakness: Misconfiguration
team_handle: mailru
created_at: '2020-02-19T12:24:13.680Z'
disclosed_at: '2020-03-10T15:45:06.699Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: 'Ext. O: Delegated subdomain or branded partner service'
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- misconfiguration
---

# vk.com profile page takeover on https://cabinet.am.ru/

## Metadata

- HackerOne Report ID: 799593
- Weakness: Misconfiguration
- Program: mailru
- Disclosed At: 2020-03-10T15:45:06.699Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description
Hi team,
While exploring https://cabinet.am.ru/ domain I found this site points to some social media accounts, One of them was a vk.com profile as https://vk.com/amrusocial but when I opened that link it showed me a 404 error so I successfully could register an account on vk.com and claim that user name.

## PoC
- Go to https://cabinet.am.ru/login/
- In the bottom of the page, In `Am.ru в соцсетях` section click on vk.com icon
- You will redirect to my profile page
(Please see attachments)

If you want I can change my id so you can claim this again.

Best regards,
@Naategh

## Impact

Impact of this is same as subdomain takeover, An attacker can claim nonexistent id (that used on your site) on social and post behind of your company that can hurt your credibility.

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
