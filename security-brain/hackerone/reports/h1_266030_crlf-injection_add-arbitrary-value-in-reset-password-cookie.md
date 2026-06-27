---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '266030'
original_report_id: '266030'
title: Add arbitrary value in reset password cookie
weakness: CRLF Injection
team_handle: legalrobot
created_at: '2017-09-05T13:23:42.848Z'
disclosed_at: '2018-02-01T14:41:09.454Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# Add arbitrary value in reset password cookie

## Metadata

- HackerOne Report ID: 266030
- Weakness: CRLF Injection
- Program: legalrobot
- Disclosed At: 2018-02-01T14:41:09.454Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I recently discovered that we can add arbitery value in reset pass token and compromise the life time unlimitedly ..

After opening a reset password link I got these cookies ....for token expires timeout .

{
    "domain": ".app.legalrobot.com",
    "expirationDate": 1504618468.82726,
    "hostOnly": false,
    "httpOnly": false,
    "name": "tokenExpires",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "Tue%20Sep%2005%202017%2013%3A35%3A30%20GMT%2B0000%20(UTC)",
    "id": 2
}


There was a warning in a page like .....

Your password reset token expires in 21 minutes...

okay so I decoded the value and changed year to 2019 instead of 2017 ...and it's all done ....miracle i got this page  with different warning ...

Your password reset token expires in 2 years

okay there are some issue like content spoofing , attacker can do this again and again , generally after 21 minutes token must experies but after changing to two years it won't ....


attaching screenshot here ....

If you can please take a another look  #265652  i have attached a logical bug with fully video poc 


thanks again

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
