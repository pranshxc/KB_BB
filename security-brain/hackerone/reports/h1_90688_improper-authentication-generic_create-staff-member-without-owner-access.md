---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90688'
original_report_id: '90688'
title: create staff member without owner access
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-09-27T20:10:42.338Z'
disclosed_at: '2016-02-29T17:17:07.990Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# create staff member without owner access

## Metadata

- HackerOne Report ID: 90688
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2016-02-29T17:17:07.990Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi 

as you mentioned in #56726 

    "Only the the store owner is allowed to create new staff members"

admins can't create new staff members!
but with this vulnerability admins can use api to create user! 


steps:

- get access token for one full access admin (you can send request to xauth or sniff it from mobile device)

- send request with POST method to "https://~ShopName~.myshopify.com/admin/users.json"

data : 

{
"user": {
"email": "anyvalidmail@valid.com",
"first_name":"~fname~",
"last_name" : "~lname~",
"pin" : 1234
}
}


now, a user will be created! this user marked as POS staff member, without any access to admin shop!

-  go to "https://~ShopName~.myshopify.com/admin/auth/recover"

- enter new admin email address

- follow instructions to reset password
after recovering password user will convert to normal limited access

- open that first full access admin and then select new created admin

- unselect limited access

Done, a new admin will full access created!


Regards

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
