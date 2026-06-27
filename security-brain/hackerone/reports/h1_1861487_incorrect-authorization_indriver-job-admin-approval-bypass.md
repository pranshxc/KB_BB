---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1861487'
original_report_id: '1861487'
title: inDriver Job - Admin Approval Bypass
weakness: Incorrect Authorization
team_handle: indrive
created_at: '2023-02-03T16:35:23.279Z'
disclosed_at: '2023-07-05T09:43:12.826Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 139
asset_identifier: injob.indriver.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- incorrect-authorization
---

# inDriver Job - Admin Approval Bypass

## Metadata

- HackerOne Report ID: 1861487
- Weakness: Incorrect Authorization
- Program: indrive
- Disclosed At: 2023-07-05T09:43:12.826Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A vulnerability has been found in "inDriver Job", an application located at https://injob.indriver.com/, a platform that allows employers to **publish job offers** and candidates to sign up for them. It seems like the application has **heavy use**, with a plethora of job offers in many categories.

In the app, anyone can request to **create job offers**, but, to prevent spam, scamming and phishing, every job offer creation and edit **has to be approved by a site admin** before being published. This is essential, since it prevents the app from getting **flooded with scammers**.

The vulnerability discovered allows an attacker to **completely bypass** this approval step, allowing the publishing of arbitrary content.

## Technical Details:
On the last step of the job offer creation, the application makes a final `POST` request to `/api/graphql`, calling for `UpdateVacancyStatus`.

```
{"operationName":"UpdateVacancyStatus","variables":{"vacancyId":"█████","status":"MODERATION"}
...
```
Re-sending this request, but modifying the **"status" variable to "ACTIVE"**, bypasses the need for a moderator approval, **publishing the ad**.

## Video POC
██████████

## Steps To Reproduce:
*Note for Triager: A phone number is required for signup. To skip this step, I've attached my session cookies. Using these, you could reproduce the steps noted below.*

(Please see video for in-depth demo)
  1. In employer mode, create a new job offer
  2. Fill in the required fields
  3. After the creation, the offer will appear as "Pending Approval"
  4. In Burp Proxy, send the last "UpdateVacancyStatus" request to Repeater, modifying "status":"ACTIVE"
  5. The arbitrary ad will now show up as "Active", it will have been verified and published. All users will be able to see it.

## Impact

An attacker can use this vulnerability to upload arbitrary content, for **scamming**, **malware** or even **advertising** purposes.
It is also possible to **flood the platform** with infinite offers, making it unusable for legitimate users.

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
