---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2001913'
original_report_id: '2001913'
title: Create miscellaneous support ticket on anyone's account through support@hackerone.com
  email
weakness: Misconfiguration
team_handle: security
created_at: '2023-05-25T14:40:06.043Z'
disclosed_at: '2023-08-11T07:18:22.199Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: support.hackerone.com
asset_type: URL
max_severity: none
tags:
- hackerone
- misconfiguration
---

# Create miscellaneous support ticket on anyone's account through support@hackerone.com email

## Metadata

- HackerOne Report ID: 2001913
- Weakness: Misconfiguration
- Program: security
- Disclosed At: 2023-08-11T07:18:22.199Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I hope you're well,
Hackerone recently changed from Zendesk to Freshdesk , that introduced this vulnerability , This asset is not in scope but the reason I'm reporting this because of the severity of this vulnerability as this can cause high impact on integrity of support desk.

**Description:**
This vulnerability is similar to my previous finding [on Dropbox program](https://infosecwriteups.com/mail-server-misconfiguration-leads-to-sending-a-fax-from-anyones-account-on-hellofax-dropbox-bbp-aab3d97ab4e7?source=user_profile---------0----------------------------]) , So when we create a support ticket by sending email to support@hackerone.com then it creates a support ticket on Hackerone Support portal on Victim's support center account , I found that we can create support ticket on anyone's  by sending a fake email to support@hackerone.com , by putting victim's email in `FROM` field. This would create a support ticket on victim's account , attacker can use this to create miscellaneous tickets on anyone's account or they can create ticket on behalf of **Hackerone** staff. You can check the ticket (441828) , I created this ticket by sending a fake email.
We can use any fake emailer service for e.g https://emkei.cz/

### Steps To Reproduce

1. Go to https://emkei.cz/
2. Put victim's email in `From E-mail:	` field and support@hackerone.com in `To:` field
3. Enter anything in name , content , subject and click Send

██████

* Now a ticket would be created on behalf of victim

## Impact

* Using this bug an attacker can create miscellaneous tickets on behalf of victim or create unnecessary noise on victim's support desk account
* Attacker can create internal ticket on behalf of HackerOne employees

Best Regards
**Sayaan Alam**

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
