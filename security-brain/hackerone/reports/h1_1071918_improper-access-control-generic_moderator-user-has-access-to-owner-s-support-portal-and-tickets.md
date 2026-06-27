---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1071918'
original_report_id: '1071918'
title: Moderator user has access to owner's support portal and tickets
weakness: Improper Access Control - Generic
team_handle: logitech
created_at: '2021-01-05T13:15:18.824Z'
disclosed_at: '2021-01-20T23:49:51.153Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.streamlabs.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Moderator user has access to owner's support portal and tickets

## Metadata

- HackerOne Report ID: 1071918
- Weakness: Improper Access Control - Generic
- Program: logitech
- Disclosed At: 2021-01-20T23:49:51.153Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi there,

In https://streamlabs.com, there's a function where users can share his account to other users to manage their dashboard via following link.

``https://streamlabs.com/dashboard#/settings/shared-access``.

In shared-access setting, user can invite other user with two roles **Moderator** and **Administrator**

{F1145278}

As you can see in above picture, **Moderator**  has only access to Dashboard access, ability to skip/repeat alerts and cloudbot access.

But due to improper session management between https://streamlabs.com and https://support.streamlabs.com,
Shared-access users  can view/create/edit parent user's support tickets and profile which they should not access to.


## Steps To Reproduce:

Let's suppose there are two users which named User A and User B.

*  Login to User A account and browse to https://streamlabs.com/dashboard#/settings/shared-access

* Create an invitation link with **Moderator** role and copy link and Logout.

*  Login to User B account and accept the invitation by pasting copied link.

* Browse to https://streamlabs.com/dashboard#/settings/shared-access and you should notice that you have **Moderator** access to User A account.

* Click the User A name and you'll see the message in header of the page, ***"You are currently acting as User A, click here to return to User B"***

* Normally you only should be able to access dashboard and cloud bot function.

* Now, just browse the following link then you'll be logged into  User A's support tickets account.
        
        https://streamlabs.com/zendesk?brand_id=1&locale_id=1&return_to=https://support.stramlabs.com

I've attached  proof of concept video, hope it helps for you.

{F1145279}

## Impact

As I mentioned in above, Shared Access users can create/view/edit parent user's support tickets and profile which they shouldn't .

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
