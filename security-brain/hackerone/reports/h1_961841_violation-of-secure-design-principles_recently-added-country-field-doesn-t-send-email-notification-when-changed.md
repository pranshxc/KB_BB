---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '961841'
original_report_id: '961841'
title: Recently added 'Country' field doesn't send email notification when changed
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2020-08-18T20:54:10.782Z'
disclosed_at: '2020-08-25T10:57:33.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 105
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Recently added 'Country' field doesn't send email notification when changed

## Metadata

- HackerOne Report ID: 961841
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2020-08-25T10:57:33.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team,

This is a small bug report. Actually I think there is no important security issue but I wanted to report it ¯\\_(ツ)_/¯
If you change your 'Country' information on account settings, HackerOne doesn't send `Your profile was recently changed` email.

**Description:**
There is an email notification system at HackerOne. If you change any information in your account, you will get an email notification from HackerOne like that :

{F954222}

And recently, HackerOne added a field called ´Country´ to account settings for future features.

{F954224}

But if you change your country, you will not get an email notification. This is just a small bug, no need for immediate actions :)

### Steps To Reproduce

1. Go to your HackerOne account settings (https://hackerone.com/settings/profile/edit)
2. Change your ´Country´ information
3. Check your email, you won't get any email notification.

You can check other fields, you will get an email when you change them (like name, location etc.)

I know some fields don't send any notifications, like social media links etc. They are frequently changeable fields, but I think the country information not. Also, HackerOne even sends email notifications on any change at ´Location´ field. This is so similar to ´Country´ field.

## Impact

HackerOne doesn't send email notification when any change at ´Country´ field in account settings

Regards,
Bugra

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
