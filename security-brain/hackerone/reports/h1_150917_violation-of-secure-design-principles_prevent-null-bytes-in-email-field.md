---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150917'
original_report_id: '150917'
title: prevent null bytes in email field
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-07-12T14:15:47.713Z'
disclosed_at: '2016-07-13T03:00:25.610Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# prevent null bytes in email field

## Metadata

- HackerOne Report ID: 150917
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-07-13T03:00:25.610Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
Zawad here.

**Description**
I recently visited gratipay.com and logged in.
I found that invalid characters ( *eg. null bytes* ) were accepted in email field, which is obviously not an expected behavior.

**Steps to Reproduce**
1. Go to https://gratipay.com/~username/emails/
2. Enter `yourname@domain.com\0` or `you@abc.com%00` or `you@xyz.com$`
3. Now ***Inspect Element*** the field and change field type to **`text`** from **`email`**
4. Click on **Add email address**.
You'll see an error message ***Looks like you've found a bug! Sorry for the inconvenience, we'll get it fixed ASAP!***
Now reload the page and you'll see the email listed.

It means server side validation of email is not okay.
Validation should be improved.

For your reference, #3227 and #3991 are same kind of bug which were resolved.

----------------
Zawad

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
