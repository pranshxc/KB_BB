---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222080'
original_report_id: '222080'
title: The email API to reset password is unlimited and can be used as a email bomb
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2017-04-19T07:58:27.332Z'
disclosed_at: '2017-04-20T15:34:21.403Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- improper-access-control-generic
---

# The email API to reset password is unlimited and can be used as a email bomb

## Metadata

- HackerOne Report ID: 222080
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2017-04-20T15:34:21.403Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Description:**

The email API `https://demo.nextcloud.com/qazxsw/lostpassword/email` to reset password is unlimited and can be used as a email bomb

**Reproduce steps:**

1.Every `Instant trial`'s link is `https://demo.nextcloud.com/yourname`,and it always has a default user `admin`

2.then I try to visit one `https://demo.nextcloud.com/qazxsw/login?user=admin`,then I try to login it using `username:admin || password:xxxxx`(password can be any wrong password)  .see screenshot(1)

3.Then nextcloud will prompt you to reset password,if you click it,admin's email box will receive an email.see screenshot(2)

4.So I can use chrome console network panel to `replay XHR` continuously,then my email box receive many email.see screenshot(3)

**How to harm other people:**

1.visit any project which you don't own,for example `https://demo.nextcloud.com/test`
2.If this people has set email address for his `admin`,then you can try the above reproduce steps.

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
