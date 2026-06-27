---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329209'
original_report_id: '329209'
title: Making further registrations difficult on Vanilla forum
weakness: Uncontrolled Resource Consumption
team_handle: vanilla
created_at: '2018-03-23T14:51:49.743Z'
disclosed_at: '2020-06-11T14:03:43.734Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Making further registrations difficult on Vanilla forum

## Metadata

- HackerOne Report ID: 329209
- Weakness: Uncontrolled Resource Consumption
- Program: vanilla
- Disclosed At: 2020-06-11T14:03:43.734Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
After registering the account, user gets a verification email. There is a number assigned in that mail and it is incremented for next user. Trying to verify the next number with same code shows user not found but will create problem for next person registering the account.

**Description:**

## Steps to reproduce:

1. Register an account on https://open.vanillaforums.com . I registered with alpesh73768@gmail.com and username alpesh73768

2.  You will get a confirmation mail like https://open.vanillaforums.com/entry/emailconfirm/67421/nSBDdPuH2zdZlRYiYCgvnYJZOUCmZMLE

If you just change the number here 67421 and increment by 1 , url becomes, https://open.vanillaforums.com/entry/emailconfirm/67422/nSBDdPuH2zdZlRYiYCgvnYJZOUCmZMLE  

Load this url in browser and you will get error "user not found"

3. Now when next user tries to register on the site he will see this error on registering " user 67422 not found".  Adding the image below

Image- Vanilla 1

4. If he again tries with same details, he will get error:

The name you entered is already used by another member
The email is entered i already used by another member

Image- Vanilla 2.

5. This user will also get no confirmation email in his email id. Only if he logs in and then sends a verification email again, he will be able to use the account.


Let me know if you need any more information.

## Impact

Can be abused to prevent registrations on the forum. Not a standard practice for a reputed forum.

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
