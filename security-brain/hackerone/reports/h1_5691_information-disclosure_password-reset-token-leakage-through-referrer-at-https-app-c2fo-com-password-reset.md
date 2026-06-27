---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5691'
original_report_id: '5691'
title: Password reset token leakage through referrer at https://app.c2fo.com/password/reset/
weakness: Information Disclosure
team_handle: c2fo
created_at: '2014-04-02T21:42:52.229Z'
disclosed_at: '2014-04-15T02:39:05.517Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Password reset token leakage through referrer at https://app.c2fo.com/password/reset/

## Metadata

- HackerOne Report ID: 5691
- Weakness: Information Disclosure
- Program: c2fo
- Disclosed At: 2014-04-15T02:39:05.517Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

another bug I came across. There's a possible password reset token leakage on the password reset page. 

###Steps to reproduce

1. Go to https://app.c2fo.com/password-reset and request a new password (with your existing test account)
2. Click on the password reset link which you'll receive via email

The url bar should look like that: ```https://app.c2fo.com/password/reset/XXXX0de607bdbc2df949a7da49fabcfXXXXX```

So far so good.  You should see the logo of "Truste certified blabla" at the bottom. 

The logo is linked to the following url: ```https://privacy.truste.com/privacy-seal/Pollen,-Inc-/validation?rid=46f28cc9-128f-431a-8fff-6d19427150d9```. 

As you can see it's a link from a "https" page to a "https" url. That means that the referrer will be send to the target. That means that the password reset token will be leaked to the "truste"-company through the referrer.

Clicking on the logo should send the following request (including the referrer):

```
GET /privacy-seal/Pollen,-Inc-/validation?rid=46f28cc9-128f-431a-8fff-6d19427150d9 HTTP/1.1
Host: privacy.truste.com
[...snip...]
Referer: https://app.c2fo.com/password/reset/XXXX0de607bdbc2df949a7da49fabcfXXXXX
[...snip...]
Connection: keep-alive
```

A bad boy webmaster at the "truste"-company could collect the reset urls/token from the access.log.

###How to fix
I'd recommend to either remove the logo from this particular page or remove the link to the third-party company. 

Best regards,
Sebastian

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
