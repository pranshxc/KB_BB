---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '342693'
original_report_id: '342693'
title: Password reset token leakage via referer
weakness: Violation of Secure Design Principles
team_handle: semrush
created_at: '2018-04-24T10:25:00.266Z'
disclosed_at: '2018-08-14T13:25:02.602Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password reset token leakage via referer

## Metadata

- HackerOne Report ID: 342693
- Weakness: Violation of Secure Design Principles
- Program: semrush
- Disclosed At: 2018-08-14T13:25:02.602Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I have found that if user open the link of reset password and than click on any external links within the reset password page its leak password reset token in referer header.

Steps to reproduce:

1.Open Password reset page from email. 
2.Click on any social media link(on follow us section)
3.Intercept the request(I have used burp suite) 
4.You can see the link for reset password in referrer

## Impact

It allows the person who has control of particular site to change the user's password (CSRF attack), because this person knows reset password token of the user.

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
