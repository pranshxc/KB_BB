---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '30975'
original_report_id: '30975'
title: Improper Verification of email address while saving Account Settings
weakness: Violation of Secure Design Principles
team_handle: x
created_at: '2014-10-10T17:56:31.045Z'
disclosed_at: '2015-08-13T13:36:18.927Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Improper Verification of email address while saving Account Settings

## Metadata

- HackerOne Report ID: 30975
- Weakness: Violation of Secure Design Principles
- Program: x
- Disclosed At: 2015-08-13T13:36:18.927Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

* Signup for Ads on twitter and navigate to "Account Settings" on ads.twitter.com/accounts

* Enter any email address and save Account Settings. Notice that the email address gets updated successfully.

* There is no verification email that is sent out to confirm that the email account updated actually belongs to the user account. 

This can be exploited or misused in a few ways. One such way is:

* An attacker changes his account settings to update the email address to a victim's email address.

* The attacker then navigates to Audience Manager and creates a list audience by uploading a CSV data file.

* After some time, the victim receives an email from twitter saying that "Your uploaded list test did not match enough people on Twitter to create a usable audience."  See attached screenshot. 

* The victim remains clueless as the attacker just leveraged the twitter platform to send this email to the victim. 

There might be other possible ways as well that an attacker can leverage the twitter email service to spam innocent victims.

Remediation:

On updating the email address under Account Settings, it should be verified by sending a confirmation link. 

PS - I understand that spamming is generally excluded from the scope of this bounty but when I clicked on the link provided under the Program details, it took me to a page which appears to only mention spamming attacks caused directly by attackers targeting victims. In this case, the attacker is completely out of the picture and is leveraging the twitter platform to spam victims. I just wanted to point that out.

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
