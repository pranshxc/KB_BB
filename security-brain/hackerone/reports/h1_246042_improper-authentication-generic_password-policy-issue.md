---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246042'
original_report_id: '246042'
title: Password Policy Issue
weakness: Improper Authentication - Generic
team_handle: wakatime
created_at: '2017-07-05T10:04:00.052Z'
disclosed_at: '2017-07-06T15:46:42.440Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-authentication-generic
---

# Password Policy Issue

## Metadata

- HackerOne Report ID: 246042
- Weakness: Improper Authentication - Generic
- Program: wakatime
- Disclosed At: 2017-07-06T15:46:42.440Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Greetings **Wakatime,**

I just found a weak password policy in your login page.

Some websites prevents the users to use password constructed of character combinations that otherwise meet company policy, but should no longer be used because they have been deemed insecure for one or more reasons, such as being easily guessed, following a common pattern, or public disclosure from previous data breaches. Common examples are 123456, qwerty, or the word password itself.

###Steps to reproduce###
A. 
1. Go to https://wakatime.com/signup.
2. Create an account by typing your email address and your password same as your email.
3. Hit "Sign Up for WakaTime" button. 
4. Your account will be created.

B.
1. Go to https://wakatime.com/signup.
2. Create an account by typing your email address and password to 123456.
3. Hit "Sign Up for WakaTime" button.
4. Your account will be created.

Some policies suggest or impose requirements on what type of password a user can choose, such as:

* the use of both upper-case and lower-case letters (case sensitivity)
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* prohibition of words found in a password blacklist
* prohibition of words found in the user's personal information
* prohibition of use of company name or an abbreviation
* prohibition of passwords that match the format of calendar dates, license plate numbers, telephone 
* numbers, or other common numbers

Refer to this link: https://en.wikipedia.org/wiki/Password_policy

Thanks for the time and effort you spent for reading my report.

Regards,
_________

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
