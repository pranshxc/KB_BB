---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208407'
original_report_id: '208407'
title: Able to create basic user account via Google login on HackerOne Drupal CMS
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2017-02-23T12:59:58.613Z'
disclosed_at: '2017-04-25T07:38:05.456Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- improper-authentication-generic
---

# Able to create basic user account via Google login on HackerOne Drupal CMS

## Metadata

- HackerOne Report ID: 208407
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2017-04-25T07:38:05.456Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi,
I've found that hackerone.com has drupal installed and when I navigated to this URL
https://www.hackerone.com/user/password
Found "Log in" and "password reset option".
When I clicked on login it redirected me to google login
Then I login using my gmail account and it redirected to hackerone.com
Then I requested to pasword reset and got link from email and able to acces the 
 internal drupal

**Description (Include Impact):**
Able to create a new account on that CMS.

### Steps To Reproduce

1. Navigate to this https://www.hackerone.com/user/password
2. Click "Log in" using google account.
3.Again navigate to this  https://www.hackerone.com/user/password

put the google mail and click on the request.

A  one-time login link will be provided to that email





POC:(Unlisted)
https://youtu.be/lBio9OZpLpM

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
