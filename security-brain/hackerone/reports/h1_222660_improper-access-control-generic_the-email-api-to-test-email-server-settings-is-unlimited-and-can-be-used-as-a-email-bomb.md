---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222660'
original_report_id: '222660'
title: The email API to test email-server settings is unlimited and can be used as
  a email bomb
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2017-04-21T03:43:39.047Z'
disclosed_at: '2017-04-24T16:36:20.147Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-access-control-generic
---

# The email API to test email-server settings is unlimited and can be used as a email bomb

## Metadata

- HackerOne Report ID: 222660
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2017-04-24T16:36:20.147Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Description:**

The email-server settings test function in  `https://demo.nextcloud.com/xxx/settings/admin/additional` is unlimited and can be used as a email bomb.

And the test email API  is `https://demo.nextcloud.com/xxx/settings/admin/mailtest`

**Reproduce steps:**

1.Go to `https://demo.nextcloud.com/xxx/settings/personal` ,set your personal address to a email address which you want to attack .see screenshot(1)

2.Then go to `https://demo.nextcloud.com/xxx/settings/admin/additional`,`send test mail` ,then above email address will receive an test email.

3.So I can use chrome console network panel to `replay XHR` continuously,then my email box receive many email.see screenshot(2)

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
