---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '257194'
original_report_id: '257194'
title: Weak Bithdate Validation Implemented on Sign Up
weakness: Violation of Secure Design Principles
team_handle: khanacademy
created_at: '2017-08-06T08:15:58.710Z'
disclosed_at: '2017-08-14T16:11:31.055Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Weak Bithdate Validation Implemented on Sign Up

## Metadata

- HackerOne Report ID: 257194
- Weakness: Violation of Secure Design Principles
- Program: khanacademy
- Disclosed At: 2017-08-14T16:11:31.055Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The Birthdate Field on the KhanAcademy's [Sign Up](https://www.khanacademy.org/signup) page for new users has the year range from 2017 to 1897. 
{F210177}
However, while signing up for a new account, I was able to set the year to 1033 by manipulating the data being sent to the server and the account was successfully created. I can also confirm the year by checking the settings page of my account. Please refer to the screenshots for information.
{F210178}
{F210179}
{F210180}
{F210181}

I was also able to create a Child account with the same bug. Attaching the screenshot where the system says "You don't have an email address connected to this Khan Academy account. Since you're **_1017 years old_**, you can connect an email address to your account, which will unlink it from your parent's account.".
{F210182}
{F210183}

Suggestion: Proper validation should be implemented on Birthdate field so that the user is not able to set any year other than what is being displayed on the dropdown.

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
