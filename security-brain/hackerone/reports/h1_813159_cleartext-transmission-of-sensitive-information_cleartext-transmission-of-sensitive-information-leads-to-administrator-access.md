---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '813159'
original_report_id: '813159'
title: Cleartext Transmission of Sensitive Information Leads to administrator access
weakness: Cleartext Transmission of Sensitive Information
team_handle: helium
created_at: '2020-03-08T13:50:33.121Z'
disclosed_at: '2020-05-30T10:51:13.632Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: https://helium-console-dev.herokuapp.com/
asset_type: URL
max_severity: high
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Cleartext Transmission of Sensitive Information Leads to administrator access

## Metadata

- HackerOne Report ID: 813159
- Weakness: Cleartext Transmission of Sensitive Information
- Program: helium
- Disclosed At: 2020-05-30T10:51:13.632Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The weakness of the program is Cleartext Transmission of Sensitive Information through URL Leads to administrator access. This program is having one feature like we can add users like administrator and read-only, these are roles, into organizations. Here I get the administrator role at same organization by removing the original user id.

Vulnerable URL:  https%3A%2F%2Fconsole.helium.com%2Fusers

Steps to Reproduce:
1. After creating the account for your organization, go to the Users tab and here you can see your organization name on the top, now try to add a user by using the mail id with the role of the administration.
2. Then the opposite user will receive the invitation link from the first user, Click on the invitation link it will take you into the registration page of Console.helium.com, but here thing is, just go to URL of current page here you can see the organization name, inviter id and also invite receiver id and change the mail id of receiver and click on enter.
3. Now, you able to see the registration page again with different mail id in the field of the username and create a password for this id and click on the Register button.
4. Now, this last mail id will receive a confirmation link to complete the registration process, for this go to the mailbox and click on the link and after trying to log in.
5. After a successful login to the account, you can see the organization name of the inviter. Now you are also one the administrator of this organization.
6. To confirm this, go to a first user account who invited into the administrator role, here you can able see the mail id of the last user instead of the real one.
7. Yes… we have successfully done it.

## Impact

Full administrator account take over.


Severity:
Critical

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
