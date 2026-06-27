---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173501'
original_report_id: '173501'
title: Stored XSS on Admin Access Page - Email field
weakness: Cross-site Scripting (XSS) - Generic
team_handle: revive_adserver
created_at: '2016-10-02T11:36:03.419Z'
disclosed_at: '2017-08-02T05:58:41.882Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on Admin Access Page - Email field

## Metadata

- HackerOne Report ID: 173501
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: revive_adserver
- Disclosed At: 2017-08-02T05:58:41.882Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

"Cricetinae" :)

###Short Description

The **Email** field is not sanitized on **Inventory > Admin Access** page resulting in to Stored Cross-Site Scripting vulnerability.

###Vulnerability Details

Cross-Site Scripting issue let's one to run a javascript of choice. It helps most of the client side risks including but not limited to phishing, temporary deface, browser key-logger and others. Exploitation frameworks like BeEF eases the offensive attack.

Stored XSS is more risky than the reflected ones because of the fact that the malicious script is persisted across. It can affect all the time and all the users who has the access to the page.

### Attack Vector
As this is a stored XSS, the attack vector lies in one user phishing other users. If there are multiple administrators, one admin can get a javascript backdoor on another admin's browser.

### Steps to Reproduce
To effectively illustrate one user affect another user, please create 2 admin accounts and follow the below instruction:
* Login as `admin1`. Navigate to **Preferences** *>* **Change E-mail**
* Enter the current password and `admin1@example.com<script>alert('xss');</script>` for *Email address* field. Save and logout
* Login as `admin2`. 
* Navigate to **Inventory** *>* **Admin Access** and notice the alert box.

Attached screenshot for a reference.

### Test Environment Details
Version: Latest as on Oct 2: revive-adserver-4.0.0 downloaded from the official source
Setup type: local
Browser: Firefox 47.0
OS: Mac OS X


Cheers,
Pavan

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
