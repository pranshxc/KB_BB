---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '418767'
original_report_id: '418767'
title: Hacker can bypass 2FA requirement and reporter blacklist through embedded submission
  form
weakness: Improper Authorization
team_handle: security
created_at: '2018-10-04T02:41:19.585Z'
disclosed_at: '2018-10-31T17:24:15.211Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 186
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Hacker can bypass 2FA requirement and reporter blacklist through embedded submission form

## Metadata

- HackerOne Report ID: 418767
- Weakness: Improper Authorization
- Program: security
- Disclosed At: 2018-10-31T17:24:15.211Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

### Summary:

A program owner can enforce the hackers to setup the two-factor authentication before submitting new reports to their program here: https://hackerone.com/parrot_sec/submission_requirements (see below image)

{F355169}

The [Parrot Sec](https://hackerone.com/parrot_sec) program has this feature enabled to enforce the hackers to setup `2FA` before submitting reports. I removed my `2FA` to test and it is good that i was block from submitting new reports (see below image)

{F355168}

---

### BYPASS 2FA Requirements using Embedded Submission:

Now i was able to bypass this 2FA setup requirements by using the Parrot Sec program __Embedded Submission Form__.

## Steps to reproduce:

  1. Login to your account and __remove__ your 2FA on your account (if you already setup it)
  2. Now go to https://hackerone.com/parrot_sec and hit `Submit Report` button, observed that you cannot submit report unless you will enable your 2FA.
  3. __BYPASS:__ Get the `Embedded Submission` URL on their [policy page](https://hackerone.com/parrot_sec): i get this ->> https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new
  4. Now submit report using that embedded submission form and you can submit reports without setting-up your 2FA, despite the program __enforce__ the user to setup the 2FA before submitting new reports.
  5. 2FA requirements successfully bypassed!

## Impact

Bypassing the enabled protection/feature of the program.

Let me know if anything else is needed.

Regards
Japz

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
