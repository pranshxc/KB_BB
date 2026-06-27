---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1636552'
original_report_id: '1636552'
title: Email Verification Bypass Allows Users to Add & verify Any Email  As Guardians
  Email
weakness: Privilege Escalation
team_handle: khanacademy
created_at: '2022-07-14T08:35:48.737Z'
disclosed_at: '2022-12-17T02:33:28.678Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- privilege-escalation
---

# Email Verification Bypass Allows Users to Add & verify Any Email  As Guardians Email

## Metadata

- HackerOne Report ID: 1636552
- Weakness: Privilege Escalation
- Program: khanacademy
- Disclosed At: 2022-12-17T02:33:28.678Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Go to https://www.khanacademy.org/signup and signup as learner keeping date of birth below 13 years.
{F1821117}
2. Now keep victims email as parent's email for example here I am keeping info@khanacademy.org as parents email and click on signup.
████
3. Now you will see a following message "Your parent or guardian must approve your account or it will be deleted in 7 days".
██████
4. Now go to https://www.khanacademy.org/settings/account and update your email to temporary email or any email you have access to.
██████████
██████
5. Now, you will receive a verification email in your temporary email you have access to. But don't click on the email. Now again change the email to info@khanacademy.org.

{F1821137} ███████
6. Now open the verification email you received in your temporary email account in an incognito tab and refresh your child's account. We have successfully tied info@khanacademy.org as parent account with email verification.

This is the account that I created : Username : ██████ Password : ██████████ Email : ████

█████████

## Impact

Attacker is able to bypass email verification.

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
