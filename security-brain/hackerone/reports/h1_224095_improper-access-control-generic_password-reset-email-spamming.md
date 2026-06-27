---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224095'
original_report_id: '224095'
title: password reset email spamming
weakness: Improper Access Control - Generic
team_handle: owncloud
created_at: '2017-04-26T16:30:09.856Z'
disclosed_at: '2017-05-17T06:46:44.939Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# password reset email spamming

## Metadata

- HackerOne Report ID: 224095
- Weakness: Improper Access Control - Generic
- Program: owncloud
- Disclosed At: 2017-05-17T06:46:44.939Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

**Description:**

The email API `https://yoursite/index.php/login?user=admin` to reset password is unlimited and can be used as a email bomb

vuln address:`https://yoursite/index.php/lostpassword/email`

**Reproduce steps:(use demo.owncloud.org as example)**

1.`https://demo.owncloud.org/index.php/login` has a default user `admin`

2.then I try to visit `https://demo.owncloud.org/index.php/login`,then I try to login it using `username:admin || password:xxxxx`(password can be any wrong passwords)

3.Then owncloud will prompt you to reset password,if you click it,admin's email box will receive an email.

4.So I can use chrome console network panel to `replay XHR` continuously,then `admin's email box` receive many email.

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
