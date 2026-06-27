---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '803141'
original_report_id: '803141'
title: Unauthorized User Can Delete Any User Account
weakness: Privacy Violation
team_handle: nordsecurity
created_at: '2020-02-24T08:51:36.082Z'
disclosed_at: '2020-03-26T13:43:19.961Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 24
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Unauthorized User Can Delete Any User Account

## Metadata

- HackerOne Report ID: 803141
- Weakness: Privacy Violation
- Program: nordsecurity
- Disclosed At: 2020-03-26T13:43:19.961Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

###DESCRIPTION:

Your help desk allows creating tickets by email. Which means the user can send an email to the NordVPN support email to a add a new ticket to his activities. So when you send an email to `support@nordvpn.com` from your email address, this ticket will be created on the account that you have registered with the email.

###Steps To Reproduce:

1. Navigate this page:

        https://ucp.nordvpn.com/login/ 

2. Try to click the Email button below.
3. Try to fill up the form. See my attached photo.
{F726511}
4. As you notice I am not Authorized User and has no account in NordVPN.
5. Try to use the victim Email when deleting an account.
6. Few hours later.
7. The account of the victim was deleted successfully.

######Victim 1 :
{F726515}
######Victim 2 :
{F726516}

#####Note: The account was remove from the database

###Recommendation fix

* Critical actions like changing email or close account should be verify by sending PIN code to user email and asks him to reply back the code again.
* The second fix and I don’t like is disable creating tickets via your support email for more security
* Sending a confirmation link when deleting an account


Regards,

## Impact

The Unauthorized User Can Delete Any User Account

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
