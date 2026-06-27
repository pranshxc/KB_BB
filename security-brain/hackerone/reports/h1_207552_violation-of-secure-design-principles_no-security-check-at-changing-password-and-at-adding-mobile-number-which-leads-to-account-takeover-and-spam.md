---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '207552'
original_report_id: '207552'
title: No Security check at changing password and at adding mobile number which leads
  to account takeover and spam
weakness: Violation of Secure Design Principles
team_handle: khanacademy
created_at: '2017-02-19T21:12:21.445Z'
disclosed_at: '2017-02-21T20:45:12.417Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# No Security check at changing password and at adding mobile number which leads to account takeover and spam

## Metadata

- HackerOne Report ID: 207552
- Weakness: Violation of Secure Design Principles
- Program: khanacademy
- Disclosed At: 2017-02-21T20:45:12.417Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#Description

I have noticed that there is no security check at changing password. If someone gets a logged in account for 5 seconds, they are extremely likely to change the password of the account with the knowledge of the victim. also, while adding a mobile number / changing a mobile number, there is no sms / call verification which leads to spamming of any user using Khan Academy as source.

Since there is no sms verification, I could spam anyone (not necessarily khan academy user) with khan Academy notifications.


#Steps to reproduce

1. Click on the name of the profile on top right.
2. Select settings in the drop down menu.
3.  Change the password by just entering the new password, without knowing anything.
4.  Add the mobile number (if already entered, change ) of your choice, since there is no security check, they will be spammed by khan academy messages.


#Impact

Lack of security check at password change leaves a vulnerability open to attackers to change the password without knowing anything about the user.
Lack of verification of mobile while adding / changing mobile number leaves every mobile user open for spamming via Khan Academy.


#Screen shots/ References

███
F162091

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
