---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '315879'
original_report_id: '315879'
title: Able to reset other user's password in https://card.starbucks.com.sg/
weakness: Improper Authentication - Generic
team_handle: starbucks
created_at: '2018-02-14T05:48:58.768Z'
disclosed_at: '2018-07-23T17:42:34.870Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Able to reset other user's password in https://card.starbucks.com.sg/

## Metadata

- HackerOne Report ID: 315879
- Weakness: Improper Authentication - Generic
- Program: starbucks
- Disclosed At: 2018-07-23T17:42:34.870Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description**
In the website https://card.starbucks.com.sg/ there is a password reset function (https://card.starbucks.com.sg/forgetPassword.php) that sends the password reset link to the user's email. By using a web proxy to monitor the request, the email address can be changed to allow the attacker to reset a victim(another email) password, thus allowing him to gain full access to the victim's starbucks account and starbucks card.

**Summary**
The attacker request a password reset and obtains the password reset link in his email. By using a web proxy, he can use the password reset token and modify the his own email to a victim's email and the password reset will be used for the victim instead of the attacker.

**Steps to Reproduce**
1)Attacker visits https://card.starbucks.com.sg/forgetPassword.php and enters his account's email
2)The link is sent to the attacks email's inbox and he clicks on the link while having a proxy monitor the request(burp)
3)The attacker then modifies the email to put the victim's email in these 2 requests as shown in the image below F263235 & F263234
4)Upon submitting the request, the password will be changed and the victim's password will be changed to the desired password

## Impact

This attack does not require the victim to perform any actions and yet the account can be taken over by the attacker and this leaks the victim's personal information and starbucks card which can be used to purchase items. The attacker can also capture the session id.

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
