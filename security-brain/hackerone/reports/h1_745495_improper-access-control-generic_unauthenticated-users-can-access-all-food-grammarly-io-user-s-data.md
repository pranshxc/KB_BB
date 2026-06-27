---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '745495'
original_report_id: '745495'
title: Unauthenticated users can access all food.grammarly.io user's data
weakness: Improper Access Control - Generic
team_handle: grammarly
created_at: '2019-11-24T23:15:37.689Z'
disclosed_at: '2020-08-10T10:10:03.488Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 130
asset_identifier: food.grammarly.io
asset_type: URL
max_severity: low
tags:
- hackerone
- improper-access-control-generic
---

# Unauthenticated users can access all food.grammarly.io user's data

## Metadata

- HackerOne Report ID: 745495
- Weakness: Improper Access Control - Generic
- Program: grammarly
- Disclosed At: 2020-08-10T10:10:03.488Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** The food.grammarly.io site uses the Meteor framework, which uses publications and methods to communicate between the backend and frontend. Although the site seems to require being authenticated as a Grammarly employee to use it, most methods and publications work without being authenticated. I was able to list user data including emails, access tokens and admin status just by using the Chrome Developer tools.

**Description:** I discovered that the following Meteor publications work without being authenticated:

* activeUsers
* allExtraFood
* allOrders(date)
* allUsers
* allUserStats
* allVendors
* allVendorsItems
* extraFoodFromToday
* foodEventLog
* foodSettings
* itemsLimits
* monthlyTop
* vendorByName
* vendorHistoryFromToday
* vendorItemsByName
* vendorsHistory

This means I can access the data stored in the following Meteor collections:
* Meteor.users
* ExtraFood
* OrderItems
* UserStats
* Vendors
* VendorsItems,
* FoodEventLog
* FoodSettings
* VendorsItemsLimits
* MontlyTopItems
* VendorsHistory

The Meteor.users collection includes the email address of 300+ employees of Grammarly, along with their Okta and Google oauth access tokens, a hash of their login tokens, and their admin status. The FoodSettings collection also exposes some Grammarly user emails.

Based on the source code of the app, it seems that most Meteor methods also don't perform any authentication checks. But because they could perform destruction of data, I preferred not no use them when testing.


## Browsers Verified In:

  * Chrome
  * Firefox

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Visit https://food.grammarly.io and open the Chrome Developer Tools
  1. In the console, run `Meteor.subscribe('activeUsers')`
  1. Wait a few seconds, and run `Meteor.users.find().forEach(e => console.log(e))`
  1. You will see all user's information, as seen in the screenshots

## Supporting Material/References:

  * The [Meteor Security page](https://guide.meteor.com/security.html) explains how this vulnerabilities can be fixed by implementing proper access control in the Meteor methods and publications

## Impact

An attacker could use this vulnerability to get information about Grammarly employees. He/she could know which employees have admin privileges and target them in other attacks.

I wasn't able to use the Okta and Google tokens for anything of high impact. Also, the hashedLoginToken requires the attacker to reverse a SHA256 hash of a random secret, so exploiting it seems difficult.

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
